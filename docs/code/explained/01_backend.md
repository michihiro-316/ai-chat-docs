# backend.py 詳細解説

このファイルはサーバー側の処理を担当します。「厨房のシェフ」のような役割です。

**このドキュメントでは、Pythonの基礎構文から丁寧に解説します。**

---

## 目次 { data-toc-skip }

1. [Python基礎：これだけ覚えよう](#1-python基礎これだけ覚えよう)
2. [ライブラリ読み込み](#2-ライブラリ読み込み)
3. [設定部分](#3-設定部分)
4. [ヘルパー関数](#4-ヘルパー関数)
5. [アクセス制御](#5-アクセス制御)
6. [メインハンドラ](#6-メインハンドラ)

---

## 1. Python基礎：これだけ覚えよう

コードを読む前に、必要なPython構文を解説します。

### 1-1. 辞書（dictionary）とは？

**辞書 = 「名前」と「値」のペアを保存するもの**

```python
# 辞書を作る
person = {
    'name': '田中',
    'age': 25,
    'email': 'tanaka@example.com'
}

# 値を取り出す
print(person['name'])   # → 田中
print(person['age'])    # → 25

# 値を追加・変更する
person['phone'] = '090-1234-5678'  # 追加
person['age'] = 26                  # 変更
```

!!! tip "イメージ：辞書 = 引き出しに名前ラベルがついた棚"

    | ラベル（キー） | name | age | email |
    |---------------|------|-----|-------|
    | 中身（値） | 田中 | 25 | tanaka@.. |

    `person['name']` → 「nameラベルの引き出しを開けて中身を見る」

**このコードでの使われ方**
```python
# headers という辞書に値を追加していく
headers = {}  # 空の辞書を作る
headers['Content-Type'] = 'text/html'  # 追加
headers['X-Frame-Options'] = 'DENY'    # 追加

# 結果
# headers = {
#     'Content-Type': 'text/html',
#     'X-Frame-Options': 'DENY'
# }
```

---

### 1-2. in 演算子

**in = 「〜の中に含まれる？」を確認する**

```python
# リスト（配列）での使用
fruits = ['りんご', 'みかん', 'ぶどう']

'りんご' in fruits    # → True（含まれる）
'バナナ' in fruits    # → False（含まれない）

# 文字列での使用
email = 'tanaka@example.com'

'@' in email          # → True（@が含まれる）
'@example.com' in email  # → True
'@test.com' in email     # → False
```

**if文での使い方**
```python
allowed_list = ['tanaka@example.com', 'yamada@test.com']
email = 'tanaka@example.com'

if email in allowed_list:
    print('許可されています')
else:
    print('許可されていません')

# → 許可されています
```

---

### 1-3. `or` とは？

**`or` = 「または」（どちらかがTrueならTrue）**

```python
# 条件での使用
age = 20
is_student = True

if age >= 18 or is_student:
    print('OK')  # どちらかがTrueなのでOK

# → OK
```

**値の選択での使用（これが重要！）**
```python
# 「値 or デフォルト値」という書き方
name = None
result = name or '名無し'
print(result)  # → '名無し'

name = '田中'
result = name or '名無し'
print(result)  # → '田中'
```

!!! info "仕組み：A or B の動き"

    1. まず A を確認
    2. A が「ある」（True相当）なら → **A を返す**
    3. A が「ない」（False相当）なら → **B を返す**

    **例：**

    - `origin = None` の場合：`origin or '*'` → `'*'` を返す
    - `origin = 'https://example.com'` の場合：`origin or '*'` → `'https://example.com'` を返す

---

### 1-4. `with open()` とは？

**`with open()` = ファイルを安全に開いて読む方法**

```python
with open('front.html', 'r', encoding='utf-8') as f:
    content = f.read()
```

!!! note "各部分の意味"

    ```
    with open('front.html', 'r', encoding='utf-8') as f:
    ```

    | 部分 | 意味 |
    |------|------|
    | `open` | ファイルを開く関数 |
    | `'front.html'` | ファイル名 |
    | `'r'` | read（読み取り） |
    | `encoding='utf-8'` | 文字コード（日本語対応） |
    | `as f` | 変数名（何でもOK） |

    ```
    content = f.read()
    ```

    - `f.read()` → ファイルの中身を全部読む
    - `content` → 読んだ内容を変数に保存

**なぜ `with` を使う？**
```python
# 悪い例（ファイルを閉じ忘れる可能性）
f = open('file.txt', 'r')
content = f.read()
f.close()  # 閉じ忘れると問題が起きる！

# 良い例（withを使うと自動で閉じてくれる）
with open('file.txt', 'r') as f:
    content = f.read()
# ← ここで自動的にファイルが閉じられる
```

!!! example "イメージ：with = 自動で片付けてくれる仕組み"

    **例：冷蔵庫を開けて食材を取り出す**

    | 方法 | 流れ |
    |------|------|
    | 普通 | 冷蔵庫を開ける → 食材を取る → **閉め忘れる！** |
    | with | 冷蔵庫を開ける → 食材を取る → **自動で閉まる** |

---

### 1-5. Base64エンコード・デコードとは？

- **エンコード** = データを別の形式に変換すること
- **デコード** = 変換されたデータを元に戻すこと

!!! example "日常の例：暗号ごっこ"

    | ステップ | データ |
    |---------|--------|
    | 元のメッセージ | 「こんにちは」 |
    | ↓ エンコード（変換） | |
    | 変換後 | `44GT44KT44Gr44Gh44Gv` ← 読めない！ |
    | ↓ デコード（復元） | |
    | 復元後 | 「こんにちは」 ← 元に戻った！ |

!!! info "なぜBase64を使う？"

    **JWTトークン（ログイン証明書）は3つの部分からできている**

    ```
    eyJhbGci... . eyJlbWFpbCI... . SflKxwRJ...
    ```

    | 部分 | 名前 | 役割 |
    |------|------|------|
    | 1番目 | ヘッダー | 形式情報 |
    | 2番目 | ペイロード | ユーザー情報（**メールアドレスがBase64で入っている**） |
    | 3番目 | 署名 | 改ざん防止 |

**具体例**
```python
import base64
import json

# JWTトークンの例（ペイロード部分）
encoded = "eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSIsIm5hbWUiOiLnlLDkuK0ifQ"

# ステップ1: Base64デコード
decoded_bytes = base64.urlsafe_b64decode(encoded + '==')
# → b'{"email":"tanaka@example.com","name":"\xe7\x94\xb0\xe4\xb8\xad"}'

# ステップ2: 文字列に変換
decoded_str = decoded_bytes.decode('utf-8')
# → '{"email":"tanaka@example.com","name":"田中"}'

# ステップ3: JSONとして解析
data = json.loads(decoded_str)
# → {'email': 'tanaka@example.com', 'name': '田中'}

# ステップ4: メールアドレスを取り出す
email = data.get('email')
# → 'tanaka@example.com'
```

**図解**
```
eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSIsIm5hbWUiOiLnlLDkuK0ifQ
                            ↓
                    Base64デコード
                            ↓
{"email":"tanaka@example.com","name":"田中"}
                            ↓
                    JSONとして解析
                            ↓
                    email を取り出す
                            ↓
                 tanaka@example.com
```

---

## 2. ライブラリ読み込み

```python
import os
import json
import base64
from datetime import datetime
import functions_framework
from openai import OpenAI
```

### 各ライブラリの役割

| ライブラリ | 役割 | 使う場面 |
|-----------|------|---------|
| `os` | 環境変数を読む | APIキーや許可リストの取得 |
| `json` | JSONデータを扱う | トークン解析、レスポンス作成 |
| `base64` | データを変換する | JWTトークンのデコード |
| `datetime` | 日時を扱う | ヘルスチェックの時刻表示 |
| `functions_framework` | Cloud Run対応 | HTTPリクエストを受け取る |
| `openai` | ChatGPT API | AIに質問を送る |

---

## 3. 設定部分

### ALLOWED_ORIGINS

```python
ALLOWED_ORIGINS = ['*']
```

**これは何？**
- どのWebサイトからのアクセスを許可するかのリスト
- `'*'` = どこからでもOK（開発用）

---

### ファイル読み込み

```python
with open('front.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    SCRIPT_CONTENT = f.read()
```

**何をしている？**
1. `front.html` ファイルを開く
2. 中身を全部読み込む
3. `HTML_CONTENT` という変数に保存

**なぜ最初に読み込む？**
- リクエストのたびに読み込むと遅くなる
- 一度読んでメモリに保存しておく

---

## 4. ヘルパー関数

### 4-1. set_cors_headers（CORS設定）

```python
def set_cors_headers(headers, origin):
    if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
        headers['Access-Control-Allow-Origin'] = origin or '*'
    headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    headers['Access-Control-Max-Age'] = '3600'
```

#### 引数の説明

| 引数 | 型 | 説明 |
|------|-----|------|
| `headers` | 辞書 | レスポンスに付けるヘッダー情報 |
| `origin` | 文字列 | リクエスト元のURL（例：`https://example.com`） |

#### 1行ずつ解説

**1行目：条件判定**
```python
if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
```

!!! note "この条件は2つの判定を `or` で繋いでいる"

    | 判定 | 内容 | 結果 |
    |------|------|------|
    | 判定1 | `'*' in ALLOWED_ORIGINS` → ALLOWED_ORIGINS に '*' が含まれるか？ | `['*']` なので True |
    | 判定2 | `origin in ALLOWED_ORIGINS` → リクエスト元URLが許可リストに含まれるか？ | URL次第 |

    `or` で繋いでいるので、**どちらかがTrueなら中の処理を実行**

**2行目：ヘッダーに値を設定**
```python
headers['Access-Control-Allow-Origin'] = origin or '*'
```

!!! note "解説"

    - `headers['キー名'] = 値` → 辞書に値を追加する書き方
    - `origin or '*'` → origin に値があればそれを使う。None や空なら `'*'` を使う

    **例：**

    | origin の値 | 結果 |
    |-------------|------|
    | `'https://example.com'` | `headers['Access-Control-Allow-Origin'] = 'https://example.com'` |
    | `None` | `headers['Access-Control-Allow-Origin'] = '*'` |

**3-5行目：固定ヘッダーの設定**
```python
headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
headers['Access-Control-Max-Age'] = '3600'
```

| ヘッダー | 値 | 意味 |
|---------|-----|------|
| `Access-Control-Allow-Methods` | `'GET, POST, OPTIONS'` | この3つのHTTPメソッドを許可 |
| `Access-Control-Allow-Headers` | `'Content-Type, Authorization'` | この2つのヘッダーを許可 |
| `Access-Control-Max-Age` | `'3600'` | この設定を3600秒（1時間）キャッシュ |

#### CORSとは？（詳細解説）

**CORS = Cross-Origin Resource Sharing（異なるオリジン間のリソース共有）**

!!! success "シナリオ1：普通の使い方（問題なし）"

    **あなたのサイト:** `https://your-app.run.app`

    - `front.html`（画面）
    - `/api/chat`（API）

    **流れ：**
    ユーザー → your-app.run.app にアクセス → front.html の JavaScript が `/api/chat` を呼ぶ → **同じサイトなので問題なし ✓**

!!! danger "シナリオ2：悪意のあるサイトからの攻撃"

    **悪意のあるサイト:** `https://evil.com`

    ページ内のJavaScriptで、あなたの `/api/chat` を勝手に呼ぼうとする：

    ```javascript
    fetch('https://your-app.run.app/api/chat', {
        method: 'POST',
        body: JSON.stringify({ message: '...' })
    });
    ```

    **ブラウザの動き：**

    1. ブラウザ：「待って！evil.com から your-app へのリクエストだ。許可されてる？」
    2. サーバーの `Access-Control-Allow-Origin` を確認
    3. evil.com が許可されていなければ → **ブロック！**

**つまりCORSは：**
- ブラウザが行うセキュリティチェック
- 「このサイトからのリクエストを許可しますか？」をサーバーに確認
- サーバーが「OK」と言わなければブロック

!!! info "HTTPメソッドの役割"

    | メソッド | 用途 | 具体例 |
    |---------|------|--------|
    | **GET** | データを取得する | ページ表示、ユーザー情報取得 |
    | **POST** | データを送信・処理する | チャット送信、ログイン処理 |
    | **OPTIONS** | 事前確認（プリフライト） | 「このリクエスト送っていい？」とブラウザがサーバーに確認 |

    **POSTの動き（イメージ）**

    ```
    [あなた]                    [API（+1する処理）]
       │                              │
       │──── POST { value: 1 } ──────▶│
       │                              │ ← ここで1+1の処理
       │◀───── { result: 2 } ─────────│
    ```

    → データを投げて、API側で処理して、結果が返ってくる

!!! note "OPTIONSリクエストの流れ（プリフライト）"

    ブラウザは「本番のリクエスト」を送る前に、まず「送っていいか？」を確認します。

    ```
    ブラウザ: 「POSTリクエスト送りたいんだけど、いい？」（OPTIONS）
        ↓
    サーバー: 「このオリジンからならOK」または「ダメ」
        ↓
    ブラウザ: OKなら本番のPOSTを送信、ダメならブロック
    ```

    この仕組みにより、許可されていないサイトからの不正なリクエストを防いでいます。

**注意：iframeとは別の話**
- iframe埋め込みは `X-Frame-Options` ヘッダーで制御
- CORSはJavaScriptの `fetch` や `XMLHttpRequest` の制御

---

### 4-2. set_security_headers（セキュリティ設定）

```python
def set_security_headers(headers):
    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Frame-Options'] = 'DENY'
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
```

#### 1行ずつ解説

**1. X-Content-Type-Options**
```python
headers['X-Content-Type-Options'] = 'nosniff'
```

!!! warning "攻撃の例"

    攻撃者：「image.jpg」という名前で悪意のあるJavaScriptをアップロード

    ブラウザ：「image.jpg って書いてあるけど、中身を見たらJavaScriptっぽいな。実行しちゃおう！」→ **攻撃成功！**

!!! success "nosniffの効果"

    ブラウザ：「nosniffが設定されてる。Content-Type通りに解釈しよう。画像として扱うから実行しない」→ **攻撃失敗！**

**2. X-Frame-Options**
```python
headers['X-Frame-Options'] = 'DENY'
```

!!! warning "攻撃の例：クリックジャッキング"

    **攻撃者のサイト evil.com の手口：**

    1. 「無料プレゼント！ここをクリック！」というボタンを表示
    2. その下に、あなたのサイトをiframeで**透明**に重ねて表示
    3. 「プレゼント」ボタンの位置に、あなたのサイトの「削除」ボタンを配置

    **結果：** ユーザーは「プレゼント！」をクリックしたつもりが、実際は「削除」ボタンをクリックしていた

!!! success "DENYの効果"

    あなたのサイトをiframeに埋め込むことを**禁止** → この攻撃が不可能になる

**3. X-XSS-Protection**
```python
headers['X-XSS-Protection'] = '1; mode=block'
```

!!! warning "攻撃の例：XSS（クロスサイトスクリプティング）"

    攻撃者がURLに悪意のあるスクリプトを仕込む：

    `https://your-app.com/search?q=<script>悪意のあるコード</script>`

!!! success "1; mode=blockの効果"

    ブラウザ：「XSS攻撃を検知！ページの表示をブロック」

    ※ 現代のブラウザは独自のXSS対策があるため、このヘッダーは補助的な役割

**4. Referrer-Policy**
```python
headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
```

!!! info "Referrer（リファラー）とは"

    「どのページから来たか」の情報

    **例：** Aページのリンクをクリック → Bページへ移動 → BページはリファラーとしてAページのURLを受け取る

!!! warning "問題"

    リファラーにはURLの全体が含まれることがある

    例：`https://your-app.com/user/12345/secret-token`

    → URLにトークンやIDが含まれていたら**情報漏洩！**

!!! success "strict-origin-when-cross-originの効果"

    | 送信先 | 送信内容 |
    |--------|----------|
    | 同じサイト内 | 完全なURL送信 |
    | 別サイト宛て | ドメインのみ送信（`https://your-app.com` のみ） |

---

## 5. アクセス制御

### 5-1. is_email_allowed（メール許可チェック）

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

#### 1行ずつ解説

**1-3行目：空チェック**
```python
def is_email_allowed(email):
    if not email:
        return False
    lower_email = email.lower()
```

```
email = None or ''（空）の場合
  → if not email: が True
  → return False で終了

email = 'Tanaka@Example.com' の場合
  → lower_email = 'tanaka@example.com' に変換
    （大文字小文字を統一して比較しやすくする）
```

**4-5行目：許可メールリストの取得**
```python
allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
allowed_emails = [e.strip().lower() for e in allowed_emails_str.split(',') if e.strip()]
```

**詳細な分解**
```python
# 環境変数の例
# ALLOWED_EMAILS = "tanaka@example.com, yamada@test.com, admin@company.co.jp"

# ステップ1: 環境変数を取得
allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
# → "tanaka@example.com, yamada@test.com, admin@company.co.jp"
# （もし環境変数がなければ空文字 '' になる）

# ステップ2: カンマで分割
parts = allowed_emails_str.split(',')
# → ["tanaka@example.com", " yamada@test.com", " admin@company.co.jp"]
#    ※ 空白が残っている

# ステップ3: 各要素を処理
allowed_emails = []
for e in parts:
    cleaned = e.strip()       # 前後の空白を除去
    if cleaned:               # 空でなければ
        allowed_emails.append(cleaned.lower())  # 小文字にして追加

# 結果
# → ["tanaka@example.com", "yamada@test.com", "admin@company.co.jp"]
```

**リスト内包表記の読み方**
```python
[e.strip().lower() for e in allowed_emails_str.split(',') if e.strip()]
 └──────────────┘     └─────────────────────────────┘    └─────────┘
    「何をする」         「何から繰り返す」              「条件」
```

**8-11行目：許可チェック**
```python
if lower_email in allowed_emails:
    return True
for domain in allowed_domains:
    if lower_email.endswith(domain):
        return True
```

```
チェック1: メールアドレスが許可リストに完全一致するか
  例: tanaka@example.com in ["tanaka@example.com", "yamada@test.com"]
  → True

チェック2: メールアドレスが許可ドメインで終わるか
  例: "tanaka@company.co.jp".endswith("@company.co.jp")
  → True（会社のドメイン全員を許可する場合に使う）
```

---

### 5-2. get_email_from_token（トークンからメール取得）

```python
def get_email_from_token(id_token):
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

#### 完全な処理の流れ

```python
# 入力されるJWTトークンの例
id_token = "eyJhbGciOiJSUzI1NiJ9.eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9.abc123"

# ステップ1: ピリオドで分割
parts = id_token.split('.')
# → ["eyJhbGciOiJSUzI1NiJ9", "eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9", "abc123"]
#         ヘッダー                      ペイロード                      署名

# ステップ2: ペイロード（2番目）を取得
payload = parts[1]
# → "eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9"

# ステップ3: パディング調整（Base64の仕様に合わせる）
# Base64は4文字ずつ処理するので、4の倍数にする必要がある
padding = 4 - len(payload) % 4  # 何文字足りないか
if padding != 4:
    payload += '=' * padding  # '='で埋める

# ステップ4: Base64デコード
decoded_bytes = base64.urlsafe_b64decode(payload)
# → b'{"email":"tanaka@example.com"}'

# ステップ5: バイト列を文字列に変換
decoded_str = decoded_bytes.decode('utf-8')
# → '{"email":"tanaka@example.com"}'

# ステップ6: JSON文字列を辞書に変換
data = json.loads(decoded_str)
# → {"email": "tanaka@example.com"}

# ステップ7: emailを取得
email = data.get('email')
# → "tanaka@example.com"
```

**図解**
```
JWTトークン
eyJhbGci...  .  eyJlbWFpbCI...  .  SflKxwRJ...
     |               |               |
  ヘッダー       ペイロード        署名
                     ↓
            split('.')[1]で取得
                     ↓
        eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9
                     ↓
            Base64デコード
                     ↓
        {"email":"tanaka@example.com"}
                     ↓
            json.loads()で辞書に
                     ↓
            .get('email')で取得
                     ↓
            tanaka@example.com
```

---

## 6. メインハンドラ

### 6-1. エントリポイントの定義

```python
@functions_framework.http
def app(request):
```

!!! note "@ とは？（デコレータ）"

    ```python
    @functions_framework.http
    def app(request):
    ```

    「app という関数を、HTTPリクエストを受け取る関数としてCloud Run に登録する」という意味

    **@（アットマーク）= 関数に目印をつける仕組み**

    | 役割 | 説明 |
    |------|------|
    | Cloud Run | 「受付係募集中」 |
    | `def app(request):` | 「はい！私が受付係です！」 |
    | `@functions_framework.http` | 「この人を受付係として登録してください」 |

### 6-2. requestオブジェクト

```python
def app(request):
    # request = ブラウザから届いた情報全部
```

| プロパティ | 説明 | 例 |
|-----------|------|-----|
| `request.method` | HTTPメソッド | `'GET'`, `'POST'` |
| `request.path` | URLのパス | `'/'`, `'/api/chat'` |
| `request.headers` | ヘッダー情報 | `{'Authorization': 'Bearer xxx'}` |
| `request.get_json()` | ボディ（JSON） | `{'message': 'こんにちは'}` |

### 6-3. 戻り値

```python
return (HTML_CONTENT, 200, headers)
#         ↑          ↑      ↑
#       本文     ステータス  ヘッダー
```

| ステータスコード | 意味 |
|-----------------|------|
| `200` | 成功 |
| `400` | リクエストが不正（入力エラー） |
| `401` | 認証が必要（ログインしていない） |
| `403` | 権限なし（ログイン済みだが許可されていない） |
| `404` | ページが見つからない |
| `500` | サーバーエラー |

---

## まとめ

このドキュメントで学んだPython構文：

| 構文 | 意味 | 例 |
|------|------|-----|
| `dict['key'] = value` | 辞書に値を追加 | `headers['Content-Type'] = 'text/html'` |
| `x in list` | リストに含まれるか | `'*' in ALLOWED_ORIGINS` |
| `a or b` | aがあればa、なければb | `origin or '*'` |
| `with open() as f:` | ファイルを安全に開く | ファイル読み込み |
| `base64.decode()` | Base64をデコード | トークン解析 |
| `@decorator` | 関数に目印をつける | `@functions_framework.http` |
| `[x for x in list]` | リスト内包表記 | メールリストの処理 |
