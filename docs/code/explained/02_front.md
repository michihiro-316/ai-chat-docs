# front.html 詳細解説

このファイルは画面の「構造」を定義します。レストランで言えば「店内の装飾、テーブル配置」です。

---

## 目次 { data-toc-skip }

1. [HTMLの基本構造](#1-htmlの基本構造)
2. [head部分](#2-head部分)
3. [CSS（スタイル）](#3-cssスタイル)
4. [body部分（画面構造）](#4-body部分画面構造)
5. [各画面の役割](#5-各画面の役割)

---

## 1. HTMLの基本構造

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <!-- ここに設定やスタイル -->
</head>
<body>
    <!-- ここに画面の内容 -->
</body>
</html>
```

**各部分の役割**

| 部分 | 役割 | 例え |
|------|------|------|
| `<!DOCTYPE html>` | 「これはHTML5です」と宣言 | 「日本語で書かれています」 |
| `<html lang="ja">` | HTMLの開始、言語は日本語 | 本の表紙 |
| `<head>` | 設定情報（画面には表示されない） | 本の奥付 |
| `<body>` | 実際に表示される内容 | 本の本文 |

---

## 2. head部分

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI チャット</title>
    <!-- Firebase SDK -->
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <style>
        /* CSSがここに入る */
    </style>
</head>
```

### 各要素の解説

#### `<meta charset="UTF-8">`

```html
<meta charset="UTF-8">
```

**何をするもの？**
- 文字コードを指定する
- UTF-8 = 日本語を含む世界中の文字が使える

**これがないと？**
```
こんにちは → ã"ã‚"ã«ã¡ã¯ （文字化け）
```

---

#### `<meta name="viewport">`

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**何をするもの？**
- スマートフォンでの表示を最適化する

**各設定の意味**

| 設定 | 意味 |
|------|------|
| `width=device-width` | 画面幅をデバイスの幅に合わせる |
| `initial-scale=1.0` | 初期ズームを100%にする |

**これがないと？**
- スマホでPC版サイトが縮小表示される
- 文字が小さくて読めない

---

#### `<title>`

```html
<title>AI チャット</title>
```

**何をするもの？**
- ブラウザのタブに表示されるタイトル

```
┌─────────────────────────────────────────┐
│ 🌐 AI チャット   │ × │                 │
├─────────────────────────────────────────┤
│                                         │
│           （ページの内容）               │
│                                         │
└─────────────────────────────────────────┘
      ↑
   ここに表示される
```

---

#### Firebase SDK の読み込み

```html
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
```

**何をするもの？**
- Firebase（Googleのサービス）の機能を使えるようにする
- 特にGoogleログイン機能に必要

**2つのファイルの役割**

| ファイル | 役割 |
|---------|------|
| `firebase-app-compat.js` | Firebase の基本機能 |
| `firebase-auth-compat.js` | 認証（ログイン）機能 |

**`-compat` とは？**
- 互換モード（古い書き方でも動く）
- 新しいモジュール形式でなくても使える

---

## 3. CSS（スタイル）

CSSは「見た目」を定義します。

### 基本リセット

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
```

**何をするもの？**

| プロパティ | 意味 |
|-----------|------|
| `*` | すべての要素に適用 |
| `margin: 0` | 外側の余白をなくす |
| `padding: 0` | 内側の余白をなくす |
| `box-sizing: border-box` | 幅の計算方法を統一 |

**なぜ必要？**
- ブラウザごとにデフォルトのスタイルが違う
- リセットすることで統一した見た目にできる

---

### body のスタイル

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #f5f5f5;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
```

| プロパティ | 意味 |
|-----------|------|
| `font-family` | フォントの優先順位 |
| `background` | 背景色（薄いグレー） |
| `min-height: 100vh` | 最低でも画面の高さ分 |
| `display: flex` | フレックスボックスを使う |
| `flex-direction: column` | 縦方向に並べる |

**フォントの優先順位**
```
-apple-system     → Mac/iOS のシステムフォント
BlinkMacSystemFont → Chrome on Mac
'Segoe UI'        → Windows
Roboto            → Android
sans-serif        → どれもなければゴシック系
```

---

### ヘッダーのスタイル

```css
header {
    background: #1a73e8;
    color: white;
    padding: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

```
┌─────────────────────────────────────────────────────────────┐
│  AI チャット                        👤 田中太郎  ログアウト  │
│  ← justify-content: space-between で左右に分散 →           │
└─────────────────────────────────────────────────────────────┘
```

---

### メッセージのスタイル

```css
.message {
    margin-bottom: 16px;
    padding: 12px 16px;
    border-radius: 8px;
    max-width: 80%;
}
.user { background: #e3f2fd; margin-left: auto; text-align: right; }
.assistant { background: #f5f5f5; margin-right: auto; }
.error { background: #ffebee; color: #c62828; }
```

**表示イメージ**

```
┌─────────────────────────────────────────────────────────────┐
│  ┌──────────────────────────────┐                          │
│  │ こんにちは！何でも聞いてください │  ← assistant（左寄せ） │
│  └──────────────────────────────┘                          │
│                                                             │
│                        ┌──────────────────────────────┐    │
│      user（右寄せ） →  │ プログラミングを教えて         │    │
│                        └──────────────────────────────┘    │
│                                                             │
│  ┌──────────────────────────────┐                          │
│  │ プログラミングとは...          │  ← assistant（左寄せ） │
│  └──────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────┘
```

---

### ローディングアニメーション

```css
.loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 2px solid #f3f3f3;
    border-top: 2px solid #1a73e8;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
```

**仕組み**

```
┌────────────────────────────────────────┐
│     ⟳ 考え中...                        │
│     ↑                                  │
│  border-top だけ青色にして回転させる    │
│  → くるくる回っているように見える       │
└────────────────────────────────────────┘
```

---

### hidden クラス

```css
.hidden { display: none !important; }
```

**何をするもの？**
- 要素を非表示にする
- JavaScriptで画面を切り替える時に使う

**使用例（script.js）**
```javascript
// ログイン画面を表示
$('login-screen').classList.remove('hidden');  // 表示
$('chat-screen').classList.add('hidden');      // 非表示
```

---

## 4. body部分（画面構造）

### ヘッダー

```html
<header>
    <h1>AI チャット</h1>
    <div id="user-info" class="user-info hidden">
        <img id="user-photo" src="" alt="">
        <span id="user-name"></span>
        <button class="btn btn-outline" onclick="logout()">ログアウト</button>
    </div>
</header>
```

**ポイント**

| 要素 | 説明 |
|------|------|
| `id="user-info"` | JavaScriptから操作するためのID |
| `class="hidden"` | 最初は非表示（ログイン後に表示） |
| `onclick="logout()"` | クリックで `logout()` 関数を実行 |

---

### main（メイン領域）

```html
<main>
    <!-- ログイン画面 -->
    <div id="login-screen" class="center-screen">...</div>

    <!-- アクセス拒否画面 -->
    <div id="access-denied" class="center-screen hidden">...</div>

    <!-- チャット画面 -->
    <div id="chat-screen" class="hidden">...</div>
</main>
```

**3つの画面がある**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   login-screen      → 最初に表示                            │
│   access-denied     → hidden（権限がない時に表示）          │
│   chat-screen       → hidden（ログイン成功時に表示）        │
│                                                             │
│   ※ 同時に表示されるのは1つだけ                             │
│   ※ script.js で hidden を付け外しして切り替える            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. 各画面の役割

### ログイン画面

```html
<div id="login-screen" class="center-screen">
    <h2>ようこそ</h2>
    <p style="margin: 20px 0; color: #666;">Googleアカウントでログインしてください</p>
    <button class="google-btn" onclick="login()">
        <svg>...</svg>
        Googleでログイン
    </button>
</div>
```

**表示イメージ**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                         ようこそ                            │
│                                                             │
│           Googleアカウントでログインしてください              │
│                                                             │
│               ┌────────────────────────┐                   │
│               │ 🔵 Googleでログイン     │                   │
│               └────────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**onclick="login()"**
- ボタンをクリックすると `script.js` の `login()` 関数が実行される

---

### アクセス拒否画面

```html
<div id="access-denied" class="center-screen hidden">
    <h2 style="color: #c62828;">アクセスが許可されていません</h2>
    <p style="margin: 20px 0; color: #666;">管理者にお問い合わせください。</p>
    <p style="color: #999; font-size: 14px;">ログイン中: <span id="denied-email"></span></p>
    <button class="btn" style="margin-top: 20px;" onclick="logout()">別のアカウントでログイン</button>
</div>
```

**表示イメージ**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              アクセスが許可されていません                    │
│                                                             │
│              管理者にお問い合わせください                    │
│                                                             │
│            ログイン中: tanaka@example.com                   │
│                                                             │
│               ┌────────────────────────┐                   │
│               │  別のアカウントでログイン │                   │
│               └────────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### チャット画面

```html
<div id="chat-screen" class="hidden">
    <div id="chat-container" class="chat-container">
        <div class="message assistant">こんにちは！何でも聞いてください。</div>
    </div>
    <div class="input-area">
        <input type="text" id="message-input" placeholder="メッセージを入力..." autocomplete="off">
        <button id="send-btn" class="btn" onclick="sendMessage()">送信</button>
    </div>
</div>
```

**表示イメージ**

```
┌─────────────────────────────────────────────────────────────┐
│  ┌─────────────────────────────────────────────────────┐   │
│  │ こんにちは！何でも聞いてください。                    │   │
│  │                                                     │   │
│  │                              プログラミングを教えて │   │
│  │                                                     │   │
│  │ プログラミングとは...                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────────────────────────────────────┐ ┌─────┐     │
│  │ メッセージを入力...                        │ │送信 │     │
│  └──────────────────────────────────────────┘ └─────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

### JavaScript の読み込み

```html
<script src="script.js"></script>
```

**配置位置が重要！**

```html
<body>
    <!-- 画面の内容 -->
    ...

    <!-- 最後に読み込む -->
    <script src="script.js"></script>
</body>
```

**なぜ最後に置く？**
1. HTMLが先に読み込まれる
2. その後でJavaScriptが実行される
3. JavaScriptがHTML要素を操作できる

**もし先に置くと？**
```javascript
// HTMLがまだ読み込まれていない
$('chat-container')  // → null（要素が見つからない）
```

---

## HTMLとJavaScriptの連携

HTMLとJavaScriptは `id` で連携します。

```html
<!-- HTML側 -->
<div id="chat-screen">...</div>
<input id="message-input">
<button onclick="sendMessage()">送信</button>
```

```javascript
// JavaScript側
$('chat-screen').classList.remove('hidden');  // id で要素を取得
const message = $('message-input').value;     // 入力値を取得
function sendMessage() { ... }                // onclick で呼ばれる関数
```

**$ 関数とは？**

```javascript
const $ = id => document.getElementById(id);
```

- `$('chat-screen')` は `document.getElementById('chat-screen')` の短縮形
- jQuery ではなく、自分で定義したショートカット
