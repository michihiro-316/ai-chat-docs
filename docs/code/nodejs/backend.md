# backend.js

サーバー側の処理（メイン）

```javascript
/**
 * AI チャットアプリ - バックエンド（サーバー側処理）
 *
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 * 【HTTP通信とは？ - 手紙のやり取りに例えると】
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 *
 * ブラウザ（フロントエンド）とサーバー（バックエンド）は「手紙」でやり取りします。
 *
 * ┌─────────────────────────────────────────────────────────────┐
 * │  fetch('/api/chat', {                                       │
 * │      method: 'POST',                    ← 手紙の種類        │
 * │      headers: { Authorization: '...' }, ← 封筒の情報        │
 * │      body: JSON.stringify({ message })  ← 手紙の中身        │
 * │  })                                                         │
 * └─────────────────────────────────────────────────────────────┘
 *
 * ■ method = 手紙の種類（GET=情報ください / POST=これ処理して）
 * ■ headers = 封筒の情報（認証トークン等）
 * ■ body = 手紙の中身（送りたいデータ）
 *
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 * 【JWTトークンとは？ - 会員証に例えると】
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 *
 * JWTトークン = 「デジタル会員証」のようなもの。
 *
 * ┌─────────────────────────────────────────────────────────────┐
 * │  Googleでログイン                                            │
 * │       ↓                                                     │
 * │  Firebaseが「この人は○○さんです」という会員証を発行         │
 * │       ↓                                                     │
 * │  その会員証（JWTトークン）をサーバーに見せてアクセス         │
 * └─────────────────────────────────────────────────────────────┘
 *
 * ■ なぜ必要？
 *   → サーバーは「誰からのリクエストか」を確認する必要がある
 *   → JWTトークンの中にメールアドレス等の情報が入っている
 *
 * ■ このコードでの使われ方
 *   1. フロントエンド: ログイン後、トークンをheadersに入れて送信
 *   2. バックエンド: トークンからメールアドレスを取り出して認証
 */

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ライブラリ読み込み【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// Cloud Run functions でHTTPリクエストを受け取るために必要（Google提供）
const functions = require('@google-cloud/functions-framework');

// ChatGPT APIを呼び出すために必要（OpenAI提供）
const OpenAI = require('openai');

// ファイルを読み込むために必要（Node.js標準機能）
const fs = require('fs');

// ファイルパスを扱うために必要（Node.js標準機能）
const path = require('path');

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ★★★ 設定（プロジェクトごとに変更が必要）★★★
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/**
 * 【CORS設定 - 本番環境では変更推奨】
 *
 * ■ これは何？
 *   「どのWebサイトからのアクセスを許可するか」の設定です。
 *   '*' は「どこからでもOK」という意味（開発用）。
 *
 * ■ 本番ではどうする？
 *   Cloud Runの関数URL（デプロイ後に表示される）を設定します。
 *
 *   【確認方法】
 *   GCPコンソール → Cloud Run → 関数をクリック → 上部に表示されるURL
 *   例: https://ai-chat-app-xxxxx-an.a.run.app
 *
 *   【設定例】
 *   const ALLOWED_ORIGINS = [
 *       'https://ai-chat-app-xxxxx-an.a.run.app'
 *   ];
 *
 * ■ 今は変更しなくてOK
 *   このアプリはフロントとバックエンドが同じURLなので、
 *   '*' のままでも動作します。
 */
const ALLOWED_ORIGINS = ['*'];

// HTMLファイル読み込み【削除禁止】
const HTML_CONTENT = fs.readFileSync(path.join(__dirname, 'front.html'), 'utf8');

// JavaScriptファイル読み込み【削除禁止】
const SCRIPT_CONTENT = fs.readFileSync(path.join(__dirname, 'script.js'), 'utf8');

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ヘルパー関数【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// CORSヘッダー設定
function setCorsHeaders(res, origin) {
    if (ALLOWED_ORIGINS.includes('*') || ALLOWED_ORIGINS.includes(origin)) {
        res.set('Access-Control-Allow-Origin', origin || '*');
    }
    res.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.set('Access-Control-Max-Age', '3600');
}

// セキュリティヘッダー設定
function setSecurityHeaders(res) {
    res.set('X-Content-Type-Options', 'nosniff');
    res.set('X-Frame-Options', 'DENY');
    res.set('X-XSS-Protection', '1; mode=block');
    res.set('Referrer-Policy', 'strict-origin-when-cross-origin');
}

/**
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 * ★★★ アクセス制御（重要！削除禁止）★★★
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 *
 * この関数がないと、誰でもアプリを使えてしまいます。
 *
 * 【環境変数の設定方法】GCPコンソール → Cloud Run → 環境変数
 *   ALLOWED_EMAILS: "admin@example.com,user1@example.com"
 *   ALLOWED_DOMAINS: "@yourcompany.co.jp"
 *
 * 【注意】両方未設定だと全員許可になります（開発用）
 */
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

    // 設定なし = 全員許可（開発用）
    if (allowedEmails.length === 0 && allowedDomains.length === 0) {
        console.warn('⚠️ ALLOWED_EMAILS/ALLOWED_DOMAINS 未設定');
        return true;
    }
    return false;
}

// JWTトークンからメールアドレス取得【削除禁止】
function getEmailFromToken(idToken) {
    try {
        const payload = idToken.split('.')[1];
        const decoded = Buffer.from(payload, 'base64').toString('utf8');
        return JSON.parse(decoded).email || null;
    } catch (e) {
        return null;
    }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// メインハンドラ【削除禁止】
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
//
// ■ メインハンドラとは？
//   「受付係」のようなもの。ブラウザからのリクエストを最初に受け取り、
//   URLに応じて適切な処理に振り分けます。
//
// ┌─────────────────────────────────────────────────────────────┐
// │  ブラウザ: 「/api/chat に POST でメッセージ送ります」         │
// │       ↓                                                     │
// │  メインハンドラ: 「/api/chat ですね、チャット処理に回します」  │
// │       ↓                                                     │
// │  チャットAPI: 「AIに問い合わせて返答します」                  │
// └─────────────────────────────────────────────────────────────┘
//
// ■ functions.http('app', ...) とは？
//   「appという名前でHTTPリクエストを受け取る入口を作る」という意味。
//   GCPはこの名前を見て、リクエストをこの関数に渡します。
//

functions.http('app', async (req, res) => {
    // ┌─────────────────────────────────────────────────────────────┐
    // │ req（リクエスト）= ブラウザから届いた「手紙」               │
    // │   - req.method  → 手紙の種類（GET/POST）                   │
    // │   - req.path    → どこ宛て？（/api/chat など）             │
    // │   - req.headers → 封筒の情報（認証トークンなど）           │
    // │   - req.body    → 手紙の中身（送られてきたデータ）         │
    // │                                                             │
    // │ res（レスポンス）= ブラウザに返す「返事」を作る道具         │
    // │   - res.json()  → JSON形式で返事を返す                     │
    // │   - res.send()  → テキストやHTMLで返事を返す               │
    // │   - res.status()→ 返事の状態（200=成功、404=見つからない） │
    // └─────────────────────────────────────────────────────────────┘

    const origin = req.headers.origin;

    // セキュリティ設定を返事に追加【削除禁止】
    setCorsHeaders(res, origin);
    setSecurityHeaders(res);

    // ┌─────────────────────────────────────────────────────────────┐
    // │ プリフライトリクエストとは？【削除禁止】                     │
    // │                                                             │
    // │ ブラウザが本番のリクエストを送る前に                        │
    // │ 「このサーバー、アクセスしていい？」と確認する仕組み        │
    // │                                                             │
    // │ ブラウザ: 「OPTIONSで確認します」                           │
    // │ サーバー: 「204（OK、中身なし）で返事」                     │
    // │ ブラウザ: 「じゃあ本番のPOSTを送ります」                    │
    // └─────────────────────────────────────────────────────────────┘
    if (req.method === 'OPTIONS') {
        return res.status(204).send('');
    }

    const reqPath = req.path;

    // ╔═════════════════════════════════════════════════════════════╗
    // ║ 【処理の流れ】ユーザーの操作順に並んでいます                 ║
    // ║                                                             ║
    // ║  1. / (トップページ)     → ユーザーが最初にアクセス         ║
    // ║  1b. /script.js          → フロントエンドのJavaScript       ║
    // ║  2. /api/check-access    → ログイン後、権限を確認           ║
    // ║  3. /api/chat            → メインのチャット機能             ║
    // ║  4. 【新しいAPIを追加】  → 機能拡張はここに                 ║
    // ║  5. /api/health          → 運用監視用（ユーザーは使わない） ║
    // ║  6. 404エラー            → どれにも該当しない場合           ║
    // ╚═════════════════════════════════════════════════════════════╝

    // ---------------------------------------------------------------
    // 1. トップページ表示【削除禁止】
    // → ユーザーが最初にアクセスする画面（ログイン画面が表示される）
    // ---------------------------------------------------------------
    if (reqPath === '/' && req.method === 'GET') {
        res.set('Content-Type', 'text/html; charset=utf-8');
        return res.send(HTML_CONTENT);
    }

    // ---------------------------------------------------------------
    // 1b. JavaScript配信【削除禁止】
    // → フロントエンドで使うJavaScript（front.htmlから読み込まれる）
    // ---------------------------------------------------------------
    if (reqPath === '/script.js' && req.method === 'GET') {
        res.set('Content-Type', 'application/javascript; charset=utf-8');
        return res.send(SCRIPT_CONTENT);
    }

    // ---------------------------------------------------------------
    // 2. アクセス権限チェック【削除禁止】
    // → ログイン後、このユーザーがアプリを使えるか確認
    // フロントエンドから: fetch('/api/check-access', { method: 'POST', headers: {...} })
    // ---------------------------------------------------------------
    if (reqPath === '/api/check-access' && req.method === 'POST') {
        try {
            const authHeader = req.headers.authorization;
            if (!authHeader?.startsWith('Bearer ')) {
                return res.status(401).json({ allowed: false, error: '認証トークンがありません' });
            }
            const email = getEmailFromToken(authHeader.split('Bearer ')[1]);
            if (!email) {
                return res.status(401).json({ allowed: false, error: 'メールアドレス取得失敗' });
            }
            const allowed = isEmailAllowed(email);
            console.log(`アクセス: ${email} → ${allowed ? '許可' : '拒否'}`);
            return res.json({ allowed });
        } catch (e) {
            return res.status(500).json({ allowed: false, error: 'エラーが発生しました' });
        }
    }

    // ---------------------------------------------------------------
    // 3. ★★★ チャットAPI（ここをカスタマイズ）★★★
    // → メインの機能。AIとチャットする
    // フロントエンドから: fetch('/api/chat', { method: 'POST', body: JSON.stringify({ message }) })
    // ---------------------------------------------------------------
    if (reqPath === '/api/chat' && req.method === 'POST') {
        try {
            // --- 認証チェック【削除禁止】---
            const authHeader = req.headers.authorization;
            if (!authHeader?.startsWith('Bearer ')) {
                return res.status(401).json({ error: 'ログインが必要です' });
            }
            const email = getEmailFromToken(authHeader.split('Bearer ')[1]);
            if (!isEmailAllowed(email)) {
                return res.status(403).json({ error: '権限がありません' });
            }

            // --- 入力チェック【削除禁止】---
            const { message } = req.body;
            if (!message || typeof message !== 'string') {
                return res.status(400).json({ error: 'メッセージを入力してください' });
            }
            if (message.length > 10000) {
                return res.status(400).json({ error: 'メッセージが長すぎます' });
            }

            // --- AI呼び出し【カスタマイズ可能】---
            const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
            const completion = await openai.chat.completions.create({
                model: 'gpt-3.5-turbo',  // ← gpt-4 に変更可能
                messages: [{ role: 'user', content: message }],
                max_tokens: 1000,        // ← 回答の長さ
                temperature: 0.7         // ← 0=固定的、1=創造的
            });

            return res.json({ response: completion.choices[0].message.content });

        } catch (e) {
            console.error('チャットエラー:', e.message);
            return res.status(500).json({ error: 'AIの処理中にエラーが発生しました' });
        }
    }

    // ---------------------------------------------------------------
    // 4. 【新しいAPIを追加する場所】
    // → 機能を追加したい場合はここに書く
    //
    // 例: チャット履歴を取得するAPI
    // if (reqPath === '/api/history' && req.method === 'GET') {
    //     // 認証チェック（上のチャットAPIからコピー）
    //     // 履歴を取得して返す処理
    //     return res.json({ history: [...] });
    // }
    // ---------------------------------------------------------------

    // ---------------------------------------------------------------
    // 5. ヘルスチェック【削除禁止】
    // → サーバーが動いているか確認用（運用監視用、ユーザーは使わない）
    // ---------------------------------------------------------------
    if (reqPath === '/api/health' && req.method === 'GET') {
        return res.json({ status: 'ok', timestamp: new Date().toISOString() });
    }

    // ---------------------------------------------------------------
    // 6. 404エラー【削除禁止】
    // → 上のどれにも該当しないURLにアクセスされた場合
    // ---------------------------------------------------------------
    return res.status(404).json({ error: 'ページが見つかりません' });
});
```
