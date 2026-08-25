# Runtime skills

このディレクトリには、agent が session 実行時に使う skill を置きます。Discovery の子 skill カタログもこのディレクトリを優先して読みます。

```text
.agents/skills/<skill-name>/SKILL.md
```

各 `SKILL.md` の frontmatter には、Agent Skills 標準の `name` / `description` に加えて、公開時の表示に使う `metadata` を持たせます。

```yaml
---
name: skill-name
description: Protocol description used by Agent Skills consumers.
metadata:
  aachat.headline.ja: "短い日本語タイトル"
  aachat.headline.en: "Short English title"
  aachat.description.ja: "利用者向けの日本語説明"
  aachat.description.en: "English description for users"
  aachat.discovery.listed: "true"
---
```

`aachat.discovery.listed` は、skill 一覧に個別掲載する場合が `"true"`、この agent のページにだけ出す場合が `"false"` です。
