# backend.py 詳細解説

このファイルはサーバー側の処理を担当します。「厨房のシェフ」のような役割です。

---

## 目次

1. [ライブラリ読み込み](#1-ライブラリ読み込み)
2. [設定部分](#2-設定部分)
3. [ヘルパー関数](#3-ヘルパー関数)
4. [アクセス制御](#4-アクセス制御)
5. [メインハンドラ（app関数）](#5-メインハンドラapp関数)
6. [各APIエンドポイント](#6-各apiエンドポイント)

---

## 1. ライブラリ読み込み

```python
import os
import json
import base64
from datetime import datetime
import functions_framework
from openai import OpenAI
```

### 各ライブラリの役割

| ライブラリ | 役割 | 例え |
|-----------|------|------|
| `os` | 環境変数を読む | 「お店の設定書を読む」 |
| `json` | JSONデータを扱う | 「注文票を読み書きする」 |
| `base64` | データを変換する | 「暗号を解読する」 |
| `datetime` | 日時を扱う | 「時計を見る」 |
| `functions_framework` | Cloud Runで動かすため | 「厨房の設備」 |
| `openai` | ChatGPT APIを呼ぶ | 「料理のレシピ本」 |

### 詳細解説

#### `import os`

```python
import os
```

**何をするもの？**
- パソコン（サーバー）の「環境変数」を読み取るためのライブラリ

**環境変数とは？**
- コードの外に置く設定値
- 例：`OPENAI_API_KEY`（AIのパスワード）、`ALLOWED_EMAILS`（許可するメール）

**なぜ環境変数を使う？**
```
【悪い例】コードに直接書く
api_key = "sk-abc123..."  ← GitHubに公開したら大変！

【良い例】環境変数から読む
api_key = os.environ.get('OPENAI_API_KEY')  ← 安全！
```

**使われている場所（このファイル内）**
```python
# 134行目: 許可メールアドレスを取得
allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')

# 303行目: OpenAI APIキーを取得
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
```

---

#### `import json`

```python
import json
```

**何をするもの？**
- JSON形式のデータを扱うライブラリ

**JSONとは？**
```json
{
    "message": "こんにちは",
    "user": "田中さん"
}
```
- 人間にも読みやすく、プログラムでも扱いやすいデータ形式
- ブラウザとサーバーの間でデータをやり取りする時に使う

**使われている場所**
```python
# 160行目: JWTトークンを解読
return json.loads(decoded).get('email')

# 170行目: レスポンスを作成
body = json.dumps(body, ensure_ascii=False)
```

---

#### `import base64`

```python
import base64
```

**何をするもの？**
- データを「エンコード（変換）」「デコード（復元）」するライブラリ

**なぜ必要？**
- JWTトークン（ログイン証明書）はbase64でエンコードされている
- それをデコードしてメールアドレスを取り出す

**使われている場所**
```python
# 159行目: JWTトークンをデコード
decoded = base64.urlsafe_b64decode(payload).decode('utf-8')
```

---

#### `from datetime import datetime`

```python
from datetime import datetime
```

**何をするもの？**
- 現在の日時を取得する

**使われている場所**
```python
# 334行目: ヘルスチェックで現在時刻を返す
{'status': 'ok', 'timestamp': datetime.now().isoformat()}
```

---

#### `import functions_framework`

```python
import functions_framework
```

**何をするもの？**
- Cloud Run functions でHTTPリクエストを受け取るためのライブラリ
- Google公式が提供

**重要な使い方**
```python
@functions_framework.http   # ← この「デコレータ」が重要！
def app(request):           # ← この関数がリクエストを受け取る
    ...
```

**デコレータ `@` とは？**
- 関数に「目印」をつける仕組み
- 「この関数がHTTPリクエストを受け取りますよ」とCloud Runに教える

---

#### `from openai import OpenAI`

```python
from openai import OpenAI
```

**何をするもの？**
- ChatGPT（OpenAI）のAPIを呼び出すライブラリ

**使われている場所**
```python
# 303-309行目: AIに質問を送る
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'user', 'content': message}],
    max_tokens=1000,
    temperature=0.7
)
```

---

## 2. 設定部分

### ALLOWED_ORIGINS（CORS設定）

```python
ALLOWED_ORIGINS = ['*']
```

**何をするもの？**
- どのWebサイトからのアクセスを許可するかを決める

**`'*'` の意味**
- 「どこからでもOK」（開発用）

**本番環境では？**
```python
ALLOWED_ORIGINS = [
    'https://ai-chat-app-xxxxx.run.app'  # 自分のURLだけ許可
]
```

---

### ファイル読み込み

```python
with open('front.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    SCRIPT_CONTENT = f.read()
```

**何をしている？**

```
┌─────────────────────────────────────────────────────────────┐
│  with open('front.html', 'r', encoding='utf-8') as f:      │
│            ↑           ↑         ↑              ↑          │
│       ファイル名   読み取り    文字コード    変数名         │
│                    モード      （日本語対応）               │
└─────────────────────────────────────────────────────────────┘
```

**なぜ起動時に読み込む？**
- リクエストのたびに読み込むと遅くなる
- 一度読み込んでメモリに保存しておく

---

## 3. ヘルパー関数

「ヘルパー」= 補助する関数。メイン処理を助ける。

### set_cors_headers

```python
def set_cors_headers(headers, origin):
    """CORSヘッダー設定"""
    if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
        headers['Access-Control-Allow-Origin'] = origin or '*'
    headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    headers['Access-Control-Max-Age'] = '3600'
```

**CORSとは？**

```
【CORSがないと起こること】

サイトA (evil.com)
    ↓ あなたのサイトにリクエスト
サイトB (あなたのサイト)
    ↓
ブラウザ: 「違うサイトからのリクエストは危険！ブロック！」
```

**各ヘッダーの意味**

| ヘッダー | 意味 |
|---------|------|
| `Access-Control-Allow-Origin` | どのサイトからのアクセスを許可するか |
| `Access-Control-Allow-Methods` | どのHTTPメソッドを許可するか |
| `Access-Control-Allow-Headers` | どのヘッダーを許可するか |
| `Access-Control-Max-Age` | この設定を何秒間キャッシュするか |

---

### set_security_headers

```python
def set_security_headers(headers):
    """セキュリティヘッダー設定"""
    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Frame-Options'] = 'DENY'
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
```

**各ヘッダーの意味**

| ヘッダー | 意味 | 防ぐ攻撃 |
|---------|------|---------|
| `X-Content-Type-Options` | ファイルタイプを厳密に判断 | MIMEスニッフィング |
| `X-Frame-Options` | 他サイトへの埋め込み禁止 | クリックジャッキング |
| `X-XSS-Protection` | XSS攻撃を検知してブロック | XSS攻撃 |
| `Referrer-Policy` | リファラー情報の制限 | 情報漏洩 |

---

## 4. アクセス制御

### is_email_allowed 関数

```python
def is_email_allowed(email):
    if not email:
        return False
    lower_email = email.lower()

    allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
    allowed_emails = [e.strip().lower() for e in allowed_emails_str.split(',') if e.strip()]

    allowed_domains_str = os.environ.get('ALLOWED_DOMAINS', '')
    allowed_domains = [d.strip().lower() for d in allowed_domains_str.split(',') if d.strip()]

    if lower_email in allowed_emails:
        return True
    for domain in allowed_domains:
        if lower_email.endswith(domain):
            return True

    if not allowed_emails and not allowed_domains:
        print('⚠️ ALLOWED_EMAILS/ALLOWED_DOMAINS 未設定')
        return True
    return False
```

**処理の流れ**

```
┌─────────────────────────────────────────────────────────────┐
│  is_email_allowed("tanaka@example.com")                     │
├─────────────────────────────────────────────────────────────┤
│  1. メールアドレスが空？ → False                             │
│  2. 小文字に変換: "tanaka@example.com"                       │
│  3. 環境変数から許可リストを取得                             │
│     ALLOWED_EMAILS: "tanaka@example.com,yamada@test.com"    │
│     ↓ カンマで分割                                          │
│     ["tanaka@example.com", "yamada@test.com"]               │
│  4. 許可リストに含まれる？ → True                            │
└─────────────────────────────────────────────────────────────┘
```

**リスト内包表記の解説**

```python
allowed_emails = [e.strip().lower() for e in allowed_emails_str.split(',') if e.strip()]
```

これを分解すると：
```python
# 1. カンマで分割
parts = allowed_emails_str.split(',')  # ["tanaka@example.com", " yamada@test.com"]

# 2. 各要素を処理
allowed_emails = []
for e in parts:
    if e.strip():  # 空白を除去して空でなければ
        allowed_emails.append(e.strip().lower())  # 小文字にして追加

# 結果: ["tanaka@example.com", "yamada@test.com"]
```

---

### get_email_from_token 関数

```python
def get_email_from_token(id_token):
    """JWTトークンからメールアドレス取得"""
    try:
        payload = id_token.split('.')[1]
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += '=' * padding
        decoded = base64.urlsafe_b64decode(payload).decode('utf-8')
        return json.loads(decoded).get('email')
    except:
        return None
```

**JWTトークンの構造**

```
eyJhbGciOiJS...  .  eyJlbWFpbCI6InRh...  .  SflKxwRJSMeKKF2Q...
     ↑                    ↑                      ↑
  ヘッダー             ペイロード              署名
 （形式情報）        （ユーザー情報）       （改ざん防止）
                         ↑
                   ここにメールアドレスがある
```

**処理の流れ**

```python
# 1. ピリオドで分割して2番目（ペイロード）を取得
payload = id_token.split('.')[1]
# "eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSIsIm5hbWUiOiLnlLDkuK0ifQ"

# 2. Base64デコード用のパディング調整
padding = 4 - len(payload) % 4
if padding != 4:
    payload += '=' * padding

# 3. Base64デコード
decoded = base64.urlsafe_b64decode(payload).decode('utf-8')
# '{"email":"tanaka@example.com","name":"田中"}'

# 4. JSONとして解析してメールアドレスを取得
json.loads(decoded).get('email')
# "tanaka@example.com"
```

---

## 5. メインハンドラ（app関数）

```python
@functions_framework.http
def app(request):
```

**これがエントリポイント！**

```
┌─────────────────────────────────────────────────────────────┐
│  ユーザーがアクセス                                          │
│       ↓                                                     │
│  Cloud Run: 「エントリポイントは 'app' だな」                │
│       ↓                                                     │
│  @functions_framework.http がついた関数を探す                │
│       ↓                                                     │
│  def app(request): を実行！                                 │
└─────────────────────────────────────────────────────────────┘
```

**request オブジェクトの中身**

```python
request.method      # 'GET' または 'POST' など
request.path        # '/api/chat' などのパス
request.headers     # {'Authorization': 'Bearer xxx', ...}
request.get_json()  # {'message': 'こんにちは'} などのボディ
```

---

## 6. 各APIエンドポイント

### トップページ表示（`/`）

```python
if path == '/' and request.method == 'GET':
    headers['Content-Type'] = 'text/html; charset=utf-8'
    return (HTML_CONTENT, 200, headers)
```

**処理**
1. パスが `/` で、メソッドが `GET` なら
2. Content-Typeを `text/html` に設定（HTMLですよと伝える）
3. HTMLの内容、ステータスコード200、ヘッダーを返す

**戻り値の形式**
```python
return (本文, ステータスコード, ヘッダー)
```

---

### JavaScript配信（`/script.js`）

```python
if path == '/script.js' and request.method == 'GET':
    headers['Content-Type'] = 'application/javascript; charset=utf-8'
    return (SCRIPT_CONTENT, 200, headers)
```

**なぜ別で配信？**
- `front.html` の中に `<script src="script.js">` がある
- ブラウザは `script.js` を別途リクエストする
- そのリクエストに応答する必要がある

---

### アクセス権限チェック（`/api/check-access`）

```python
if path == '/api/check-access' and request.method == 'POST':
    try:
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return make_response({'allowed': False, 'error': '認証トークンがありません'}, 401, headers=headers)

        email = get_email_from_token(auth_header.split('Bearer ')[1])
        if not email:
            return make_response({'allowed': False, 'error': 'メールアドレス取得失敗'}, 401, headers=headers)

        allowed = is_email_allowed(email)
        print(f"アクセス: {email} → {'許可' if allowed else '拒否'}")
        return make_response({'allowed': allowed}, headers=headers)
    except:
        return make_response({'allowed': False, 'error': 'エラーが発生しました'}, 500, headers=headers)
```

**処理の流れ**

```
┌─────────────────────────────────────────────────────────────┐
│  1. Authorization ヘッダーを取得                             │
│     "Bearer eyJhbGciOiJS..."                                │
│                                                             │
│  2. "Bearer " で始まるか確認                                │
│     → 始まらなければ 401 エラー                             │
│                                                             │
│  3. トークンからメールアドレスを取得                         │
│     "tanaka@example.com"                                    │
│                                                             │
│  4. 許可リストに含まれるか確認                               │
│     → 含まれれば {"allowed": true}                          │
│     → 含まれなければ {"allowed": false}                     │
└─────────────────────────────────────────────────────────────┘
```

---

### チャットAPI（`/api/chat`）

```python
if path == '/api/chat' and request.method == 'POST':
    try:
        # 認証チェック
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return make_response({'error': 'ログインが必要です'}, 401, headers=headers)

        email = get_email_from_token(auth_header.split('Bearer ')[1])
        if not is_email_allowed(email):
            return make_response({'error': '権限がありません'}, 403, headers=headers)

        # 入力チェック
        body = request.get_json(silent=True) or {}
        message = body.get('message', '')

        if not message or not isinstance(message, str):
            return make_response({'error': 'メッセージを入力してください'}, 400, headers=headers)
        if len(message) > 10000:
            return make_response({'error': 'メッセージが長すぎます'}, 400, headers=headers)

        # AI呼び出し
        client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        completion = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': message}],
            max_tokens=1000,
            temperature=0.7
        )

        return make_response({'response': completion.choices[0].message.content}, headers=headers)

    except Exception as e:
        print(f'チャットエラー: {e}')
        return make_response({'error': 'AIの処理中にエラーが発生しました'}, 500, headers=headers)
```

**処理の流れ**

```
┌─────────────────────────────────────────────────────────────┐
│  1. 認証チェック                                             │
│     → ログインしているか？                                  │
│     → 許可されたユーザーか？                                │
│                                                             │
│  2. 入力チェック                                             │
│     → メッセージは空でないか？                              │
│     → 文字数は10000文字以内か？                             │
│                                                             │
│  3. AI呼び出し                                               │
│     → OpenAI API にメッセージを送信                         │
│     → 回答を受け取る                                        │
│                                                             │
│  4. 結果を返す                                               │
│     {"response": "AIの回答..."}                             │
└─────────────────────────────────────────────────────────────┘
```

**OpenAI API のパラメータ**

| パラメータ | 意味 | 値の例 |
|-----------|------|--------|
| `model` | 使用するAIモデル | `gpt-3.5-turbo`, `gpt-4` |
| `messages` | 会話履歴 | `[{'role': 'user', 'content': '質問'}]` |
| `max_tokens` | 回答の最大長 | `1000`（約750文字） |
| `temperature` | 回答の創造性 | `0`=固定的、`1`=創造的 |

---

## ステータスコードの意味

| コード | 意味 | 使用場面 |
|--------|------|---------|
| `200` | 成功 | 正常に処理完了 |
| `204` | 成功（本文なし） | OPTIONSリクエストへの応答 |
| `400` | リクエスト不正 | 入力値が不正 |
| `401` | 認証が必要 | ログインしていない |
| `403` | 権限なし | ログイン済みだが許可されていない |
| `404` | 見つからない | 存在しないパスにアクセス |
| `500` | サーバーエラー | 予期しないエラー |
