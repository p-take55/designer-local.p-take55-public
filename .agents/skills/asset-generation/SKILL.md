---
name: asset-generation
description: Use to enumerate the images a site needs and generate them with OpenAI gpt-image-2, placing the results into the Next.js project (public/) and wiring them in. Falls back to placeholders (and asks the requester for assets) for things generation shouldn't fabricate. Cost-aware.
metadata:
  aachat.headline.ja: "画像素材の生成と配置"
  aachat.headline.en: "Image Asset Generation"
  aachat.description.ja: "サイトに必要な画像を洗い出し、OpenAI の画像生成 API で作って public/ に配置します。生成が不適な実在物はプレースホルダにして依頼者に素材提供を仰ぎます。"
  aachat.description.en: "Enumerates the images a site needs, generates them via the OpenAI image API, and wires them into public/. Falls back to placeholders for anything generation should not fabricate."
  aachat.discovery.listed: "true"
---

# asset-generation

サイトに必要な画像素材を洗い出し、`gpt-image-2` で生成して Next.js プロジェクトに本番アセットとして配置する skill。プレースホルダのまま放置せず、生成できるものは生成し、生成が不適なものは依頼者に素材提供を仰ぐ。

生成スクリプトは `scripts/gen_image.py`（stdlib のみ・pip 不要、`OPENAI_API_KEY` を env から読む）。

## いつ使う

- `layout-design` 後〜`nextjs-implement` 中。各セクションに必要な画像が見えたタイミング。
- 既存サイトの仮置き画像を本番素材に差し替えるとき。

## 1. 必要画像の洗い出し

レイアウトとセクション構成から、必要な画像をすべて列挙する。各画像に **用途 / 配置場所 / 推奨サイズ・アスペクト / 形式 / 生成 or 素材依頼** を割り当て、表にして session に出す。よくある対象:

- hero ビジュアル（背景写真 or 抽象ビジュアル）
- 各セクションのイラスト・補助ビジュアル
- feature / benefit のアイコン的グラフィック
- 背景テクスチャ・パターン
- OGP 画像（`1200x630` 相当）、必要なら favicon 用の素材

## 2. 生成 or プレースホルダの判断

- **生成する**: 抽象ビジュアル、イラスト、背景・テクスチャ、雰囲気写真、OGP、アイコン的グラフィックなど、事実性が問われないもの。
- **生成しない（プレースホルダ＋素材依頼）**: 実在の商品・店舗・人物・受賞ロゴなど、生成だと事実やブランドが崩れるもの。仮置きのまま残し、差し替え箇所を明示して依頼者に実素材を依頼する。捏造した「それっぽい写真」を本番に紛れ込ませない。

## 3. プロンプト作成

用途ごとにプロンプトを分けて作る。`design-system` の配色・トーンに合わせる。

- 写実が欲しいなら `a realistic photograph of ...`、フラットイラストなら `a clean flat vector illustration of ...` のように様式を冒頭で明示する。
- 被写体・構図・色調・余白（テキストを乗せる前提なら被写体を片側に寄せる等）を具体的に書く。
- 画像内に文字を入れたくない箇所は `no text` を明示する（gpt-image-2 は文字を描けるが、UI に乗せる素材は文字なしが扱いやすい）。
- 1 ファイル = 1 用途。1 枚に詰め込まない。

## 4. 生成

まず `OPENAI_API_KEY` の有無をネットワークを使わず確認する。無ければ生成は行わず、全対象をプレースホルダにして依頼者に key 設定（`environment.yaml` の `config.env`）か素材提供を促す。

```bash
[ -n "$OPENAI_API_KEY" ] || { echo "OPENAI_API_KEY なし -> 生成せずプレースホルダ運用"; }
```

key があれば複数枚を **並列**で生成する（逐次は遅い）。サイズはアスペクトに合わせる: 横長 `1536x1024`、縦長 `1024x1536`、正方 `1024x1024`、OGP は `1536x1024` で作って後段で `1200x630` にトリミング。下書きは `--quality medium`、本番採用は `high`。

```bash
GEN=".agents/skills/asset-generation/scripts/gen_image.py"
python3 "$GEN" --prompt "<hero の英語プロンプト>"   --out public/hero.png    --size 1536x1024 --quality high &
python3 "$GEN" --prompt "<section1 の英語プロンプト>" --out public/about.png   --size 1536x1024 --quality high &
python3 "$GEN" --prompt "<og の英語プロンプト>"      --out public/og.png      --size 1536x1024 --quality high &
wait
ls -la public/*.png
```

欠けたものだけ 1 回リトライし、それでも失敗したらその対象はプレースホルダに切り替える。

## 5. 配置と参照

- 生成画像は `public/` に置き、コンポーネントから `next/image` で参照する。意味のある `alt` を入れる。
- OGP は各ページの `metadata`（`openGraph.images`）に設定する。
- 生成物を commit する。差し替え待ちのプレースホルダが残る場合は、どれが仮かを報告に明記する。

## コスト意識

- 画像生成は実費がかかる（gpt-image-2: 低品質 約 $0.01〜高品質4K 約 $0.41／枚）。1 セクション 1 枚を基本に、必要な分だけ生成する。むやみに枚数を増やさない。下書き段階は medium。
- `OPENAI_API_KEY` は env から読む。repo やドキュメントに key を書かない。

## 出力

配置した画像の一覧（用途・パス・生成 or 仮置き）と、依頼者に素材提供を仰ぐ項目を session に出す。
