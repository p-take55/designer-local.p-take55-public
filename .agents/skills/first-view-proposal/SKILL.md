---
name: first-view-proposal
description: Use when requirements are ready to propose 3-5 first-view options. Creates a new GitHub repo, links Vercel, researches references, implements each concept as a branch, and returns Vercel preview URLs for the requester to choose from.
metadata:
  aachat.headline.ja: "ファーストビュー案の提示"
  aachat.headline.en: "First-View Proposals"
  aachat.description.ja: "新規 GitHub repo を作って Vercel と紐付け、ファーストビューを 3〜5 案それぞれ branch の preview として実装します。依頼者は URL を開いて採用案を選べます。"
  aachat.description.en: "Creates a GitHub repo, links Vercel, and implements 3-5 first-view concepts as branch previews so the requester can choose a direction from live URLs."
  aachat.discovery.listed: "true"
---

# first-view-proposal

このエージェントの体験の要。要件が整ったら使う。新規 GitHub repo を作り、Vercel と紐付け、ファーストビューを 3〜5 案、それぞれデザインを入れた Next.js の Vercel preview として提示する。依頼者は URL を開いて「ええやん」と感じた案を選ぶ。

狙いは、ワイヤーフレームや言葉の説明ではなく、最初から本気でデザインの入った動くプレビューを見せること。ここで「めっちゃええやん」と思わせられるかが勝負どころ。

## 準備（認証の確認）

`GITHUB_TOKEN` と `VERCEL_TOKEN` が env にあることを前提とする。無ければ fail-fast し、依頼者に `environment.yaml` の `config.env[]` 経由で渡すよう促す。

```bash
test -n "$GITHUB_TOKEN" || { echo "GITHUB_TOKEN がありません。environment.yaml の env で渡してください"; exit 1; }
test -n "$VERCEL_TOKEN" || { echo "VERCEL_TOKEN がありません。environment.yaml の env で渡してください"; exit 1; }
```

## repo 作成と scaffold

案件 slug を決める（後戻りが大きいので依頼者に確認する）。新規 repo を作り、Next.js + Tailwind + shadcn/ui を scaffold する。

```bash
gh repo create <owner>/<slug> --private --clone
cd <slug>
pnpm create next-app@latest . --ts --tailwind --app --eslint --src-dir --import-alias "@/*" --use-pnpm
pnpm dlx shadcn@latest init -d
git add -A && git commit -m "chore: scaffold next.js + tailwind + shadcn"
git push -u origin main
```

## Vercel 連携

`vercel link` で project を紐付け、GitHub 連携で push → 自動 preview が出る状態にする。

```bash
vercel link --yes --token "$VERCEL_TOKEN"
vercel git connect --yes --token "$VERCEL_TOKEN"
```

GitHub 連携が不安定なときは、各 branch を明示 deploy して preview URL を得る代替手段を使う。

```bash
vercel deploy --token "$VERCEL_TOKEN"   # 出力された preview URL を控える
```

## リサーチ

案件ジャンルの `knowledge/patterns/<genre>/first-view.md` を読み、FV の定番パターンを把握する。

そのうえで参考事例を集める。狙うのは **「案件と同じ業界、無ければ近接業界の、デザインクオリティが突出した（めちゃイケてる）トップ事例」**。定番をなぞっただけの平凡な事例ではなく、その業界の第一線ブランド・評価の高いサイト・受賞事例レベルを基準に置く。最初に出てきた数件で妥協せず、業界内で頭ひとつ抜けた事例を狙って探す。

- 出所: 依頼者が共有した参考 URL ＋ web 検索（その業界のリーディングブランド公式サイト、受賞・キュレーション系ギャラリーなど）。外部の有料 MCP（Mobbin など）は使わない。
- まず業界を特定し、「同業のトップ事例」→ 足りなければ「近接業界／同じ印象を狙う他業界のトップ事例」の順で広げる。
- 集めた事例から案件に合いそうな方向性を 3〜5 個に絞り、各方向性について「どんな商材・どんな印象を狙うか」と「どの事例のどこ（構成・余白・配色・モーション等）を参照するか」を言語化しておく。

## 各案の実装と提示

各コンセプトを `variant/<a|b|c...>` の branch で実装する。FV だけでよいが、デザインは本気で入れる。`frontend-design`（Anthropic 公式）skill の指針に従い、ありきたりな「AI 臭い」見た目を避けて production-grade な完成度を狙う。shadcn/ui と Tailwind を使い、配色・タイポグラフィ・余白のリズムで案ごとにはっきり差を出す。FV の動き・装飾（hero のアニメーション、テキストエフェクト、背景演出など）は `magicui` MCP ツールで実装例を取得して使い、第一印象のインパクトを上げる。

各案を一旦組んだら、`reference-compare` skill を回して参考事例と見比べ、レイアウト・余白のリズム・視線設計を狙いに寄せる。納得いくまで（または手戻りが見合う範囲で）反復してから push する。仮の画像はプレースホルダや適切なフリー素材で置き、コピーは要件に沿った実文に近いものを入れる（ダミーテキストのままにしない）。

```bash
git checkout main
git checkout -b variant/a
# FV を実装（差別化されたデザインで）
git add -A && git commit -m "feat: first-view variant A"
git push -u origin variant/a   # → Vercel preview URL が出る
```

これを案の数だけ繰り返す（`variant/b`, `variant/c` ...）。各 branch は main から切る。

すべての案が出揃ったら、次を aachat session に投稿し、依頼者にどれを採用するか選んでもらう。ここで意思決定を待ち、勝手に次フェーズへ進まない。

- 各案の preview URL 一覧とコンセプト要約（狙い・どんな印象か・どんな訪問者に効くか）。
- **ベンチマークに使った事例の報告**: 参照したトップ事例を URL 付きで列挙し、各事例について「業界（同業／近接）」「何が優れていてどこを基準にしたか」「どの案にどう反映したか」を簡潔に添える。依頼者が「何を基準に作ったか」を判断できる状態にする。

## 次フェーズへの引き継ぎ

依頼者が 1 案を選んだら、その variant branch を main に merge してから design-system skill に進む。

```bash
git checkout main
git merge --no-ff variant/<選ばれた案>
git push
```
