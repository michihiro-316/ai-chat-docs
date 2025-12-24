# script.js 詳細解説

このファイルは画面の「動き」を担当します。レストランで言えば「ウェイター」です。

---

## 目次 { data-toc-skip }

1. [Firebase設定](#1-firebase設定)
2. [初期化](#2-初期化)
3. [認証状態監視](#3-認証状態監視)
4. [画面切り替え](#4-画面切り替え)
5. [認証関数](#5-認証関数)
6. [アクセス権限チェック](#6-アクセス権限チェック)
7. [チャット機能](#7-チャット機能)

---

## 1. Firebase設定

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "000000000000",
    appId: "YOUR_APP_ID"
};
```

### 各項目の意味

| 項目 | 意味 | 例 |
|------|------|-----|
| `apiKey` | Firebaseプロジェクトの識別キー | `AIzaSyC...` |
| `authDomain` | 認証用のドメイン | `my-app.firebaseapp.com` |
| `projectId` | プロジェクトID | `my-chat-app-12345` |
| `storageBucket` | ファイル保存用 | `my-app.appspot.com` |
| `messagingSenderId` | プッシュ通知用 | `123456789012` |
| `appId` | アプリのID | `1:123...:web:abc...` |

### 設定値の確認方法

1. [Firebaseコンソール](https://console.firebase.google.com/) を開く
2. プロジェクトを選択
3. 歯車アイコン → 「プロジェクトの設定」
4. 「マイアプリ」セクションで確認

---

## 2. 初期化

```javascript
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
let currentUser = null;
```

### 各行の解説

#### `firebase.initializeApp(firebaseConfig)`

```javascript
firebase.initializeApp(firebaseConfig);
```

**何をしている？**
- Firebaseを初期化する
- 設定情報を使ってFirebaseに接続する準備をする

!!! tip "イメージ"

    1. 設定情報を渡す
    2. Firebase：「了解！my-chat-app-12345 プロジェクトですね」
    3. 接続準備完了！

---

#### `const auth = firebase.auth()`

```javascript
const auth = firebase.auth();
```

**何をしている？**
- 認証機能を使えるようにする
- `auth` 変数に認証オブジェクトを保存

**これ以降できること**
```javascript
auth.signInWithPopup(...)  // ログイン
auth.signOut()             // ログアウト
auth.onAuthStateChanged()  // 状態監視
```

---

#### `let currentUser = null`

```javascript
let currentUser = null;
```

**何をしている？**
- 現在ログインしているユーザーを保存する変数
- 最初は誰もログインしていないので `null`

**`const` と `let` の違い**

| 宣言 | 再代入 | 用途 |
|------|:------:|------|
| `const` | ✗ できない | 変わらない値 |
| `let` | ○ できる | 変わる可能性がある値 |

```javascript
const auth = firebase.auth();  // auth は変わらない
let currentUser = null;        // currentUser はログインで変わる
```

---

## 3. 認証状態監視

```javascript
auth.onAuthStateChanged(async (user) => {
    if (user) {
        currentUser = user;
        const isAllowed = await checkAccess(user);
        isAllowed ? showChat(user) : showDenied(user);
    } else {
        currentUser = null;
        showLogin();
    }
});
```

!!! note "処理の流れ：auth.onAuthStateChanged(...)"

    「ログイン状態が変わったら教えて」とFirebaseにお願いする

    | 変化 | user の値 | if (user) |
    |------|-----------|-----------|
    | 未ログイン → ログイン | ユーザー情報が入る | true |
    | ログイン → ログアウト | null になる | false |

### 各部分の解説

#### `async (user) => { ... }`

```javascript
async (user) => {
    // 処理
}
```

**アロー関数とは？**
```javascript
// 従来の書き方
function(user) { ... }

// アロー関数（同じ意味）
(user) => { ... }
```

**`async` とは？**
- 「この関数の中で `await` を使います」という宣言
- 非同期処理を待てるようになる

---

#### `await checkAccess(user)`

```javascript
const isAllowed = await checkAccess(user);
```

**`await` とは？**
- 処理が終わるまで待つ
- `checkAccess()` はサーバーに問い合わせるので時間がかかる

!!! warning "await なしの場合"

    ```javascript
    const isAllowed = checkAccess(user);  // Promise が返る
    console.log(isAllowed);  // Promise {<pending>} ???
    ```

!!! success "await ありの場合"

    ```javascript
    const isAllowed = await checkAccess(user);  // 待つ
    console.log(isAllowed);  // true または false
    ```

---

#### 三項演算子

```javascript
isAllowed ? showChat(user) : showDenied(user);
```

**三項演算子とは？**
```javascript
条件 ? trueの時の処理 : falseの時の処理
```

**if文で書くと**
```javascript
if (isAllowed) {
    showChat(user);
} else {
    showDenied(user);
}
```

---

## 4. 画面切り替え

### $ 関数（ショートカット）

```javascript
const $ = id => document.getElementById(id);
```

**何をしている？**
- `document.getElementById()` の短縮形を作っている

**使い方**
```javascript
// 通常の書き方
document.getElementById('login-screen')

// $ を使った書き方（同じ意味）
$('login-screen')
```

---

### showLogin()

```javascript
function showLogin() {
    $('login-screen').classList.remove('hidden');
    $('chat-screen').classList.add('hidden');
    $('access-denied').classList.add('hidden');
    $('user-info').classList.add('hidden');
}
```

!!! note "何をしている？"

    | 要素 | hidden | 結果 |
    |------|--------|------|
    | login-screen | 外す | 表示される |
    | chat-screen | 付ける | 非表示になる |
    | access-denied | 付ける | 非表示になる |
    | user-info | 付ける | 非表示になる |

**classList とは？**
- 要素についているクラスを操作する
- `add()` でクラスを追加
- `remove()` でクラスを削除

---

### showDenied(user)

```javascript
function showDenied(user) {
    $('login-screen').classList.add('hidden');
    $('chat-screen').classList.add('hidden');
    $('access-denied').classList.remove('hidden');
    $('user-info').classList.add('hidden');
    $('denied-email').textContent = user.email;
}
```

!!! note "何をしている？"

    - アクセス拒否画面を表示
    - 拒否されたメールアドレスを表示

!!! example "画面表示イメージ"

    **アクセスが許可されていません**

    ログイン中: tanaka@example.com ← `$('denied-email').textContent = user.email;`

---

### showChat(user)

```javascript
function showChat(user) {
    $('login-screen').classList.add('hidden');
    $('chat-screen').classList.remove('hidden');
    $('access-denied').classList.add('hidden');
    $('user-info').classList.remove('hidden');
    $('user-name').textContent = user.displayName;
    $('user-photo').src = user.photoURL || '';
}
```

**何をしている？**
- チャット画面を表示
- ヘッダーにユーザー情報を表示

**`user.photoURL || ''` とは？**
```javascript
user.photoURL || ''
// user.photoURL があればそれを使う
// なければ空文字を使う（画像なし）
```

---

## 5. 認証関数

### login()

```javascript
async function login() {
    try {
        await auth.signInWithPopup(new firebase.auth.GoogleAuthProvider());
    } catch (e) {
        alert('ログインに失敗しました');
    }
}
```

!!! note "処理の流れ"

    1. ユーザーが「Googleでログイン」ボタンをクリック
    2. `login()` 関数が呼ばれる
    3. `auth.signInWithPopup()` でポップアップが開く
    4. ユーザーがGoogleアカウントを選択
    5. ログイン成功
    6. `onAuthStateChanged` が発火（自動）
    7. `checkAccess` → `showChat` or `showDenied`

**try-catch とは？**
```javascript
try {
    // エラーが起きるかもしれない処理
} catch (e) {
    // エラーが起きた時の処理
}
```

---

### logout()

```javascript
async function logout() {
    await auth.signOut();
}
```

!!! note "処理の流れ"

    1. ユーザーが「ログアウト」ボタンをクリック
    2. `logout()` 関数が呼ばれる
    3. `auth.signOut()` でログアウト
    4. `onAuthStateChanged` が発火（自動）
    5. user が null なので `showLogin()` が呼ばれる

---

## 6. アクセス権限チェック

```javascript
async function checkAccess(user) {
    try {
        const token = await user.getIdToken();

        const res = await fetch('/api/check-access', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });
        const data = await res.json();
        return data.allowed === true;
    } catch (e) {
        return false;
    }
}
```

### 各行の解説

#### `const token = await user.getIdToken()`

```javascript
const token = await user.getIdToken();
```

**何をしている？**
- JWTトークン（デジタル会員証）を取得
- これをサーバーに送って「誰か」を証明する

**トークンの中身（イメージ）**
```
eyJhbGciOiJS...（長い文字列）

↓ デコードすると

{
  "email": "tanaka@example.com",
  "name": "田中太郎",
  "exp": 1703500800  // 有効期限
}
```

---

#### `fetch('/api/check-access', {...})`

```javascript
const res = await fetch('/api/check-access', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    }
});
```

**fetch とは？**
- サーバーにHTTPリクエストを送る関数
- レストランの注文を厨房に伝えるイメージ

**各オプションの意味**

| オプション | 意味 |
|-----------|------|
| `method: 'POST'` | データを送る（POSTリクエスト） |
| `Content-Type` | 送るデータの形式（JSON） |
| `Authorization` | 認証情報（会員証） |

**`Bearer ${token}` とは？**
```javascript
`Bearer ${token}`
// テンプレートリテラル：文字列の中に変数を埋め込む

// 例
const token = "abc123";
`Bearer ${token}`  // → "Bearer abc123"
```

---

#### `const data = await res.json()`

```javascript
const data = await res.json();
return data.allowed === true;
```

**何をしている？**
1. サーバーからの返事をJSONとして解析
2. `allowed` が `true` かどうかを返す

**サーバーからの返事の例**
```json
{"allowed": true}   // 許可
{"allowed": false}  // 拒否
```

---

## 7. チャット機能

### 変数の準備

```javascript
const chatContainer = $('chat-container');
const messageInput = $('message-input');
const sendBtn = $('send-btn');
```

**何をしている？**
- よく使う要素を変数に保存
- 毎回 `$('...')` を書かなくて済む

---

### addMessage() - メッセージ追加

```javascript
function addMessage(text, type) {
    const div = document.createElement('div');
    div.className = `message ${type}`;
    div.textContent = text;
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}
```

!!! note "処理の流れ：addMessage(\"こんにちは\", \"user\")"

    | ステップ | 処理内容 | 結果 |
    |----------|----------|------|
    | 1 | div要素を作成 | `<div></div>` |
    | 2 | クラスを設定 | `<div class="message user"></div>` |
    | 3 | テキストを設定 | `<div class="message user">こんにちは</div>` |
    | 4 | チャットコンテナに追加 | `chatContainer.appendChild(div)` |
    | 5 | 一番下までスクロール | `chatContainer.scrollTop = chatContainer.scrollHeight` |

!!! tip "scrollTop と scrollHeight"

    | プロパティ | 意味 |
    |------------|------|
    | `scrollTop = 0` | 一番上 |
    | `scrollTop = scrollHeight` | 一番下 |

    `scrollTop = scrollHeight` にすると一番下に移動

---

### addLoading() - ローディング表示

```javascript
function addLoading() {
    const div = document.createElement('div');
    div.className = 'message assistant';
    div.innerHTML = '<span class="loading"></span> 考え中...';
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return div;
}
```

**何をしている？**
- 「⟳ 考え中...」を表示
- 作成した要素を返す（後で削除するため）

**textContent と innerHTML の違い**

| プロパティ | HTMLタグ |
|-----------|---------|
| `textContent` | そのまま文字として表示 |
| `innerHTML` | HTMLとして解釈 |

```javascript
div.textContent = '<b>太字</b>';  // → "<b>太字</b>" と表示
div.innerHTML = '<b>太字</b>';    // → 太字 と表示
```

---

### sendMessage() - メッセージ送信

```javascript
async function sendMessage() {
    if (!currentUser) return alert('ログインしてください');
    const message = messageInput.value.trim();
    if (!message) return;

    sendBtn.disabled = true;

    addMessage(message, 'user');
    messageInput.value = '';
    const loading = addLoading();

    try {
        const token = await currentUser.getIdToken();

        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ message })
        });
        const data = await res.json();
        loading.remove();

        addMessage(res.ok ? data.response : `エラー: ${data.error}`, res.ok ? 'assistant' : 'error');
    } catch (e) {
        loading.remove();
        addMessage('エラー: 通信に失敗しました', 'error');
    }

    sendBtn.disabled = false;
    messageInput.focus();
}
```

!!! note "処理の流れ"

    | # | 処理 | コード |
    |---|------|--------|
    | 1 | ログインチェック | `if (!currentUser) return alert(...);` |
    | 2 | 入力値を取得・チェック | `const message = messageInput.value.trim();` |
    | 3 | 送信ボタンを無効化（連打防止） | `sendBtn.disabled = true;` |
    | 4 | ユーザーのメッセージを表示 | `addMessage(message, 'user');` |
    | 5 | 入力欄をクリア | `messageInput.value = '';` |
    | 6 | ローディング表示 | `const loading = addLoading();` |
    | 7 | サーバーに送信 | `fetch('/api/chat', {...})` |
    | 8 | ローディングを削除 | `loading.remove();` |
    | 9 | 結果を表示 | `addMessage(data.response, 'assistant');` |
    | 10 | 送信ボタンを有効化 | `sendBtn.disabled = false;` |
    | 11 | 入力欄にフォーカス | `messageInput.focus();` |

---

### Enterキーで送信

```javascript
messageInput.addEventListener('keypress', e => {
    if (e.key === 'Enter') sendMessage();
});
```

**何をしている？**
- 入力欄でEnterキーを押したら `sendMessage()` を実行

**addEventListener とは？**
```javascript
要素.addEventListener(イベント名, 実行する関数);
```

| イベント名 | 発生タイミング |
|-----------|---------------|
| `'click'` | クリック時 |
| `'keypress'` | キー入力時 |
| `'submit'` | フォーム送信時 |
| `'load'` | 読み込み完了時 |

---

## まとめ：ファイル間の連携

!!! info "ファイル連携の全体像"

    **front.html** から始まる処理の流れ：

    | トリガー | 処理 |
    |----------|------|
    | `<button onclick="login()">` クリック | script.js の `login()` が実行 |
    | `<button onclick="sendMessage()">` クリック | script.js の `sendMessage()` が実行 → `fetch('/api/chat')` → backend.py が処理 → script.js で結果を表示 |
    | `<script src="script.js">` 読み込み | script.js が実行される |
