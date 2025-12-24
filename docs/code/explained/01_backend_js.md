# backend.js 詳細解説（Node.js版）

このファイルはサーバー側の処理を担当します。Python版と同じ機能ですが、JavaScript（Node.js）で書かれています。

---

## 目次 { data-toc-skip }

1. [ライブラリ読み込み](#1-ライブラリ読み込み)
2. [設定部分](#2-設定部分)
3. [ヘルパー関数](#3-ヘルパー関数)
4. [アクセス制御](#4-アクセス制御)
5. [メインハンドラ（app関数）](#5-メインハンドラapp関数)
6. [Python版との比較](#6-python版との比較)

---

## 1. ライブラリ読み込み

```javascript
const functions = require('@google-cloud/functions-framework');
const OpenAI = require('openai');
const fs = require('fs');
const path = require('path');
```

### Python版との比較

| 役割 | Python | Node.js |
|------|--------|---------|
| Cloud Run連携 | `import functions_framework` | `require('@google-cloud/functions-framework')` |
| OpenAI API | `from openai import OpenAI` | `require('openai')` |
| ファイル操作 | `open()` ※標準関数 | `require('fs')` |
| パス操作 | 文字列結合 | `require('path')` |
| 環境変数 | `import os` | 不要（`process.env` は標準） |

### 各ライブラリの解説

#### `require()` とは？

```javascript
const functions = require('@google-cloud/functions-framework');
```

**何をしている？**
- 外部ライブラリを読み込む
- Pythonの `import` と同じ

**`const` とは？**
- 再代入できない変数宣言
- 「この変数は変わらない」という意味

```javascript
const a = 1;
a = 2;  // エラー！ const は再代入できない

let b = 1;
b = 2;  // OK！ let は再代入できる
```

---

#### `fs`（File System）

```javascript
const fs = require('fs');
```

**何をするもの？**
- ファイルの読み書きを行うNode.js標準ライブラリ

**使われている場所**
```javascript
// ファイルを読み込む
const HTML_CONTENT = fs.readFileSync(path.join(__dirname, 'front.html'), 'utf8');
```

**Python版との比較**
```python
# Python
with open('front.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()
```

```javascript
// Node.js
const HTML_CONTENT = fs.readFileSync('front.html', 'utf8');
```

---

#### `path`

```javascript
const path = require('path');
```

**何をするもの？**
- ファイルパスを安全に扱うライブラリ

**なぜ必要？**
```javascript
// 悪い例：OSによってパスの区切り文字が違う
const filePath = 'folder/file.txt';    // Macでは動く
const filePath = 'folder\\file.txt';   // Windowsではこう

// 良い例：path.join が自動で調整
const filePath = path.join('folder', 'file.txt');  // どのOSでも動く
```

**`__dirname` とは？**
```javascript
path.join(__dirname, 'front.html')
```
- `__dirname` = このファイル（backend.js）があるフォルダのパス
- 例: `/app/code/nodejs/` など

---

## 2. 設定部分

### ALLOWED_ORIGINS

```javascript
const ALLOWED_ORIGINS = ['*'];
```

Python版と同じ。CORS設定。

---

### ファイル読み込み

```javascript
const HTML_CONTENT = fs.readFileSync(path.join(__dirname, 'front.html'), 'utf8');
const SCRIPT_CONTENT = fs.readFileSync(path.join(__dirname, 'script.js'), 'utf8');
```

**`readFileSync` とは？**
- `Sync` = 同期処理（読み込みが終わるまで待つ）
- 起動時に1回だけ読み込むので、Syncで問題ない

**Python版との比較**
```python
# Python（同期処理）
with open('front.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()
```

```javascript
// Node.js（同期処理）
const HTML_CONTENT = fs.readFileSync('front.html', 'utf8');

// Node.js（非同期処理）※今回は使わない
fs.readFile('front.html', 'utf8', (err, data) => {
    HTML_CONTENT = data;
});
```

---

## 3. ヘルパー関数

### setCorsHeaders

```javascript
function setCorsHeaders(res, origin) {
    if (ALLOWED_ORIGINS.includes('*') || ALLOWED_ORIGINS.includes(origin)) {
        res.set('Access-Control-Allow-Origin', origin || '*');
    }
    res.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.set('Access-Control-Max-Age', '3600');
}
```

**Python版との違い**

| 項目 | Python | Node.js |
|------|--------|---------|
| 引数 | `headers` 辞書 | `res` オブジェクト |
| 設定方法 | `headers['key'] = value` | `res.set('key', value)` |
| 配列検索 | `'*' in list` | `list.includes('*')` |

---

### setSecurityHeaders

```javascript
function setSecurityHeaders(res) {
    res.set('X-Content-Type-Options', 'nosniff');
    res.set('X-Frame-Options', 'DENY');
    res.set('X-XSS-Protection', '1; mode=block');
    res.set('Referrer-Policy', 'strict-origin-when-cross-origin');
}
```

Python版と同じヘッダーを設定。

---

## 4. アクセス制御

### isEmailAllowed

```javascript
function isEmailAllowed(email) {
    if (!email) return false;
    const lowerEmail = email.toLowerCase();

    const allowedEmails = process.env.ALLOWED_EMAILS
        ? process.env.ALLOWED_EMAILS.split(',').map(e => e.trim().toLowerCase())
        : [];
    const allowedDomains = process.env.ALLOWED_DOMAINS
        ? process.env.ALLOWED_DOMAINS.split(',').map(d => d.trim().toLowerCase())
        : [];

    if (allowedEmails.includes(lowerEmail)) return true;
    for (const domain of allowedDomains) {
        if (lowerEmail.endsWith(domain)) return true;
    }

    if (allowedEmails.length === 0 && allowedDomains.length === 0) {
        console.warn('⚠️ ALLOWED_EMAILS/ALLOWED_DOMAINS 未設定');
        return true;
    }
    return false;
}
```

### `process.env` とは？

```javascript
const apiKey = process.env.OPENAI_API_KEY;
```

**Python版との比較**
```python
# Python
import os
api_key = os.environ.get('OPENAI_API_KEY')
```

```javascript
// Node.js
const apiKey = process.env.OPENAI_API_KEY;
// ※ require('os') は不要！process は常に使える
```

**重要：Node.jsでは `import os` 不要**
- `process` はNode.jsのグローバルオブジェクト
- どこからでも `process.env.変数名` で環境変数を取得できる

---

### 三項演算子

```javascript
const allowedEmails = process.env.ALLOWED_EMAILS
    ? process.env.ALLOWED_EMAILS.split(',').map(e => e.trim().toLowerCase())
    : [];
```

**分解すると**
```javascript
// 条件 ? trueの時 : falseの時

if (process.env.ALLOWED_EMAILS) {
    // 環境変数がある場合
    allowedEmails = process.env.ALLOWED_EMAILS
        .split(',')                    // カンマで分割
        .map(e => e.trim())            // 各要素の空白を除去
        .map(e => e.toLowerCase());    // 小文字に変換
} else {
    // 環境変数がない場合
    allowedEmails = [];
}
```

---

### getEmailFromToken

```javascript
function getEmailFromToken(idToken) {
    try {
        const payload = idToken.split('.')[1];
        const decoded = Buffer.from(payload, 'base64').toString('utf8');
        return JSON.parse(decoded).email || null;
    } catch (e) {
        return null;
    }
}
```

**Python版との比較**

| 処理 | Python | Node.js |
|------|--------|---------|
| Base64デコード | `base64.urlsafe_b64decode()` | `Buffer.from(payload, 'base64')` |
| JSONパース | `json.loads()` | `JSON.parse()` |
| 文字列変換 | `.decode('utf-8')` | `.toString('utf8')` |

---

## 5. メインハンドラ（app関数）

### エントリポイントの定義

```javascript
functions.http('app', async (req, res) => {
    // 処理...
});
```

**Python版との比較**

```python
# Python
@functions_framework.http
def app(request):
    return (body, status, headers)
```

```javascript
// Node.js
functions.http('app', async (req, res) => {
    res.status(200).json({ ... });
});
```

**大きな違い**

| 項目 | Python | Node.js |
|------|--------|---------|
| 引数 | `request` のみ | `req` と `res` の2つ |
| 戻り値 | タプルを `return` | `res` オブジェクトで送信 |
| 関数名 | 関数定義で指定 | `functions.http('名前', ...)` で指定 |

---

### req と res

```javascript
functions.http('app', async (req, res) => {
    // req = リクエスト（ブラウザからの情報）
    // res = レスポンス（ブラウザに返す道具）
});
```

**req オブジェクト**
```javascript
req.method      // 'GET' または 'POST'
req.path        // '/api/chat' などのパス
req.headers     // { authorization: 'Bearer xxx', ... }
req.body        // { message: 'こんにちは' }
```

**res オブジェクト**
```javascript
res.status(200)           // ステータスコードを設定
res.json({ data: '...' }) // JSONで返す
res.send('HTML...')       // テキストで返す
res.set('Header', 'value') // ヘッダーを設定
```

---

### APIエンドポイントの例

```javascript
// トップページ
if (reqPath === '/' && req.method === 'GET') {
    res.set('Content-Type', 'text/html; charset=utf-8');
    return res.send(HTML_CONTENT);
}

// チャットAPI
if (reqPath === '/api/chat' && req.method === 'POST') {
    // 認証チェック
    const authHeader = req.headers.authorization;
    if (!authHeader?.startsWith('Bearer ')) {
        return res.status(401).json({ error: 'ログインが必要です' });
    }
    // ...
}
```

**`?.` とは？（オプショナルチェーン）**
```javascript
// authHeader が null や undefined でもエラーにならない
authHeader?.startsWith('Bearer ')

// 従来の書き方
authHeader && authHeader.startsWith('Bearer ')
```

---

## 6. Python版との比較

### 構文の違い

| 項目 | Python | Node.js |
|------|--------|---------|
| 関数定義 | `def func():` | `function func() {}` |
| 無名関数 | `lambda x: x` | `(x) => x` |
| 非同期 | `async def` | `async function` |
| 環境変数 | `os.environ.get()` | `process.env.NAME` |
| 配列操作 | `[e.strip() for e in list]` | `list.map(e => e.trim())` |
| 条件分岐 | `if x in list:` | `if (list.includes(x))` |
| 文字列判定 | `s.endswith('.com')` | `s.endsWith('.com')` |
| None | `None` | `null` |
| True/False | `True`, `False` | `true`, `false` |

---

### 同じ処理の比較

**環境変数から許可メールを取得**

=== "Python"

    ```python
    allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
    allowed_emails = [
        e.strip().lower()
        for e in allowed_emails_str.split(',')
        if e.strip()
    ]
    ```

=== "Node.js"

    ```javascript
    const allowedEmails = process.env.ALLOWED_EMAILS
        ? process.env.ALLOWED_EMAILS.split(',')
            .map(e => e.trim().toLowerCase())
            .filter(e => e)
        : [];
    ```

**レスポンスを返す**

=== "Python"

    ```python
    return make_response(
        {'response': 'Hello'},
        200,
        headers=headers
    )
    ```

=== "Node.js"

    ```javascript
    return res.status(200).json({ response: 'Hello' });
    ```

---

## まとめ

| 項目 | 説明 |
|------|------|
| `require()` | Pythonの `import` と同じ |
| `process.env` | 環境変数を取得（`os` は不要） |
| `req, res` | リクエストとレスポンスが分かれている |
| `res.json()` | JSONを返す |
| `res.send()` | テキスト/HTMLを返す |
| `async/await` | Pythonと同じ非同期処理 |

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ★ Python版との主な違い ★                                   │
│                                                             │
│  1. 戻り値の方法                                            │
│     Python: return (body, status, headers)                  │
│     Node.js: res.status(200).json(body)                     │
│                                                             │
│  2. 環境変数                                                │
│     Python: import os → os.environ.get()                    │
│     Node.js: process.env.NAME（import不要）                  │
│                                                             │
│  3. エントリポイント                                         │
│     Python: @decorator + def app():                         │
│     Node.js: functions.http('app', callback)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
