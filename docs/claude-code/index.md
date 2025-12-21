# Claude Code 設定

このセクションでは、Claude Code（Anthropic公式CLI）のプロジェクト設定について説明します。

<div class="download-section" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
<p style="color: white; margin: 0 0 0.5rem 0; font-weight: bold;">テンプレートをダウンロード</p>
<p style="color: rgba(255,255,255,0.9); margin: 0 0 1rem 0; font-size: 0.9rem;">プロジェクトにそのまま使える .claude フォルダ一式</p>
<a href="claude-template.zip" download style="display: inline-block; background: white; color: #667eea; padding: 0.5rem 1.5rem; border-radius: 4px; text-decoration: none; font-weight: bold;">📦 claude-template.zip</a>
</div>

## 概要

Claude Codeは `.claude` フォルダを使って、プロジェクト固有のルールや権限を設定できます。
これにより、AIがプロジェクトの文脈を理解し、一貫したコード生成を行います。

## フォルダ構成

```
.claude/
├── CLAUDE.md           # ルールのインデックス（エントリポイント）
├── settings.json       # 権限設定（チーム共有用）
├── settings.local.json # 権限設定（個人用・Git対象外）
└── rules/              # プロジェクトルール
    ├── 00_project_context.md
    ├── 01_comment_policy.md
    ├── 02_system_architecture.md
    ├── 03_directory_structure.md
    ├── 04_boundary_policy.md
    ├── 05_security_notes.md
    ├── 06_cloudrun_ops.md
    └── 99_for_non_engineers.md
```

## 各ファイルの役割

| ファイル | 役割 |
|---------|------|
| `CLAUDE.md` | ルールファイルの読み込み順序を定義 |
| `settings.json` | 禁止操作の定義（秘密情報の読み取り禁止等） |
| `rules/*.md` | コード生成時に従うべきルール |

## ルール一覧

| 番号 | ファイル | 内容 |
|------|---------|------|
| 00 | [project_context](00_project_context.md) | プロジェクトの前提条件 |
| 01 | [comment_policy](01_comment_policy.md) | コメント方針 |
| 02 | [system_architecture](02_system_architecture.md) | システム構成 |
| 03 | [directory_structure](03_directory_structure.md) | ディレクトリ構成 |
| 04 | [boundary_policy](04_boundary_policy.md) | 境界と型管理 |
| 05 | [security_notes](05_security_notes.md) | セキュリティ方針 |
| 06 | [cloudrun_ops](06_cloudrun_ops.md) | Cloud Run運用 |
| 99 | [for_non_engineers](99_for_non_engineers.md) | 非エンジニア向け説明 |

## 使い方

1. `.claude` フォルダをプロジェクトルートに配置
2. `CLAUDE.md` でルールの読み込み順序を定義
3. `rules/` 配下にプロジェクト固有のルールを記述
4. `settings.json` で権限を制御

Claude Codeは会話開始時にこれらのファイルを自動的に読み込み、ルールに従ってコード生成を行います。
