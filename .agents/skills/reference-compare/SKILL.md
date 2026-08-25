---
name: reference-compare
description: Use to tighten a design toward reference pages — render reference URLs in a headless browser, screenshot them, compare against your own screenshotted design, and iterate the fix loop. Self-contained and repeatable; callable from first-view-proposal or ad hoc.
metadata:
  aachat.headline.ja: "参考サイトへの寄せ込み"
  aachat.headline.en: "Reference Comparison Loop"
  aachat.description.ja: "参考ページをヘッドレスブラウザで撮影し、自分の案のスクリーンショットと見比べて差分を埋める修正を反復します。提案フェーズからでも単体でも使えます。"
  aachat.description.en: "Screenshots reference pages in a headless browser, compares them against your own design, and iterates fixes to close the gap. Usable standalone or from a proposal flow."
  aachat.discovery.listed: "true"
---

# reference-compare

参考ページを実レンダリングしてスクショを撮り、自分の案のスクショと並べて見比べ、差分を埋める修正を反復する skill。提案フェーズの寄せ込みにも、後からの「この参考にもっと寄せて」にも使う。何度でも回せる自己完結ループ。

## 入力

- 参考 URL（1 つ以上）。依頼者が共有したもの、または探索で見つけた事例。探索する場合は **案件と同じ業界、無ければ近接業界の、デザインクオリティが突出した（めちゃイケてる）トップ事例**を狙う。平凡な定番例で妥協しない（探し方は `first-view-proposal` のリサーチ節に準拠）。
- 比較対象＝自分の案。Vercel preview URL かローカル dev のいずれか。

## 行うこと（1 周）

1. session に既備のヘッドレスブラウザ（gstack-browse 等）で各参考 URL を開き、主要ブレークポイント（最低でもモバイルとデスクトップ）でスクショを撮って workspace に保存する（例: `.refs/<name>-desktop.png` / `.refs/<name>-mobile.png`）。遅延読み込みやアニメは描画が落ち着くまで待ってから撮る。
2. 自分の案を同じブレークポイントでスクショする。
3. 参考と自案を並べて目視で見比べ、差分を箇条書きで言語化する。観点:
   - ファーストビューの第一印象と視線の入り（最初に何が目に入るか）。
   - レイアウトと余白のリズム（セクションの間（ま）、要素間の密度）。
   - タイポ階層と情報密度（見出し／本文のコントラスト、詰め込みすぎ／間延び）。
   - 配色・コントラスト・コントラスト比。
   - 装飾・モーションの効かせどころ（Magic UI を使う箇所の妥当性）。
4. 差分から具体的な修正を 1〜数件に絞って実装し、push（またはローカル rebuild）して自案を撮り直す。
5. 「狙いに十分寄った」と判断するか、依頼者が指定した回数に達するまで 1〜4 を反復する。各周回で「見た差分 → 直したこと」を 1〜2 行で session に残し、進捗を共有する。

## 方針

- 参考は **構成・密度・余白のリズム・視線設計の良さを学んで自案に翻訳する** ために使う。レイアウトやコピーの丸コピー・トレースはしない。
- 1 周ごとに、直した結果が別の崩れ（他ブレークポイント・他セクション）を生んでいないか確認する。
- 定量メトリクスや自動ピクセル差分は作らない。デザイン判断は目視の定性比較に留める（必要になったら後段で足す）。

## 出力

寄せ込み後の案と、比較の要約を session に出す。要約には **ベンチマークに使った事例を URL 付きで列挙**し、各事例について「業界（同業／近接）」「どこを基準にしたか」「各周回で何を改善したか」を添える。提案フェーズで使った場合は、そのまま first-view-proposal の提示／意思決定に戻る（ベンチマーク事例の報告は提示にそのまま使う）。
