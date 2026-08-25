---
name: design-review
description: Use after implementation to self-review the site — take screenshots, check visual consistency, spacing, and typography, and commit improvements. Keep it lightweight; no quantitative metrics.
metadata:
  aachat.headline.ja: "デザインの自己レビュー"
  aachat.headline.en: "Design Self-Review"
  aachat.description.ja: "主要ブレークポイントのスクリーンショットを撮り、一貫性・視線誘導・レイアウト崩れを点検して改善をコミットします。定量メトリクスは作りません。"
  aachat.description.en: "Screenshots key breakpoints, checks consistency, visual hierarchy, and layout breakage, then commits improvements. Deliberately qualitative - no metrics."
  aachat.discovery.listed: "true"
---

# design-review

実装が一段落したあとに使う、自己レビューの skill。初期版は素朴に保つ。スクリーンショットを撮って自分の目で点検し、気になる箇所を直す、までに留める。定量メトリクスや自動回帰検出は作らない（必要になったら後段で足す）。

## 入力

- 実装済みサイトの Vercel preview URL（または最新 main）。

## 行うこと

session に既備のヘッドレスブラウザ（例: gstack-browse）で、主要ブレークポイントのスクリーンショットを撮る。最低でもモバイルとデスクトップの 2 つ。

撮った画面を次の観点で点検する。

- 一貫性: 余白・配色・タイポ・コンポーネントの見た目がセクション間で揃っているか。design-system のトークンから外れた値が紛れていないか。
- 視線誘導: 各セクションで見てほしい順に視線が流れるか。主 CTA が埋もれていないか。
- 崩れ: テキストのはみ出し、画像の比率崩れ、モバイルでの段組み崩れ、余白の詰まり / 開きすぎがないか。

## 直し方

気になった箇所を改善コミットとして main に積み、push して preview で再確認する。1 つ直すごとに見た目を確かめ、別の崩れを生んでいないかを見る。

## 出力

最終 preview URL と簡単な完了報告を session に出して案件を終える。報告には、どの FV 案を採用したか、主要な構成、残った仮置き（差し替え待ちの画像やコピー）を添えると依頼者が次の判断をしやすい。
