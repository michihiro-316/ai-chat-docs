# settings.json

`.claude/settings.json` はClaude Codeの権限を制御する設定ファイルです。

## 役割

- 禁止操作の定義
- チーム全体で共有する権限ルール
- Git管理対象

## 内容

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./**/*.key)",
      "Read(./**/*.pem)",
      "Read(./**/*credential*)",
      "Read(./**/*secret*)"
    ]
  }
}
```

## 設定項目

### deny（禁止）

| パターン | 説明 |
|---------|------|
| `.env`, `.env.*` | 環境変数ファイル |
| `secrets/**` | シークレットフォルダ |
| `*.key`, `*.pem` | 秘密鍵・証明書 |
| `*credential*` | 認証情報ファイル |
| `*secret*` | シークレット関連ファイル |

## settings.local.json との違い

| ファイル | 用途 | Git管理 |
|---------|------|---------|
| `settings.json` | チーム共有のルール | ○ |
| `settings.local.json` | 個人の許可設定 | × |

!!! warning "注意"
    `settings.local.json` は個人の作業環境に依存するため、`.gitignore` に追加することを推奨します。
