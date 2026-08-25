---
name: requirements-intake
description: Use at the start of a design project to read the brief and organize purpose, target audience, tone, and required elements. Confirm critical gaps via asks; declare assumptions for minor gaps and proceed.
metadata:
  aachat.headline.ja: "案件ブリーフの要件整理"
  aachat.headline.en: "Design Brief Intake"
  aachat.description.ja: "案件ブリーフを読み、目的・ターゲット・トーン・必須要素を構造化して整理します。致命的な不足は依頼者に確認し、軽微な不足は仮置きを宣言して先に進めます。"
  aachat.description.en: "Reads a design brief and organizes it into purpose, target audience, tone, and required elements. Confirms critical gaps with the requester and declares assumptions for minor ones."
  aachat.discovery.listed: "true"
---

# requirements-intake

案件の最初に使う。ブリーフを読み、後続フェーズが迷わず進める形に要件を整理する skill。

## 入力として読むもの

- 案件ブリーフ（aachat メッセージ本文）。
- 依頼者が共有した参考 URL（参考にしたいサイト、競合、既存ブランド素材）。
- 既存資産があれば渡されたもの（ロゴ、ブランドカラー、トンマナ資料）。

## 整理する項目

ブリーフから次を抽出して埋める。埋まらない欄は「不明」と明示する。

- ページの種類 / ジャンル（LP、コーポレートサイト、など）。
- ビジネスゴールと主 CV（無料登録、資料請求、問い合わせ、ブランド認知など）。
- ターゲット（誰が見るか。コーポレートなら複数オーディエンスを列挙）。
- トーン＆マナー（モダン / 信頼感 / 親しみ / 高級 など、言葉で）。
- 必須掲載要素（載せると決まっているコンテンツ、訴求ポイント）。
- 参考にしたい / 避けたいテイスト。
- 技術・ブランド制約（指定カラー、指定フォント、既存デザインとの整合など）。

ジャンルが判明したら、対応する `knowledge/patterns/<genre>/overview.md` を読んで、そのジャンルの評価軸を頭に入れてから次に進む。

## 不足の扱い

- 致命的な不足（ジャンルが不明、主 CV が不明、ターゲットが全く不明）は、`asks` で依頼者に確認する。これらが曖昧なまま FV を作っても後戻りが大きい。
- 軽微な不足（細かいコピー、二次的な掲載要素）は、自分の仮置きを宣言した上で進む。「◯◯は仮にこう置いて進めます」と一言残す。

## 出力

整理した要件サマリを、次フェーズ（first-view-proposal）が参照できる形で短くまとめる。案件をまたいで残すべきなら `memory/` に、その場の handoff なら session に出す。長くなりすぎないようにし、判断に必要な項目だけを構造化して残す。
