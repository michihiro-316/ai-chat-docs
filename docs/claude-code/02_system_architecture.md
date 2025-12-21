# 02_system_architecture.md

システム全体のアーキテクチャを定義します。

## 内容

```markdown
# システム構成（アーキテクチャ）— フロントもバックエンドも Cloud Run

本ドキュメントは、フロントエンド（画面配信）もバックエンド（API）も
同じく Cloud Run 上で提供する前提で、システム全体の最小アーキテクチャを定義する。
```

## 構成パターン

### 推奨：単一 Cloud Run サービス（PoC向け）

```
[Cloud Run (single service)]
  GET  /            -> front.html
  GET  /static/*    -> script.js, css, etc
  POST /api/chat    -> server-side logic
  GET  /api/health  -> health check
```

**メリット**

- 構成が単純
- CORSが不要
- 運用が軽い

## データフロー

```
[Browser]
  front.html  (UI)
    ↓
  script.js   (state / auth / fetch)
    ↓ HTTPS (same origin, JSON)
[Cloud Run]
  /api/*      (server-side logic)
    ↓
[External Services]
  AI API / DB
```

## ルーティング規約

| パス | 用途 |
|------|------|
| `/` | HTML（UI） |
| `/static/*` | JS/CSS/画像 |
| `/api/*` | API |

## 禁止事項

- `/api` 以外のパスでAPIを生やす
- HTMLとJSの責務分離を崩す
- `front.html` にJSロジックを戻す
