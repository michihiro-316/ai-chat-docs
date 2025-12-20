"""
AI チャットアプリ - バックエンド（サーバー側処理）Python版

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【HTTP通信とは？ - 手紙のやり取りに例えると】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ブラウザ（フロントエンド）とサーバー（バックエンド）は「手紙」でやり取りします。

┌─────────────────────────────────────────────────────────────┐
│  fetch('/api/chat', {                                       │
│      method: 'POST',                    ← 手紙の種類        │
│      headers: { Authorization: '...' }, ← 封筒の情報        │
│      body: JSON.stringify({ message })  ← 手紙の中身        │
│  })                                                         │
└─────────────────────────────────────────────────────────────┘

■ method = 手紙の種類（GET=情報ください / POST=これ処理して）
■ headers = 封筒の情報（認証トークン等）
■ body = 手紙の中身（送りたいデータ）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【JWTトークンとは？ - 会員証に例えると】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

JWTトークン = 「デジタル会員証」のようなもの。

┌─────────────────────────────────────────────────────────────┐
│  Googleでログイン                                            │
│       ↓                                                     │
│  Firebaseが「この人は○○さんです」という会員証を発行             │
│       ↓                                                     │
│  その会員証（JWTトークン）をサーバーに見せてアクセス            │
└─────────────────────────────────────────────────────────────┘

■ なぜ必要？
  → サーバーは「誰からのリクエストか」を確認する必要がある
  → JWTトークンの中にメールアドレス等の情報が入っている

■ このコードでの使われ方
  1. フロントエンド: ログイン後、トークンをheadersに入れて送信
  2. バックエンド: トークンからメールアドレスを取り出して認証
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ライブラリ読み込み【削除禁止】
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import json
import base64
from datetime import datetime

# Cloud Run functions でHTTPリクエストを受け取るために必要（Google提供）
import functions_framework

# ChatGPT APIを呼び出すために必要（OpenAI提供）
from openai import OpenAI

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ★★★ 設定（プロジェクトごとに変更が必要）★★★
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 【CORS設定 - 本番環境では変更推奨】
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# ■ これは何？
#   「どのWebサイトからのアクセスを許可するか」の設定です。
#   '*' は「どこからでもOK」という意味（開発用）。
#
# ■ 本番ではどうする？
#   Cloud Runの関数URL（デプロイ後に表示される）を設定します。
#
#   【確認方法】
#   GCPコンソール → Cloud Run → 関数をクリック → 上部に表示されるURL
#   例: https://ai-chat-app-xxxxx-an.a.run.app
#
#   【設定例】
#   ALLOWED_ORIGINS = [
#       'https://ai-chat-app-xxxxx-an.a.run.app'
#   ]
#
# ■ 今は変更しなくてOK
#   このアプリはフロントとバックエンドが同じURLなので、
#   '*' のままでも動作します。
#
ALLOWED_ORIGINS = ['*']

# HTMLファイル読み込み【削除禁止】
with open('front.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()

# JavaScriptファイル読み込み【削除禁止】
with open('script.js', 'r', encoding='utf-8') as f:
    SCRIPT_CONTENT = f.read()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ヘルパー関数【削除禁止】
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def set_cors_headers(headers, origin):
    """CORSヘッダー設定"""
    if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
        headers['Access-Control-Allow-Origin'] = origin or '*'
    headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    headers['Access-Control-Max-Age'] = '3600'

def set_security_headers(headers):
    """セキュリティヘッダー設定"""
    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Frame-Options'] = 'DENY'
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ★★★ アクセス制御（重要！削除禁止）★★★
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# この関数がないと、誰でもアプリを使えてしまいます。
#
# 【環境変数の設定方法】GCPコンソール → Cloud Run → 環境変数
#   ALLOWED_EMAILS: "admin@example.com,user1@example.com"
#   ALLOWED_DOMAINS: "@yourcompany.co.jp"
#
# 【注意】両方未設定だと全員許可になります（開発用）

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

    # 設定なし = 全員許可（開発用）
    if not allowed_emails and not allowed_domains:
        print('⚠️ ALLOWED_EMAILS/ALLOWED_DOMAINS 未設定')
        return True
    return False

def get_email_from_token(id_token):
    """JWTトークンからメールアドレス取得【削除禁止】"""
    try:
        payload = id_token.split('.')[1]
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += '=' * padding
        decoded = base64.urlsafe_b64decode(payload).decode('utf-8')
        return json.loads(decoded).get('email')
    except:
        return None

def make_response(body, status=200, content_type='application/json', headers=None):
    """レスポンス作成【削除禁止】"""
    if headers is None:
        headers = {}
    headers['Content-Type'] = content_type
    if content_type == 'application/json' and isinstance(body, dict):
        body = json.dumps(body, ensure_ascii=False)
    return (body, status, headers)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# メインハンドラ【削除禁止】
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# ■ メインハンドラとは？
#   「受付係」のようなもの。ブラウザからのリクエストを最初に受け取り、
#   URLに応じて適切な処理に振り分けます。
#
# ┌─────────────────────────────────────────────────────────────┐
# │  ブラウザ: 「/api/chat に POST でメッセージ送ります」         │
# │       ↓                                                     │
# │  メインハンドラ: 「/api/chat ですね、チャット処理に回します」  │
# │       ↓                                                     │
# │  チャットAPI: 「AIに問い合わせて返答します」                  │
# └─────────────────────────────────────────────────────────────┘
#
# ■ @functions_framework.http とは？
#   「このappという関数がHTTPリクエストを受け取る入口ですよ」という目印。
#   GCPはこの目印を見て、リクエストをこの関数に渡します。
#

@functions_framework.http
def app(request):
    # ┌─────────────────────────────────────────────────────────────┐
    # │ request（リクエスト）= ブラウザから届いた「手紙」            │
    # │   - request.method  → 手紙の種類（GET/POST）               │
    # │   - request.path    → どこ宛て？（/api/chat など）         │
    # │   - request.headers → 封筒の情報（認証トークンなど）       │
    # │   - request.get_json() → 手紙の中身（送られてきたデータ）  │
    # │                                                             │
    # │ 返り値 = ブラウザに返す「返事」                             │
    # │   - (本文, ステータスコード, ヘッダー) の形式で返す         │
    # │   - ステータスコード: 200=成功、404=見つからない、など      │
    # └─────────────────────────────────────────────────────────────┘

    headers = {}
    origin = request.headers.get('Origin', '')

    # セキュリティ設定を返事に追加【削除禁止】
    set_cors_headers(headers, origin)
    set_security_headers(headers)

    # ┌─────────────────────────────────────────────────────────────┐
    # │ プリフライトリクエストとは？【削除禁止】                     │
    # │                                                             │
    # │ ブラウザが本番のリクエストを送る前に                        │
    # │ 「このサーバー、アクセスしていい？」と確認する仕組み        │
    # │                                                             │
    # │ ブラウザ: 「OPTIONSで確認します」                           │
    # │ サーバー: 「204（OK、中身なし）で返事」                     │
    # │ ブラウザ: 「じゃあ本番のPOSTを送ります」                    │
    # └─────────────────────────────────────────────────────────────┘
    if request.method == 'OPTIONS':
        return ('', 204, headers)

    path = request.path

    # ╔═════════════════════════════════════════════════════════════╗
    # ║ 【処理の流れ】ユーザーの操作順に並んでいます                 ║
    # ║                                                             ║
    # ║  1. / (トップページ)     → ユーザーが最初にアクセス         ║
    # ║  1b. /script.js          → フロントエンドのJavaScript       ║
    # ║  2. /api/check-access    → ログイン後、権限を確認           ║
    # ║  3. /api/chat            → メインのチャット機能             ║
    # ║  4. 【新しいAPIを追加】  → 機能拡張はここに                 ║
    # ║  5. /api/health          → 運用監視用（ユーザーは使わない） ║
    # ║  6. 404エラー            → どれにも該当しない場合           ║
    # ╚═════════════════════════════════════════════════════════════╝

    # ---------------------------------------------------------------
    # 1. トップページ表示【削除禁止】
    # → ユーザーが最初にアクセスする画面（ログイン画面が表示される）
    # ---------------------------------------------------------------
    if path == '/' and request.method == 'GET':
        headers['Content-Type'] = 'text/html; charset=utf-8'
        return (HTML_CONTENT, 200, headers)

    # ---------------------------------------------------------------
    # 1b. JavaScript配信【削除禁止】
    # → フロントエンドで使うJavaScript（front.htmlから読み込まれる）
    # ---------------------------------------------------------------
    if path == '/script.js' and request.method == 'GET':
        headers['Content-Type'] = 'application/javascript; charset=utf-8'
        return (SCRIPT_CONTENT, 200, headers)

    # ---------------------------------------------------------------
    # 2. アクセス権限チェック【削除禁止】
    # → ログイン後、このユーザーがアプリを使えるか確認
    # ---------------------------------------------------------------
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

    # ---------------------------------------------------------------
    # 3. ★★★ チャットAPI（ここをカスタマイズ）★★★
    # → メインの機能。AIとチャットする
    # ---------------------------------------------------------------
    if path == '/api/chat' and request.method == 'POST':
        try:
            # --- 認証チェック【削除禁止】---
            auth_header = request.headers.get('Authorization', '')
            if not auth_header.startswith('Bearer '):
                return make_response({'error': 'ログインが必要です'}, 401, headers=headers)

            email = get_email_from_token(auth_header.split('Bearer ')[1])
            if not is_email_allowed(email):
                return make_response({'error': '権限がありません'}, 403, headers=headers)

            # --- 入力チェック【削除禁止】---
            body = request.get_json(silent=True) or {}
            message = body.get('message', '')

            if not message or not isinstance(message, str):
                return make_response({'error': 'メッセージを入力してください'}, 400, headers=headers)
            if len(message) > 10000:
                return make_response({'error': 'メッセージが長すぎます'}, 400, headers=headers)

            # --- AI呼び出し【カスタマイズ可能】---
            client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
            completion = client.chat.completions.create(
                model='gpt-3.5-turbo',  # ← gpt-4 に変更可能
                messages=[{'role': 'user', 'content': message}],
                max_tokens=1000,        # ← 回答の長さ
                temperature=0.7         # ← 0=固定的、1=創造的
            )

            return make_response({'response': completion.choices[0].message.content}, headers=headers)

        except Exception as e:
            print(f'チャットエラー: {e}')
            return make_response({'error': 'AIの処理中にエラーが発生しました'}, 500, headers=headers)

    # ---------------------------------------------------------------
    # 4. 【新しいAPIを追加する場所】
    # → 機能を追加したい場合はここに書く
    #
    # 例: チャット履歴を取得するAPI
    # if path == '/api/history' and request.method == 'GET':
    #     # 認証チェック（上のチャットAPIからコピー）
    #     # 履歴を取得して返す処理
    #     return make_response({'history': [...]}, headers=headers)
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # 5. ヘルスチェック【削除禁止】
    # → サーバーが動いているか確認用（運用監視用、ユーザーは使わない）
    # ---------------------------------------------------------------
    if path == '/api/health' and request.method == 'GET':
        return make_response(
            {'status': 'ok', 'timestamp': datetime.now().isoformat()},
            headers=headers
        )

    # ---------------------------------------------------------------
    # 6. 404エラー【削除禁止】
    # → 上のどれにも該当しないURLにアクセスされた場合
    # ---------------------------------------------------------------
    return make_response({'error': 'ページが見つかりません'}, 404, headers=headers)
