# script.js

フロントエンドの処理（JavaScript）

```javascript
/**
 * AI チャットアプリ - フロントエンド（ブラウザ側処理）
 *
 * ╔═════════════════════════════════════════════════════════════╗
 * ║ 【処理の流れ】                                               ║
 * ║  1. Firebase設定     → プロジェクトごとに書き換え           ║
 * ║  2. 認証状態監視     → ログイン/ログアウトを検知            ║
 * ║  3. 画面切り替え     → ログイン/拒否/チャット画面を切替     ║
 * ║  4. 認証関数         → ログイン/ログアウト処理              ║
 * ║  5. アクセス権限確認 → バックエンドに問い合わせ             ║
 * ║  6. チャット機能     → AIとの会話処理                       ║
 * ╚═════════════════════════════════════════════════════════════╝
 */

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. ★★★ Firebase設定（プロジェクトごとに変更が必要）★★★
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Firebaseコンソール → プロジェクト設定 → 「構成」で確認できます
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",                     // ← 書き換え必須
    authDomain: "YOUR_PROJECT.firebaseapp.com", // ← 書き換え必須
    projectId: "YOUR_PROJECT_ID",               // ← 書き換え必須
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "000000000000",
    appId: "YOUR_APP_ID"
};

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. 初期化【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
let currentUser = null;

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. 認証状態監視【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ログイン/ログアウトすると自動でこの関数が呼ばれる
auth.onAuthStateChanged(async (user) => {
    if (user) {
        // ログイン済み → アクセス権限を確認
        currentUser = user;
        const isAllowed = await checkAccess(user);
        isAllowed ? showChat(user) : showDenied(user);
    } else {
        // 未ログイン → ログイン画面を表示
        currentUser = null;
        showLogin();
    }
});

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. 画面切り替え【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// $('id名') で要素を取得するショートカット
const $ = id => document.getElementById(id);

// ログイン画面を表示
function showLogin() {
    $('login-screen').classList.remove('hidden');
    $('chat-screen').classList.add('hidden');
    $('access-denied').classList.add('hidden');
    $('user-info').classList.add('hidden');
}

// アクセス拒否画面を表示
function showDenied(user) {
    $('login-screen').classList.add('hidden');
    $('chat-screen').classList.add('hidden');
    $('access-denied').classList.remove('hidden');
    $('user-info').classList.add('hidden');
    $('denied-email').textContent = user.email;
}

// チャット画面を表示
function showChat(user) {
    $('login-screen').classList.add('hidden');
    $('chat-screen').classList.remove('hidden');
    $('access-denied').classList.add('hidden');
    $('user-info').classList.remove('hidden');
    $('user-name').textContent = user.displayName;
    $('user-photo').src = user.photoURL || '';
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 5. 認証関数【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// Googleでログイン
async function login() {
    try {
        await auth.signInWithPopup(new firebase.auth.GoogleAuthProvider());
    } catch (e) {
        alert('ログインに失敗しました');
    }
}

// ログアウト
async function logout() {
    await auth.signOut();
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 6. アクセス権限チェック【削除禁止】
// → バックエンドの /api/check-access を呼び出し
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async function checkAccess(user) {
    try {
        // JWTトークン（デジタル会員証）を取得
        const token = await user.getIdToken();

        // バックエンドに確認リクエストを送信
        const res = await fetch('/api/check-access', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`  // 会員証を提示
            }
        });
        const data = await res.json();
        return data.allowed === true;
    } catch (e) {
        return false;
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 7. ★★★ チャット機能（ここをカスタマイズ）★★★
// → バックエンドの /api/chat を呼び出し
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const chatContainer = $('chat-container');
const messageInput = $('message-input');
const sendBtn = $('send-btn');

// メッセージを画面に追加
function addMessage(text, type) {
    const div = document.createElement('div');
    div.className = `message ${type}`;
    div.textContent = text;
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// 「考え中...」のローディング表示を追加
function addLoading() {
    const div = document.createElement('div');
    div.className = 'message assistant';
    div.innerHTML = '<span class="loading"></span> 考え中...';
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return div;
}

// メッセージ送信処理
async function sendMessage() {
    if (!currentUser) return alert('ログインしてください');
    const message = messageInput.value.trim();
    if (!message) return;

    // 送信ボタンを無効化（連打防止）
    sendBtn.disabled = true;

    // ユーザーのメッセージを表示
    addMessage(message, 'user');
    messageInput.value = '';
    const loading = addLoading();

    try {
        // JWTトークン（デジタル会員証）を取得
        const token = await currentUser.getIdToken();

        // バックエンドにメッセージを送信
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

        // 結果を表示
        addMessage(res.ok ? data.response : `エラー: ${data.error}`, res.ok ? 'assistant' : 'error');
    } catch (e) {
        loading.remove();
        addMessage('エラー: 通信に失敗しました', 'error');
    }

    sendBtn.disabled = false;
    messageInput.focus();
}

// Enterキーで送信
messageInput.addEventListener('keypress', e => {
    if (e.key === 'Enter') sendMessage();
});

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 【新しい機能を追加する場所】
// 例: チャット履歴保存、ファイルアップロード等
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
