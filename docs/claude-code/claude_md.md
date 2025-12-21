# CLAUDE.md

`.claude/CLAUDE.md` はClaude Codeが最初に読み込むエントリポイントです。

## 役割

- ルールファイルの読み込み順序を指定
- プロジェクト全体の概要を記述
- 他のドキュメントへの参照を提供

## 内容

```markdown
# Project Memory (Claude Code)

This repository uses modular project rules under `.claude/rules/`.

## Rules index (load order)
- 00_project_context.md
- 01_comment_policy.md
- 02_system_architecture.md
- 03_directory_structure.md
- 04_boundary_policy.md
- 05_security_notes.md
- 06_cloudrun_ops.md
- 99_for_non_engineers.md

## Notes
- Architecture assumes **frontend and backend are served from Cloud Run**.
- `02_architecture.md` is kept as a short compatibility stub; refer to `02_system_architecture.md`.
- Verify loaded memory via `/memory`.
```

## ポイント

- ファイル名に番号を付けることで読み込み順序を明示
- `00_` は最重要ルール、`99_` は補足情報という慣例
- `/memory` コマンドで読み込み状態を確認可能
