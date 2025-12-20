# 02. 構築手順書（Bolt + Supabase版）

| 項目 | 内容 |
|------|------|
| 対象者 | 非エンジニア |
| 作業時間 | 約30分〜1時間 |

---

## 事前準備チェック

- [ ] Googleアカウント
- [ ] GitHubアカウント（無料で作成可能）
- [ ] AIのAPIキー（OpenAI等）

---

## 全体構成

### 仕組みの概要

```
あなた（ブラウザ）
    |
    | (1) Bolt.newでアプリを作成
    v
Bolt.new（AI開発ツール）
    |
    | (2) 自動でコード生成 & GitHub連携
    v
GitHub（コード管理）
    |
    | (3) 自動デプロイ
    v
Vercel（フロントエンド配信）
    |
    | (4) API呼び出し
    v
Supabase Edge Functions
    |
    | (5) APIキー取得 & AI呼び出し
    v
OpenAI API（ChatGPT）
```

### 何を作るか

| 作るもの | 役割 | 作業 |
|----------|------|------|
| Supabaseプロジェクト | 認証 + バックエンド | 設定のみ |
| Bolt.newプロジェクト | フロントエンド生成 | AIに指示するだけ |
| Vercelデプロイ | ホスティング | 自動 |

> **コストについて**
>
> | サービス | 無料枠 |
> |----------|--------|
> | Supabase | 500MB DB、50,000ユーザー、500,000 Edge Functions |
> | Vercel | 100GB帯域/月 |
> | Bolt.new | 月間トークン制限あり（無料プラン） |
> | **OpenAI API** | **無料枠なし（従量課金）** |

---

## Step 1: Supabaseプロジェクト作成（10分）

### 1-1. Supabaseアカウント作成

1. `https://supabase.com` にアクセス

2. 「**Start your project**」をクリック

3. 「**Continue with GitHub**」をクリック
   - GitHubアカウントでログイン（推奨）
   - または「Continue with email」でメール登録

4. GitHubとの連携を許可

### 1-2. プロジェクト作成

1. ダッシュボードで「**New project**」をクリック

2. 設定を入力:

   | 項目 | 入力値 |
   |------|--------|
   | Organization | 自分のOrg（自動作成されている） |
   | Name | `ai-chat-app`（任意） |
   | Database Password | 強力なパスワードを設定（**メモ必須**） |
   | Region | `Northeast Asia (Tokyo)` |
   | Pricing Plan | Free |

3. 「**Create new project**」をクリック

4. プロジェクト作成完了まで待機（1〜2分）

---

## Step 2: Supabase認証設定（5分）

### 2-1. Google認証を有効化

1. 左メニュー「**Authentication**」をクリック

2. 「**Providers**」タブをクリック

3. 「**Google**」を探してクリック

4. 「**Enable Google provider**」をオン

5. Google Cloud ConsoleでOAuth設定:
   - `https://console.cloud.google.com` にアクセス
   - 「APIとサービス」→「認証情報」
   - 「認証情報を作成」→「OAuthクライアントID」
   - アプリケーションの種類：「ウェブアプリケーション」
   - 承認済みリダイレクトURI：Supabaseに表示されるURLを入力

6. 取得したClient IDとClient SecretをSupabaseに入力

7. 「**Save**」をクリック

> **簡単な方法**
>
> Supabaseの「Magic Link」（メール認証）を使えば、Google設定なしで認証できます。
> 初めての場合はこちらがおすすめです。

---

## Step 3: Vault設定（APIキー保存）（5分）

### 3-1. シークレット作成

1. 左メニュー「**Project Settings**」（歯車アイコン）

2. 「**Vault**」をクリック

3. 「**Add new secret**」をクリック

4. 設定を入力:

   | 項目 | 入力値 |
   |------|--------|
   | Name | `openai_api_key` |
   | Secret | OpenAIのAPIキーを貼り付け |

5. 「**Save**」をクリック

---

## Step 4: Edge Function作成（10分）

### 4-1. Supabase CLIインストール（オプション）

CLIを使わない場合は、ダッシュボードから直接作成できます。

### 4-2. ダッシュボードから作成

1. 左メニュー「**Edge Functions**」をクリック

2. 「**Create a new function**」をクリック

3. 関数名: `chat`

4. 以下のコードを貼り付け:

```typescript
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
  // CORS対応
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    // 認証チェック
    const supabaseClient = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_ANON_KEY') ?? '',
      { global: { headers: { Authorization: req.headers.get('Authorization')! } } }
    )

    const { data: { user } } = await supabaseClient.auth.getUser()
    if (!user) {
      return new Response(JSON.stringify({ error: 'Unauthorized' }), {
        status: 401,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      })
    }

    // リクエスト取得
    const { message } = await req.json()

    // OpenAI API呼び出し
    const openaiKey = Deno.env.get('OPENAI_API_KEY')
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${openaiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: message }],
      }),
    })

    const data = await response.json()

    return new Response(JSON.stringify({
      reply: data.choices[0].message.content
    }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    })

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    })
  }
})
```

5. 「**Deploy**」をクリック

### 4-3. 環境変数設定

1. Edge Functionsページで作成した関数をクリック

2. 「**Manage secrets**」をクリック

3. `OPENAI_API_KEY` を追加（Vaultから参照）

---

## Step 5: Bolt.newでフロントエンド作成（10分）

### 5-1. Bolt.newにアクセス

1. `https://bolt.new` にアクセス

2. GitHubでログイン

### 5-2. AIにアプリ生成を指示

プロンプト例:

```
Supabaseと連携したAIチャットアプリを作成してください。

要件:
- Supabase Authでログイン機能（Googleログイン）
- ログイン後にチャット画面を表示
- チャットはSupabase Edge Functions経由でOpenAI APIを呼び出し
- シンプルでモダンなUI（Tailwind CSS使用）
- レスポンシブデザイン

Supabase設定:
- URL: [SupabaseダッシュボードのProject URL]
- Anon Key: [SupabaseダッシュボードのAnon Key]
```

3. AIがコードを生成するのを待つ

4. 生成されたアプリをプレビューで確認

### 5-3. Supabase接続情報の確認

Supabaseダッシュボード → Project Settings → API で確認:

| 項目 | 場所 |
|------|------|
| Project URL | `https://xxxxx.supabase.co` |
| Anon Key | `eyJhbGci...` |

---

## Step 6: デプロイ（5分）

### 6-1. GitHubにプッシュ

1. Bolt.newの「**Deploy**」ボタンをクリック

2. GitHubリポジトリを作成（または既存を選択）

3. プッシュ完了を待つ

### 6-2. Vercelにデプロイ

1. `https://vercel.com` にアクセス

2. 「**Add New Project**」をクリック

3. 先ほど作成したGitHubリポジトリを選択

4. 「**Deploy**」をクリック

5. デプロイ完了を待つ（1〜2分）

6. 発行されたURLをメモ
   - 例: `https://ai-chat-app.vercel.app`

---

## Step 7: 認証リダイレクトURL設定

### 7-1. Supabase側の設定

1. Supabaseダッシュボード → Authentication → URL Configuration

2. 「**Site URL**」にVercelのURLを設定
   - 例: `https://ai-chat-app.vercel.app`

3. 「**Redirect URLs**」に追加:
   - `https://ai-chat-app.vercel.app/**`

---

## Step 8: 動作確認

### 8-1. アクセス確認

| URL | 期待する結果 |
|-----|--------------|
| `https://[Vercel URL]/` | ログイン画面が表示 |

### 8-2. ログインテスト

1. 「Googleでログイン」をクリック

2. Googleアカウントを選択

3. ログイン成功後、チャット画面が表示

### 8-3. チャットテスト

1. メッセージを入力

2. 送信ボタンをクリック

3. AIからの回答が表示されれば成功

---

## 完了チェック

- [ ] VercelのURLにアクセスできる
- [ ] ログイン画面が表示される
- [ ] Googleアカウントでログインできる
- [ ] チャットでAIと会話できる
- [ ] HTTPSで接続されている（鍵マーク）

---

## トラブルシューティング

### ログインできない

- Supabaseの「Redirect URLs」にVercelのURLを追加したか確認
- Google OAuth設定のリダイレクトURIを確認

### チャットでエラーが出る

- Edge FunctionsにOPENAI_API_KEYが設定されているか確認
- Supabase Edge Functionsのログを確認

### 「Unauthorized」エラー

- ログイン状態が正しく保持されているか確認
- ブラウザのCookieをクリアして再試行

---

## 重要なURL

| サービス | URL |
|----------|-----|
| Supabaseダッシュボード | `https://supabase.com/dashboard` |
| Vercelダッシュボード | `https://vercel.com/dashboard` |
| Bolt.new | `https://bolt.new` |
| OpenAI APIキー取得 | `https://platform.openai.com/api-keys` |
