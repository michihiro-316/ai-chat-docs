# エントリポイント（app）の仕組み

「なぜ `app` を指定したらアプリが見れるようになるのか？」を詳しく解説します。

---

## エントリポイントとは？

**エントリポイント = プログラムの入口**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  例: 会社のビル                                              │
│                                                             │
│  正面玄関（入口）                                            │
│       ↓                                                     │
│  受付（案内係）                                              │
│       ↓                                                     │
│  各部署へ案内                                               │
│                                                             │
│  エントリポイント = 正面玄関の場所を教えること               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

プログラムでも同じです。

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ユーザーがアクセス                                          │
│       ↓                                                     │
│  Cloud Run: 「どの関数を実行すればいい？」                   │
│       ↓                                                     │
│  GCP設定: 「エントリポイントは 'app' だよ」                  │
│       ↓                                                     │
│  Cloud Run: 「了解！app 関数を実行！」                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Python版の場合

### コードでの定義

```python
@functions_framework.http
def app(request):
    # 処理...
```

**ポイント**
1. `@functions_framework.http` = 「HTTPリクエストを受け取る関数です」という目印
2. `def app(request)` = 関数名は `app`
3. GCPの設定で「エントリポイント = `app`」と指定

### 設定との対応

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  【GCPコンソールでの設定】                                   │
│  エントリポイント: [  app  ]                                │
│                       ↑                                     │
│                       │                                     │
│  【コード（backend.py）】                                    │
│                       │                                     │
│  @functions_framework.http                                  │
│  def app(request):    ← この名前と一致させる                │
│      ...                                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## JavaScript（Node.js）版の場合

### コードでの定義

```javascript
const functions = require('@google-cloud/functions-framework');

functions.http('app', async (req, res) => {
    // 処理...
});
```

**ポイント**
1. `functions.http('app', ...)` = 「`app` という名前でHTTPリクエストを受け取ります」
2. GCPの設定で「エントリポイント = `app`」と指定

### 設定との対応

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  【GCPコンソールでの設定】                                   │
│  エントリポイント: [  app  ]                                │
│                       ↑                                     │
│                       │                                     │
│  【コード（backend.js）】                                    │
│                       │                                     │
│  functions.http('app', async (req, res) => {               │
│  //             ↑                                          │
│  //          この名前と一致させる                           │
│      ...                                                    │
│  });                                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## よくあるエラー

### エラー1: 名前が一致していない

```
Error: Function 'helloWorld' is not defined
```

**原因**
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  GCPの設定: エントリポイント = helloWorld                    │
│                    ↓                                        │
│  Cloud Run: 「helloWorld を探すぞ」                         │
│                    ↓                                        │
│  コード:                                                    │
│    functions.http('app', ...)  ← app はあるけど...         │
│                    ↓                                        │
│  Cloud Run: 「helloWorld が見つからない！エラー！」         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**解決方法**
- GCPの設定を `app` に変更する
- または、コードを `functions.http('helloWorld', ...)` に変更する

---

### エラー2: デコレータがない（Python）

```
Error: Could not load function
```

**原因**
```python
# 間違い
def app(request):  # @functions_framework.http がない
    ...

# 正しい
@functions_framework.http  # これが必要
def app(request):
    ...
```

---

## 処理の流れ（全体像）

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  1. ユーザーがブラウザでURLにアクセス                        │
│     https://ai-chat-app-xxxxx.run.app/                      │
│                                                             │
│  2. リクエストがCloud Runに届く                              │
│     「/ に GET でアクセスしたい」                            │
│                                                             │
│  3. Cloud Runがエントリポイントを確認                        │
│     「設定によると 'app' だな」                              │
│                                                             │
│  4. コード内の 'app' 関数を実行                              │
│                                                             │
│     【Python版】                                            │
│     @functions_framework.http                               │
│     def app(request):                                       │
│         path = request.path  # → "/"                       │
│         if path == '/':                                     │
│             return (HTML_CONTENT, 200, headers)             │
│                                                             │
│     【JavaScript版】                                         │
│     functions.http('app', async (req, res) => {            │
│         const path = req.path;  // → "/"                   │
│         if (path === '/') {                                 │
│             res.send(htmlContent);                          │
│         }                                                   │
│     });                                                     │
│                                                             │
│  5. HTMLがブラウザに返される                                 │
│                                                             │
│  6. ブラウザがHTMLを表示                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## なぜ「app」という名前？

**名前は何でもOK**

```python
# これでも動く
@functions_framework.http
def myFunction(request):
    ...
```

```javascript
// これでも動く
functions.http('handleRequest', async (req, res) => {
    ...
});
```

**「app」を使う理由**
- 短くて覚えやすい
- 「アプリケーション」の略
- 多くのフレームワークで慣例的に使われる

**重要なのは「GCPの設定と一致させること」**

```
GCPの設定              コード
─────────────────────────────────────
app            →    def app(...)
myFunction     →    def myFunction(...)
handleRequest  →    functions.http('handleRequest', ...)
```

---

## URL ごとの処理分岐

エントリポイントは1つですが、URL によって処理を分岐させます。

```python
@functions_framework.http
def app(request):
    path = request.path

    if path == '/':
        # トップページを返す
        return (HTML_CONTENT, 200, headers)

    elif path == '/api/chat':
        # チャットAPIを処理
        return handle_chat(request)

    elif path == '/api/health':
        # ヘルスチェック
        return ({'status': 'ok'}, 200, headers)

    else:
        # 404エラー
        return ({'error': 'Not found'}, 404, headers)
```

**イメージ**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  会社の受付（= app 関数）                                    │
│                                                             │
│  来客: 「/（トップ）に来ました」                             │
│  受付: 「こちらのパンフレットをどうぞ」 → HTML を返す         │
│                                                             │
│  来客: 「/api/chat に来ました」                              │
│  受付: 「AIチャット担当へご案内します」 → チャット処理        │
│                                                             │
│  来客: 「/unknown に来ました」                               │
│  受付: 「そのような部署はございません」 → 404 エラー          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## まとめ

| 項目 | 説明 |
|------|------|
| エントリポイントとは | プログラムの入口となる関数の名前 |
| 設定場所 | GCPコンソール → Cloud Run functions → エントリポイント |
| 重要なこと | GCPの設定とコード内の関数名を一致させる |
| Python の場合 | `@functions_framework.http` + `def 関数名(request):` |
| Node.js の場合 | `functions.http('関数名', (req, res) => {...})` |

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ★ 覚えること ★                                            │
│                                                             │
│  1. エントリポイント = 最初に呼ばれる関数の名前              │
│                                                             │
│  2. GCPの設定とコードの関数名を一致させる                    │
│                                                             │
│  3. このアプリでは「app」を使っている                        │
│                                                             │
│  4. URL ごとの処理分岐は app 関数の中で行う                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
