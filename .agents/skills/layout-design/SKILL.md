---
name: layout-design
description: Use after the design system is locked to plan the information architecture of all sections beyond the first view — what to show, in what order, for the page's goal.
metadata:
  aachat.headline.ja: "全セクションの情報設計"
  aachat.headline.en: "Section Information Architecture"
  aachat.description.ja: "ファーストビュー以降の全セクションについて、何をどの順で見せるかをページのゴールから逆算して設計し、粗いワイヤーとレスポンシブ方針まで決めます。"
  aachat.description.en: "Plans every section beyond the first view - what to show and in what order - working backward from the page goal, down to rough wireframes and responsive behavior."
  aachat.discovery.listed: "false"
---

# layout-design

デザインシステムが固まったあとに使う。ファーストビュー以降の全セクションの情報設計を行い、何を・どの順で・どう見せるかを決める。

## 入力

- 確定したデザインシステム（design-system の成果）。
- requirements-intake で整理した目的・主 CV・必須掲載要素。

## 行うこと

ページのゴールから逆算してセクションを並べる。ジャンルの定番構成は `knowledge/patterns/<genre>/sections.md` を参照し、案件に合わせて取捨選択する。

- 全セクションを列挙し、順序を決める。LP なら「共感 → 解決 → 裏付け → 行動」の感情導線、コーポレートならハブから各ページへの分岐を意識する。
- 各セクションについて、目的・主要素・CTA 配置を決める。
- 各セクションの粗いワイヤー（言葉でのブロック構成。「左にテキスト、右に画像」程度）を出す。
- レスポンシブの方針を決める（モバイル優先か、各セクションがモバイルでどう積み替わるか）。

## 出力

セクション構成の設計を session に短く共有し、nextjs-implement に渡す。実装に入る前に、大きな構成変更（セクションの増減や順序の大幅変更）が必要だと判断したら依頼者に確認する。細部は実装しながら詰めてよい。
