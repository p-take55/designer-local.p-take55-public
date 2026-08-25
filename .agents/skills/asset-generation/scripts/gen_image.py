#!/usr/bin/env python3
"""Generate one site image asset via OpenAI Images API (gpt-image-2).

One invocation produces one file for one purpose. Run several in parallel when a
page needs multiple assets; see the asset-generation SKILL.md for the enclosing
workflow and for what should stay a placeholder instead of being generated.

stdlib only — no pip install needed. Reads OPENAI_API_KEY from env.

Usage:
  python3 gen_image.py --prompt "<detailed prompt>" --out path/to/img.png \
      [--size 1536x1024] [--quality high]

Exit codes:
  0  success (writes image to --out, prints the path)
  2  OPENAI_API_KEY not set  -> caller skips the image
  1  API or other error      -> caller skips the image

API (verified May 2026):
  model: gpt-image-2 (alias of gpt-image-2-2026-04-21), endpoint POST /v1/images/generations.
  size:    1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or custom WxH.
  quality: auto (default), high, medium, low. high/4K is pricier — use medium for drafts.
  GPT image models always return base64 in data[0].b64_json (no response_format needed).
  Use 1536x1024 for desktop/web screens, 1024x1536 for mobile screens.
"""
import sys, os, json, base64, argparse, urllib.request, urllib.error


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="1536x1024")
    ap.add_argument("--quality", default="high",
                    choices=["auto", "high", "medium", "low"])
    args = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        print("OPENAI_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    payload = json.dumps({
        "model": "gpt-image-2",
        "prompt": args.prompt,
        "size": args.size,
        "quality": args.quality,
        "output_format": "png",
        "n": 1,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=payload,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print(f"HTTP {e.code}: {body[:500]}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"request failed: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        b64 = data["data"][0]["b64_json"]
    except (KeyError, IndexError, TypeError):
        print(f"unexpected response: {json.dumps(data)[:500]}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(base64.b64decode(b64))
    print(args.out)


if __name__ == "__main__":
    main()
