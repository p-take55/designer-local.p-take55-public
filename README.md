# design-agent

Web ページのデザインから Next.js 実装までを一貫して担う aachat エージェントです。

## できること

- 案件ブリーフから、ファーストビューを 3〜5 案、デザインを入れた Next.js の Vercel preview として提示する（URL を開いて選べる）。
- 選ばれた案を基準にデザインシステムを固め、全セクションを情報設計し、Next.js + Tailwind + shadcn/ui で全ページを実装する。
- 出来上がったサイトを自己レビューして、一貫性・余白・タイポの問題を改善コミットする。
- LP、コーポレートサイトを中心に対応する。ジャンル知識は `knowledge/patterns/<genre>/` に蓄積し、案件をこなしながら増やす。

デザインの発注側（Web ディレクターや上位のオーケストレーターエージェント）から使われることを想定しています。

## 使い方

```bash
aachat agent clone owner/repo --name design-agent
```

clone 後、project に参加させてから session を起動します。

```bash
aachat project assign <project> --agent design-agent
chat send <project> "@design-agent <案件ブリーフ>"
```

## 必要な env

案件ごとに新規 GitHub repo を作り Vercel に紐付けるため、依頼者（使う人）の権限で動くトークンを `environment.yaml` の `config.env[]` 経由で渡します。

- `GITHUB_TOKEN`: 案件 repo の作成・push。
- `VERCEL_TOKEN`: Vercel プロジェクト紐付け・preview/deploy。

値や provider ref は repo に置かず、ローカルの env provider に置きます（下記「env を script で使う」参照）。

## 構成

- `identity.md`: エージェントの人格・役割・skill ルーティングの正本
- `environment.yaml`: 必要な実行環境。依存は `config.packages` に、agent が使いたい env 名・用途は `config.env[]` に書く
- `memory/`: session 間で引き継ぐ状態、優先順位、未完了の会話
- `knowledge/patterns/<genre>/`: ジャンル別のデザイン定番パターン（lp / corporate-site）
- `.agents/skills/`: 実行時 skill。フェーズ軸の 6 つ（requirements-intake / first-view-proposal / design-system / layout-design / nextjs-implement / design-review）に加え、横断的に使う reference-compare / asset-generation / frontend-design

`.agents/skills/frontend-design/` は Anthropic 公式 skill を同梱したものです。ライセンスは同ディレクトリの `LICENSE.txt`（Apache-2.0）に従います。

## env を script で使う

`environment.yaml` の `config.env[]` で宣言した env 名は、`aachat up` がローカルの env provider
（`~/aachat/.state/env.toml` 経由で `run_env` または `infisical`）から値を解決し、
agent process env に注入します。session 起動後はそのまま環境変数として参照できます。

```yaml
# environment.yaml
config:
  env:
    - name: OPENAI_API_KEY
      purpose: OpenAI API access
```

```bash
# agent が呼ぶ script — そのまま $OPENAI_API_KEY が読める
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{...}'
```

```python
# Python script からも環境変数として参照
import os
api_key = os.environ["OPENAI_API_KEY"]
```

ルール:
- env 名は `[A-Z_][A-Z0-9_]*` のみ。`AA_*` は aachat runtime 予約 (`AA_TOKEN` / `AA_SESSION_ID` / `AA_WS_DIR` 等) なので使えない
- provider に値がなくても起動は止まらず、`up.log` の Launch Report に missing として出る。script 側は env 不在を前提に fail-fast に書く
- 値・provider ref・絶対パスは repo に書かず、ローカルの `~/aachat/.state/env.toml` だけに置く

## 注意

secret、token、JWT、PAT、秘密鍵は repo に含めないでください。
secret が必要なときは `environment.yaml` の `config.env[]` に env 名だけを書きます。
値・provider ref・ローカルパスは `~/aachat/.state/env.toml` などローカル設定にだけ置き、repo には含めません。
