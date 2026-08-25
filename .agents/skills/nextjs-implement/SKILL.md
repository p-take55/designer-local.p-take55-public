---
name: nextjs-implement
description: Use to implement all pages in Next.js (App Router) + Tailwind + shadcn/ui following the layout design, including component decomposition, responsiveness, and basic SEO.
metadata:
  aachat.headline.ja: "Next.js での全ページ実装"
  aachat.headline.en: "Next.js Implementation"
  aachat.description.ja: "情報設計に従って Next.js (App Router) + Tailwind + shadcn/ui で全ページを実装します。セクション単位のコンポーネント分割、レスポンシブ対応、基本 SEO を含みます。"
  aachat.description.en: "Implements all pages in Next.js (App Router) with Tailwind and shadcn/ui, including per-section components, responsive layout, and baseline SEO."
  aachat.discovery.listed: "false"
---

# nextjs-implement

情報設計に従って、全ページを Next.js で実装する skill。

## 入力

- layout-design のセクション構成とワイヤー。
- design-system のトークン（`tailwind.config.ts` / CSS 変数 / shadcn テーマ）。

## 実装方針

- App Router 構成で実装する。ページは `src/app/` 配下、共通レイアウトは `layout.tsx`。
- セクションごとにコンポーネントを分割する（`src/components/` に hero / features / pricing など）。1 コンポーネント 1 責務を守り、ファイルが肥大化したら分ける。
- `frontend-design`（Anthropic 公式）skill の指針に従い、ありきたりな「AI 臭い」見た目を避けて production-grade な完成度に仕上げる。
- shadcn/ui のコンポーネント（button / card / accordion など）を活用し、独自実装を増やしすぎない。
- アニメーション・装飾系（marquee / bento grid / animated beam / テキストエフェクト等）は `magicui` MCP ツールで実装例を取得して使う。shadcn/ui がベース UI、Magic UI が動き・装飾を足す役割。自前でアニメを書く前に Magic UI に該当コンポーネントがないか確認する。
- フォントは `next/font`、画像は `next/image` を使う。必要な画像が出てきたら `asset-generation` skill で洗い出して gpt-image-2 で生成し、`public/` に置いて参照する。生成が不適なもの（実在商品・人物・ブランド素材）はプレースホルダを仮置きし、差し替え箇所が分かるようにして依頼者に素材提供を仰ぐ。
- 基本 SEO を入れる: 各ページの `metadata`（title / description）、OGP、見出し階層（h1 は 1 ページ 1 つ）、適切な alt。
- レスポンシブ対応。design-system の spacing スケールに沿ってブレークポイントごとの余白・段組みを整える。

## 進め方

セクション単位でコミットし、こまめに push して Vercel preview で見た目を確認しながら進める。大きく作ってから一度に確認するのではなく、積み上げながら都度ブラウザで確かめる。

## 出力

全ページが実装された main。完了したら design-review skill に渡して自己レビューに入る。
