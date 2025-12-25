# backend.py 詳細解説

このファイルはサーバー側の処理を担当します。「厨房のシェフ」のような役割です。

**このドキュメントでは、Pythonの基礎構文から丁寧に解説します。**

---

## 目次 { data-toc-skip }

1. [Python基礎：これだけ覚えよう](#1-python基礎これだけ覚えよう)
2. [ライブラリ読み込み](#2-ライブラリ読み込み)
3. [セキュリティの全体像](#3-セキュリティの全体像なぜ安全)
4. [設定部分](#4-設定部分)
5. [ヘルパー関数](#5-ヘルパー関数)
6. [アクセス制御](#6-アクセス制御)
7. [メインハンドラ](#7-メインハンドラ)

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

### 1-2. if文（条件分岐）

**if文 = 条件によって処理を分ける**

```python
age = 20

if age >= 18:
    print('成人です')
else:
    print('未成年です')

# → 成人です
```

!!! note "if文の構造"

    ```python
    if 条件:
        条件がTrueのときの処理
    else:
        条件がFalseのときの処理
    ```

    **インデント（字下げ）が重要！**
    Pythonでは、インデントでブロック（処理のまとまり）を表します。

**複数の条件（elif）**
```python
score = 75

if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 50:
    print('C')
else:
    print('D')

# → B
```

**このコードでの使われ方**
```python
# メールが許可リストにあるかチェック
if email in allowed_list:
    return True   # 許可
else:
    return False  # 拒否
```

!!! tip "よく使う条件"

    | 条件 | 意味 | 例 |
    |------|------|-----|
    | `==` | 等しい | `status == 200` |
    | `!=` | 等しくない | `error != None` |
    | `in` | 含まれる | `'@' in email` |
    | `not` | 否定 | `if not email:` （emailが空なら） |

---

### 1-3. in 演算子

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

### 1-4. `or` とは？

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

### 1-5. def（関数定義）

**def = 処理をまとめて名前をつける**

```python
def greet(name):
    return f'こんにちは、{name}さん'

# 使う
message = greet('田中')
print(message)  # → こんにちは、田中さん
```

!!! note "関数の構造"

    ```python
    def 関数名(引数):
        処理
        return 戻り値
    ```

    | 部分 | 意味 |
    |------|------|
    | `def` | 「関数を定義する」という宣言 |
    | `greet` | 関数の名前（自由につける） |
    | `(name)` | 引数（関数に渡す値） |
    | `return` | 結果を返す |

**引数がない関数**
```python
def say_hello():
    return 'Hello!'

print(say_hello())  # → Hello!
```

**複数の引数**
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # → 8
```

**このコードでの使われ方**
```python
# ヘッダーを設定する関数
def set_cors_headers(headers, origin):
    headers['Access-Control-Allow-Origin'] = origin
    # ... 他の設定
```

!!! info "なぜ関数を使う？"

    | メリット | 説明 |
    |---------|------|
    | 再利用 | 同じ処理を何度も書かなくてよい |
    | 整理 | コードが読みやすくなる |
    | 保守 | 修正が1箇所で済む |

---

### 1-6. for ループ（繰り返し処理）

**for ループ = リストの中身を1つずつ取り出して処理する**

```python
fruits = ['りんご', 'みかん', 'ぶどう']

for fruit in fruits:
    print(fruit)
```

**実行結果：**
```
りんご
みかん
ぶどう
```

!!! note "for ループの読み方"

    ```python
    for fruit in fruits:
        print(fruit)
    ```

    **日本語で読むと：**
    「fruits の中から 1つずつ fruit として取り出して、print(fruit) を実行する」

    | 回数 | fruit の値 | 実行される処理 |
    |:----:|-----------|---------------|
    | 1回目 | `'りんご'` | `print('りんご')` |
    | 2回目 | `'みかん'` | `print('みかん')` |
    | 3回目 | `'ぶどう'` | `print('ぶどう')` |

**このコードでの使われ方**
```python
# 許可ドメインをチェックする
allowed_domains = ['@example.com', '@company.co.jp']
email = 'tanaka@company.co.jp'

for domain in allowed_domains:
    if email.endswith(domain):
        print('許可されたドメインです')
```

!!! info "よく使うメソッド"

    | メソッド | 役割 | 例 |
    |---------|------|-----|
    | `strip()` | 前後の空白を除去 | `" hello "` → `"hello"` |
    | `lower()` | 小文字に変換 | `"TaNaKa"` → `"tanaka"` |
    | `split(',')` | カンマで分割してリストに | `"a,b,c"` → `['a','b','c']` |
    | `endswith()` | 指定文字列で終わるか | `"test@a.com".endswith("@a.com")` → `True` |

---

### 1-7. リスト内包表記（省略形）

for ループを**1行で書ける**省略記法です。

```python
numbers = [1, 2, 3, 4, 5]

# 普通の書き方（4行）
doubled = []
for n in numbers:
    doubled.append(n * 2)
# → [2, 4, 6, 8, 10]

# リスト内包表記（1行）
doubled = [n * 2 for n in numbers]
# → [2, 4, 6, 8, 10]
```

**同じ結果**になります。

!!! tip "リスト内包表記の読み方"

    ```python
    [n * 2 for n in numbers]
    ```

    **読む順番は「右から左」：**

    | 順番 | 部分 | 意味 |
    |:----:|------|------|
    | ① | `for n in numbers` | numbers から1つずつ n として取り出す |
    | ② | `n * 2` | それを2倍にしてリストに追加 |

    ```text
    [  ②何をする    for  ①何から取り出す  ]
    ```

**条件付きの場合（if を追加）**
```python
numbers = [1, 2, 3, 4, 5]

# 偶数だけを2倍にする
doubled_even = [n * 2 for n in numbers if n % 2 == 0]
# → [4, 8]  （2と4だけが偶数）
```

!!! note "条件付きの読み方"

    ```python
    [n * 2 for n in numbers if n % 2 == 0]
    ```

    | 順番 | 部分 | 意味 |
    |:----:|------|------|
    | ① | `for n in numbers` | numbers から1つずつ取り出す |
    | ② | `if n % 2 == 0` | 偶数なら |
    | ③ | `n * 2` | 2倍にしてリストに追加 |

    **読む順番は ①→②→③ です！**

    ```text
    [  ③何をする    for  ①何から取り出す  if  ②条件  ]
    ```

**このコードでの使われ方**
```python
# メールリストを整形する
emails_str = "tanaka@example.com, YAMADA@test.com,  admin@company.co.jp"

# 分割 → 空白除去 → 小文字化 を1行で
emails = [e.strip().lower() for e in emails_str.split(',') if e.strip()]
# → ['tanaka@example.com', 'yamada@test.com', 'admin@company.co.jp']
```

---

### 1-8. try / except（エラー処理）

**try / except = エラーが起きても止まらないようにする**

```python
try:
    result = 10 / 0  # ← ゼロで割るとエラー！
except:
    result = 0       # ← エラーが起きたらこっちを実行
    print('エラーが発生しました')

# → エラーが発生しました
# → result = 0
```

!!! note "try / exceptの構造"

    ```python
    try:
        エラーが起きるかもしれない処理
    except:
        エラーが起きたときの処理
    ```

    | 部分 | 意味 |
    |------|------|
    | `try` | 「試す」ブロック |
    | `except` | 「例外（エラー）が起きたら」ブロック |

**なぜ必要？**

tryがないと、エラーでプログラム全体が止まってしまいます。

```python
# tryなし → プログラムが止まる
result = 10 / 0  # ← ここでエラー！以降の処理が実行されない

# tryあり → エラーを処理して続行
try:
    result = 10 / 0
except:
    result = 0
print('処理を続行')  # ← これが実行される
```

!!! example "イメージ：転んでも立ち上がる"

    | 状況 | tryなし | tryあり |
    |------|---------|---------|
    | 石につまずく | 転んで動けなくなる | 転んでも立ち上がって歩き続ける |

**このコードでの使われ方**
```python
def get_email_from_token(id_token):
    try:
        # トークンからメールを取り出す処理
        payload = id_token.split('.')[1]
        # ... デコード処理 ...
        return json.loads(decoded).get('email')
    except:
        # 何かエラーが起きたら None を返す
        return None
```

!!! tip "なぜ get_email_from_token で try を使う？"

    トークンが壊れている・形式が違う・空っぽなど、様々な理由でエラーが起きる可能性があります。

    | 起きうるエラー | 原因 |
    |---------------|------|
    | `IndexError` | トークンに `.` がない（分割できない） |
    | `UnicodeDecodeError` | Base64デコードに失敗 |
    | `JSONDecodeError` | JSON形式じゃない |

    **全部個別に対処するのは大変** → `try/except` でまとめて処理

    エラーが起きたら `None` を返し、呼び出し元で「メールが取れなかった」として処理します。

---

### 1-9. `with open()` とは？

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

### 1-10. Base64エンコード・デコードとは？

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

## 3. セキュリティの全体像（なぜ安全？）

コードの詳細に入る前に、**このシステムがどう守られているか**を理解しましょう。

### まず知っておくこと：HTTP通信の基本

#### リクエストとレスポンス

ブラウザとサーバーは「手紙のやりとり」のように通信します。

```text
【リクエスト（お願い）】
ブラウザ  ------>  サーバー
         「/api/chat のデータをください」

【レスポンス（返事）】
ブラウザ  <------  サーバー
         「はい、どうぞ」
```

#### レスポンスには「2つの部分」がある

サーバーがブラウザに返す「返事」は、以下の構造になっています：

```text
+------------------------------------------+
| ヘッダー（ブラウザへの指示書）              |
|                                          |
|   Content-Type: application/json         |
|   X-Frame-Options: DENY                  |
|   Access-Control-Allow-Origin: ...       |
+------------------------------------------+
| ボディ（実際のデータ）                     |
|                                          |
|   {"message": "こんにちは"}               |
+------------------------------------------+
```

| 部分 | 役割 | 例 |
|------|------|-----|
| **ヘッダー** | ブラウザへの「指示書」 | `X-Frame-Options: DENY` |
| **ボディ** | 実際のデータ | `{"message": "こんにちは"}` |

**ヘッダー = 「この返事をこう扱ってね」というブラウザへの命令**

#### ブラウザはヘッダーに従う（仕様で決まっている）

```text
サーバー: 「X-Frame-Options: DENY」（iframeに入れないで）
   |
   v
ブラウザ: 「了解、このページはiframeに入れません」
```

これは**ブラウザの仕様（ルール）**です。
Chrome、Firefox、Edge など、すべての主要ブラウザがこのルールに従います。

---

### CORSとは？（ヘッダーで制御する仕組み）

**CORS**は、このヘッダーを使って「**どのサイトにデータを渡すか**」を制御する仕組みです。

#### CORSの動き

```text
evil.com (JavaScript)
   |
   |  your-app のデータをください
   v
サーバー (your-app.run.app)
   |
   |  API処理中...（ここで課金発生！）
   |
   |  レスポンス + ヘッダー:
   |  「your-app.run.app だけがデータを受け取れます」
   v
ブラウザ
   |
   |  evil.com はヘッダーに書いてない...
   v
ブロック！（データはJavaScriptに渡さない）
```

ヘッダーに記載がないので**データは渡さない**！
そんな機能を持つのが、**CORS**です。

!!! danger "重要：CORSだけでは課金は防げない"

    上の図をよく見てください。

    - サーバーは**処理を実行**している
    - レスポンスも**返している**

    つまり**APIは使われている = 課金は発生する**！

    CORSが防ぐのは「結果をJavaScriptに渡すこと」だけ。
    **処理自体は止められません。**

| 疑問 | 答え |
|------|------|
| CORSは何をする？ | 許可されてないサイトにはデータを渡さない |
| 誰が判断する？ | ブラウザ（ヘッダーを見て判断） |
| 課金は防げる？ | **防げない**（処理は走る） |
| じゃあ何のため？ | データの**盗み見**を防ぐ |

!!! warning "ヘッダーの限界"

    ヘッダーで守れるのは**ブラウザからのアクセス**だけです。

    **ブラウザ以外のアクセス方法：**

    - **curl** = コマンドラインからHTTPリクエストを送るツール
    - **Postman** = APIテスト用のアプリ

    これらは**ブラウザではない**ので、CORSヘッダーを**無視できます**。

    ```text
    【ブラウザの場合】
    evil.com → リクエスト → サーバー → レスポンス
                                    → ヘッダー「evil.comはダメ」
                                    → ブラウザ「従います」→ ブロック ✓

    【curl/Postmanの場合】
    curl → リクエスト → サーバー → レスポンス
                              → ヘッダー「evil.comはダメ」
                              → curl「知らんがな」→ データ取得 ✗
    ```

    | アクセス元 | 何？ | ヘッダーに従う？ | 防御できる？ |
    |-----------|------|:---------------:|:-----------:|
    | ブラウザ | Chrome、Firefox等 | 従う（仕様） | ✓ |
    | curl | コマンドラインツール | 無視できる | ✗ |
    | Postman | APIテストアプリ | 無視できる | ✗ |

    **つまり：**
    悪意のある人がcurlやPostmanを使えば、CORSを無視してAPIを叩けてしまいます。
    だから**JWT検証や許可リスト**で、ブラウザ以外からのアクセスも防いでいます。

---

### 多層防御の仕組み

CORSだけでは課金を防げないため、一般的に**複数の防御層**で守ります。

以下は**実際の処理順序**に沿った図です：

```text
リクエスト到着
         |
         v
+-------------------------------------------+
| 1. JWT検証（サーバー側）                    |
| ログインしている？                          |
| → いいえ：エラーを返す（ここで終了）         |
+-------------------------------------------+
         | はい
         v
+-------------------------------------------+
| 2. 許可リストチェック（サーバー側）          |
| 許可されたユーザー？                        |
| → いいえ：エラーを返す（ここで終了）         |
+-------------------------------------------+
         | はい
         v
+-------------------------------------------+
| 3. OpenAI API呼び出し（ここで課金発生！）    |
+-------------------------------------------+
         |
         v
+-------------------------------------------+
| 4. レスポンスを返す（CORSヘッダー付き）      |
+-------------------------------------------+
         |
         v
+-------------------------------------------+
| 5. ブラウザがCORSをチェック（最後！）        |
| 許可されたサイト？                          |
| → いいえ：データをJavaScriptに渡さない      |
+-------------------------------------------+
```

!!! warning "CORSは最後にチェックされる"

    図を見てください。CORSチェックは**ブラウザがレスポンスを受け取った後**です。

    つまり：

    - サーバー処理（1〜4）は**すでに完了している**
    - 課金も**すでに発生している**
    - CORSが防ぐのは「データをJavaScriptに渡すこと」だけ

    **だからJWT検証と許可リストが重要！**
    課金前に不正アクセスを止められるのはこの2つだけです。

### 各防御が突破されると何が起きる？

| 処理順 | 名前 | 何を守る？ | 突破されると？ |
|:------:|------|-----------|---------------|
| 1 | JWT検証 | 未ログインユーザー | 勝手にAPIを使われ**課金される可能性有** |
| 2 | 許可リスト | 部外者のアクセス | 勝手にAPIを使われ**課金される可能性有** |
| 5 | CORS | 不正サイトからのデータ取得 | データが盗まれる可能性（課金は防げない） |

!!! example "具体例：もし防御が足りなかったら？"

    **CORSのみの場合：**
    ```
    誰でも → ログインなしでAPIを叩ける → 無制限に課金発生！
    ```
    ※ ただしCORSヘッダーは機能するため、ブラウザ経由の場合は
    　 不正サイトへのデータ表示はブロックされる

    **CORS + JWT検証のみの場合（許可リストなし）：**
    ```
    誰でも → Googleアカウント作成 → ログイン成功 → APIを使える！
    ```
    → Googleアカウントは誰でも作れるので、世界中の誰でもアクセス可能
    ※ ただしCORSヘッダーは機能するため、ブラウザ経由の場合は
    　 不正サイトへのデータ表示はブロックされる

    **CORS + JWT検証 + 許可リストの場合（現在の構成）：**
    ```
    誰か → Googleアカウントでログイン → 許可リストにいる？
                                    → いいえ → アクセス拒否
                                    → はい → API利用可能
    ```
    → 特定のメールアドレス/ドメインの人だけがアクセス可能

!!! info "JWT検証と許可リストの違い"

    この2つは**別の目的**を持っています。

    | 防御 | 確認すること | 例 |
    |------|-------------|-----|
    | JWT検証 | ログインしているか？ | Googleアカウントで認証済みか |
    | 許可リスト | **誰が**ログインしているか？ | `@yourcompany.co.jp` のドメインか |

    **なぜ両方必要？**

    - JWTだけ：誰でもGoogleアカウントを作れる → 世界中の誰でもアクセス可能
    - 許可リストを追加：特定のメールアドレス/ドメインに限定 → 会社の人だけ等

### なぜ3層すべて必要？

```text
【CORSだけの場合】

evil.com → リクエスト → サーバー処理 → OpenAI呼ぶ → 課金！
                                              ↓
                              レスポンス返す → ブラウザがブロック
                                              ↑
                                   「見せない」だけで処理は走る

【JWT + 許可リストがある場合】

evil.com → リクエスト → JWT検証 → ダメ！→ エラー返す
                          ↑
                   ここで止まる（課金されない）
```

CORSは「ブラウザが結果を見せない」だけ。
**サーバー側の処理（課金）は止められません。**

だから**JWT検証と許可リスト**で、
**高価な処理（AI呼び出し）の前に拒否**しています。

!!! tip "この後のコードを読むポイント"

    | セクション | 対応する防御 | 実行順 |
    |-----------|-------------|:------:|
    | 6-2. get_email_from_token | JWT検証 | 1 |
    | 6-1. is_email_allowed | 許可リストチェック | 2 |
    | 5-1. set_cors_headers | CORSヘッダー設定 | 3 |

    ※ CORSはレスポンスにヘッダーを付けるだけ。
    実際のCORSチェックはブラウザが最後に行います。

---

## 4. 設定部分

### ALLOWED_ORIGINS（CORS用の許可オリジンリスト）

```python
ALLOWED_ORIGINS = ['*']
```

**これは何？**

この変数は**CORS設定**に使用されます。
具体的には、後述の [5-1. set_cors_headers](#5-1-set_cors_headerscors設定) 関数で参照されます。

```python
# 5-1. set_cors_headers 内での使用例
if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
    headers['Access-Control-Allow-Origin'] = origin or '*'
```

| 設定値 | 意味 | 用途 |
|--------|------|------|
| `['*']` | どこからでもOK | 開発用（本番では危険） |
| `['https://your-app.run.app']` | 特定のオリジンのみ許可 | 本番用 |

!!! warning "「許可リスト」との違いに注意"

    | 変数名 | 用途 | 何を制限？ |
    |--------|------|-----------|
    | **ALLOWED_ORIGINS** | CORS設定 | どの**サイト**からのアクセスを許可するか |
    | ALLOWED_EMAILS | ユーザー認証 | どの**メールアドレス**のユーザーを許可するか |
    | ALLOWED_DOMAINS | ユーザー認証 | どの**ドメイン**のユーザーを許可するか |

    名前が似ていますが、**別の目的**を持っています。

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

## 5. ヘルパー関数

### 5-1. set_cors_headers（CORS設定）

この関数は、レスポンスにCORSヘッダーを追加します。

!!! info "CORSとは？"

    CORSの概念（なぜ必要か、何を守るか）については [3. セキュリティの全体像](#3-セキュリティの全体像なぜ安全) で詳しく解説しています。

    ここでは**コードの読み方**と**実際の設定方法**を解説します。

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

#### オリジン（Origin）とは？

オリジンは「**プロトコル + ドメイン + ポート**」の組み合わせです。

```
https://your-app.run.app:443
└─┬──┘ └───────┬───────┘└┬─┘
プロトコル   ドメイン    ポート
```

**同じオリジン vs 別オリジン**

| URL | `https://your-app.run.app` と比較 | 理由 |
|-----|----------------------------------|------|
| `https://your-app.run.app/api/chat` | 同じ | パスが違うだけ |
| `http://your-app.run.app` | **別** | プロトコルが違う |
| `https://evil.com` | **別** | ドメインが違う |
| `https://your-app.run.app:8080` | **別** | ポートが違う |

!!! info "httpsとhttpの違い（ハガキ vs 封筒）"

    | 方式 | 例え | 中身 |
    |------|------|------|
    | **http** | ハガキ | 配達員にも中身が丸見え |
    | **https** | 封筒（鍵付き） | 受取人だけが開封できる |

    本番環境では必ず **https** を使いましょう（Cloud Runは自動でhttpsになります）。

#### HTTPメソッドの役割

| メソッド | 用途 | 具体例 |
|---------|------|--------|
| **GET** | データを取得する | ページ表示、ユーザー情報取得 |
| **POST** | データを送信・処理する | チャット送信、ログイン処理 |
| **OPTIONS** | 事前確認（プリフライト） | 「このリクエスト送っていい？」とブラウザがサーバーに確認 |

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

#### 実際の設定方法

!!! tip "このシステムは同じオリジン"

    今回はCloud Runで**フロントエンド（front.html）もバックエンド（API）も同じサービス**で動かしています。

    ```
    https://your-app.run.app/          ← front.html（画面）
    https://your-app.run.app/api/chat  ← API
    ```

    **同じオリジン**なので、実はCORSの問題は発生しません。

    ただし、本番環境では念のため `ALLOWED_ORIGINS` を設定しておくと安全です：

    ```python
    # 開発用（現在）
    ALLOWED_ORIGINS = ['*']

    # 本番用（推奨）
    ALLOWED_ORIGINS = ['https://your-app-xxxxx-an.a.run.app']
    ```

    ※ `your-app-xxxxx-an.a.run.app` は実際のCloud Run URLに置き換えてください。

!!! question "オリジンの書き方"

    オリジンは「**プロトコル + ドメイン + ポート**」です。パス（`/api/chat` など）は含めません。

    ```
    https://your-app.run.app/page/chat?user=123
    └──────────┬──────────────┘└───────┬────────┘
          オリジン（これを登録）    パス（含めない）
    ```

    | 登録例 | 正誤 | 理由 |
    |--------|:----:|------|
    | `https://your-app.run.app` | ✓ | 正しい形式 |
    | `https://your-app.run.app/api/chat` | ✗ | パスは不要 |
    | `your-app.run.app` | ✗ | プロトコルが必要 |

!!! example "複数オリジンを登録する場合"

    開発環境・ステージング環境・本番環境など、複数のオリジンからアクセスが必要な場合は、配列に追加します。

    ```python
    ALLOWED_ORIGINS = [
        'https://your-app.run.app',           # 本番
        'https://staging.your-app.run.app',   # ステージング
        'http://localhost:3000',               # 開発（ローカル）
        'http://localhost:5173'                # Viteなど別ポート
    ]
    ```

    開発中は `['*']` で全許可にしておいて、本番では具体的なオリジンを指定する、というのがよくあるパターンです。

!!! warning "`['*']`（全許可）のままだと何が起きる？"

    ```python
    # デフォルト設定（危険！）
    ALLOWED_ORIGINS = ['*']  # ← どこからでもOK
    ```

    この状態だと、**悪意のあるサイトからAPIを勝手に使われる可能性があります**。

    | 被害 | 具体例 |
    |------|--------|
    | **課金が発生** | 勝手にチャットAPIを叩かれ、OpenAI APIの料金があなたに請求される |
    | **サービス停止** | 大量リクエストでサーバーがダウンする |
    | **信用低下** | 不正利用の踏み台にされる可能性 |

    **→ 本番では必ず許可するオリジンを限定しましょう！**

---

### 5-2. 高度なセキュリティ設定

5-1では**CORSヘッダー**（どのサイトからのアクセスを許可するか）を設定しました。

この関数では、それに加えて**追加のセキュリティヘッダー**を設定します。
これらは、より高度な攻撃（クリックジャッキング、XSS、ファイル偽装など）を防ぐためのものです。

```python
def set_security_headers(headers):
    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Frame-Options'] = 'DENY'
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
```

#### 各ヘッダーの役割

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

## 6. アクセス制御

### 6-1. is_email_allowed（メール許可チェック）

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

この2行目は「リスト内包表記」です。

!!! info "基礎知識"

    forループとリスト内包表記の基本は [1-6. forループ](#1-6-for-ループ繰り返し処理) と [1-7. リスト内包表記](#1-7-リスト内包表記省略形) で解説しています。

**この行が何をしているか：**

```text
環境変数: "tanaka@example.com, YAMADA@test.com,  admin@company.co.jp"
                ↓ split(',') でカンマ分割
         ["tanaka@example.com", " YAMADA@test.com", "  admin@company.co.jp"]
                ↓ strip() で空白除去
         ["tanaka@example.com", "YAMADA@test.com", "admin@company.co.jp"]
                ↓ lower() で小文字化
         ["tanaka@example.com", "yamada@test.com", "admin@company.co.jp"]
```

!!! tip "なぜ lower() が必要？"

    メールアドレスの比較で `Tanaka@Example.com` と `tanaka@example.com` を同じとして扱うため。

---

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

### 6-2. get_email_from_token（トークンからメール取得）

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

## 7. メインハンドラ

### 7-1. エントリポイントの定義

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

### 7-2. requestオブジェクト

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

### 7-3. 戻り値

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
| `try: ... except:` | エラーを処理して続行 | トークン解析のエラー処理 |
| `with open() as f:` | ファイルを安全に開く | ファイル読み込み |
| `base64.decode()` | Base64をデコード | トークン解析 |
| `@decorator` | 関数に目印をつける | `@functions_framework.http` |
| `[x for x in list]` | リスト内包表記 | メールリストの処理 |
