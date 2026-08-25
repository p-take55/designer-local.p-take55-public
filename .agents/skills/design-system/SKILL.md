---
name: design-system
description: Use after the requester selects a first-view option to lock in the design system (color, typography, spacing, tone) based on the chosen variant, and encode it in tailwind config / CSS variables.
metadata:
  aachat.headline.ja: "デザインシステムの確定"
  aachat.headline.en: "Design System Lock-In"
  aachat.description.ja: "採用されたデザインを起点に配色・タイポグラフィ・spacing をトークン化し、Tailwind config と CSS 変数、shadcn テーマに落とし込みます。"
  aachat.description.en: "Turns an approved design direction into color, typography, and spacing tokens, encoded in Tailwind config, CSS variables, and the shadcn theme."
  aachat.discovery.listed: "true"
---

# design-system

依頼者が FV 案を 1 つ選んだあとに使う。採用案を基準に、サイト全体で一貫させるデザインシステムを確定し、コードに埋め込む。

## 入力

- 選ばれた variant branch を main に merge した状態の repo。
- requirements-intake で整理したトーン＆マナーと制約。

## 確定する項目

採用された FV のデザインを起点に、サイト全体に展開できるトークンとして言語化する。

- カラーパレット: primary / secondary / accent / neutral（背景・境界・テキスト階調）/ semantic（success・warning・danger）。各色の役割を決める。
- タイポグラフィ: 見出しと本文のフォント、サイズスケール（h1〜小テキスト）、行間、字間。日本語と欧文の混在を考慮する。
- spacing スケール: 余白の基準単位とセクション間・要素間のリズム。
- 角丸・影・ボーダーのトーン: シャープかソフトか、フラットか立体的か。FV の印象と揃える。

トーンの基準が曖昧なときは `knowledge/patterns/<genre>/overview.md` の評価軸を参照する。

## 実装への落とし込み

確定したトークンをコードに反映する。

- `tailwind.config.ts` の `theme.extend` にカラー・フォント・spacing・角丸を定義する。
- `globals.css` に CSS 変数として色やフォントを置き、shadcn のテーマトークン（`--background` / `--foreground` / `--primary` など）に対応させる。
- フォントは `next/font` で読み込む。
- 規模が大きい、または依頼者と共有したい場合は `DESIGN.md` を repo に置き、デザインシステムの正本にする。

## 出力

デザインシステムを反映した main を push し、preview で適用を確認する。確認できたら layout-design skill に進む。
