# Cloud Run（サービス）版構築手順（Dockerイメージパターン）

> この資料は、Cloud Run（サービス）を使用してバックエンドをデプロイする場合の手順です。
> Dockerイメージを使用するため、ローカルでのDocker環境またはCloud Buildが必要です。
>
> **シンプルな構成にはCloud Run functions版（02_構築手順書.md）を推奨します。**

---

## Cloud Run（サービス）とは

**自分のアプリをGoogleのサーバーで動かすサービス**です。

```
従来の方法:
自分でサーバーを借りる → OSをインストール → Pythonを入れる → アプリを設置 → 運用管理...

Cloud Run:
アプリをアップロード → Googleが全部やってくれる → 動いた！
```

| 項目 | 説明 |
|------|------|
| 何ができる？ | Webアプリやバックエンド（API）を動かせる |
| 管理は？ | サーバー管理不要（Googleが自動でやる） |
| 料金は？ | 使った分だけ（アクセスがなければほぼ無料） |
| 必要なもの | **コンテナイメージ**（アプリのパッケージ） |

---

## Cloud Run（サービス）vs Cloud Run functions

> **名称について**
> 以前は「Cloud Functions」という名前でしたが、現在は「Cloud Run functions」に名称変更されています。
> 本資料では「Cloud Run（サービス）」と「Cloud Run functions」を区別して説明します。

| 項目 | Cloud Run（サービス） | Cloud Run functions |
|------|----------------------|---------------------|
| デプロイ方法 | Dockerイメージが必要 | コードだけでOK |
| 環境構築 | Docker or Cloud Build必要 | GCPコンソールから直接可能 |
| 適したケース | 複雑なアプリ、長時間処理 | シンプルなAPI、イベント駆動 |
| コールドスタート | やや長い | 短い |
| カスタマイズ性 | 高い（OS、ライブラリ自由） | 制限あり |

---

## 前提条件

以下のいずれかが必要：
- ローカルPCにDockerがインストールされている
- または、Cloud Buildを使用する（GCPで課金が発生）

---

## Step 1: サービスアカウント作成

1. GCPコンソール →「IAMと管理」→「サービスアカウント」
2. 「サービスアカウントを作成」
3. 名前: `sa-tenant-a` → 「作成して続行」
4. ロールの付与は**スキップ**→「完了」

---

## Step 2: APIキー保存（Secret Manager）

1. GCPコンソール →「Secret Manager」→「シークレットを作成」
2. 名前: `tenant-a-openai-key`
3. 値: APIキーを入力 →「シークレットを作成」
4. 作成したシークレット →「権限」→「アクセスを許可」
5. プリンシパル: `sa-tenant-a@[PROJECT_ID].iam.gserviceaccount.com`
6. ロール:「Secret Manager のシークレット アクセサー」→「保存」

---

## Step 3: Cloud Runサービス作成

### 3-1. テスト用イメージでの作成（環境確認用）

1. GCPコンソール →「Cloud Run」→「サービスを作成」
2. コンテナイメージ: `gcr.io/cloudrun/hello`（テスト用）
3. サービス名: `ai-platform-tenant-a`
4. リージョン: `asia-northeast1`（東京）
5. 認証:「**公開アクセスを許可する**」を選択
6. 「コンテナ、ボリューム、ネットワーキング、セキュリティ」を展開

#### コンテナ設定

| 項目 | 設定値 | 説明 |
|------|--------|------|
| メモリ | 1 GiB | アプリが使用できるメモリ量 |
| CPU | 1 | 処理能力 |
| リクエストタイムアウト | 300秒 | 1リクエストの最大処理時間 |

#### インスタンス設定

| 項目 | 設定値 | 説明 |
|------|--------|------|
| 最小インスタンス数 | 0 | アクセスがない時に起動しておく数 |
| 最大インスタンス数 | 10 | 同時に起動できる上限 |

#### セキュリティ設定

| 項目 | 設定値 |
|------|--------|
| サービスアカウント | `sa-tenant-a` |

7. 「作成」→ 緑チェックが出たら成功

### 3-2. シークレット紐付け

1. 作成したCloud Runサービス →「新しいリビジョンを編集してデプロイ」
2. 「変数とシークレット」→「＋シークレットを参照」
3. 以下を設定:

| 項目 | 設定値 |
|------|--------|
| 名前1 | `OPENAI_API_KEY` |
| シークレット | `tenant-a-openai-key` |
| バージョン | `latest` |

4. 「完了」→「デプロイ」

---

## Step 4: 本番用バックエンドのデプロイ

テスト用イメージ（`gcr.io/cloudrun/hello`）を自作のバックエンドに置き換えます。

### 必要なファイル

**backend/main.py**
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )

    return jsonify({
        'response': response.choices[0].message.content
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

**backend/requirements.txt**
```
flask==3.0.0
flask-cors==4.0.0
openai==1.6.1
gunicorn==21.2.0
```

**backend/Dockerfile**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
```

### デプロイ方法A: ローカルDocker使用

```bash
# 1. Dockerイメージをビルド
cd backend
docker build -t gcr.io/[PROJECT_ID]/ai-backend:latest .

# 2. Container Registryにプッシュ
docker push gcr.io/[PROJECT_ID]/ai-backend:latest

# 3. Cloud Runを更新
gcloud run deploy ai-platform-tenant-a \
  --image gcr.io/[PROJECT_ID]/ai-backend:latest \
  --region asia-northeast1
```

### デプロイ方法B: Cloud Build使用（Docker不要）

```bash
# backendディレクトリで実行
gcloud builds submit --tag gcr.io/[PROJECT_ID]/ai-backend:latest

# Cloud Runを更新
gcloud run deploy ai-platform-tenant-a \
  --image gcr.io/[PROJECT_ID]/ai-backend:latest \
  --region asia-northeast1
```

---

## コンテナイメージとは

アプリを動かすための「完成品パッケージ」です。

```
┌─────────────────────────────────┐
│       コンテナイメージ            │
├─────────────────────────────────┤
│  OS（Linux等）                   │
│  実行環境（Python / Node.js 等） │
│  ライブラリ（Flask, React等）    │
│  あなたのコード（main.py等）      │
│  設定ファイル                    │
└─────────────────────────────────┘
```

### Dockerとコンテナイメージの関係

| 用語 | 説明 |
|------|------|
| Docker | コンテナを作る・動かすためのツール |
| Dockerfile | イメージの設計図 |
| コンテナイメージ | 完成したパッケージ |
| コンテナ | イメージを実行している状態 |

---

## インスタンス設定の考え方

### よくある誤解: 最大10 = 10人しかアクセスできない？

**いいえ、1インスタンスで複数人のリクエストを処理できます。**

```
1インスタンスあたり約80リクエスト/秒を処理可能（デフォルト設定）

最大インスタンス数=10 の場合:
→ 10インスタンス × 80 = 約800リクエスト/秒まで対応可能
→ 同時に数百〜数千人がアクセスしても問題なし
```

### 最小インスタンス数の考え方

| 設定 | メリット | デメリット |
|------|---------|-----------|
| 最小=0 | コスト削減 | 初回アクセスが遅い（2-5秒） |
| 最小=1以上 | 常に高速応答 | 常時課金が発生 |

---

## サービスアカウントとシークレットの関係

```
例: sa-tenant-a が以下すべてにアクセス可能な場合

Secret Manager:
├── tenant-a-openai-key    ← Cloud Runで選択 → 使用する
├── tenant-a-claude-key    ← 選択しない → 使用しない
└── tenant-a-backup-key    ← 選択しない → 使用しない
```

| 設定 | 役割 |
|------|------|
| サービスアカウント | Secret Managerにアクセスする**権限** |
| シークレット紐付け | **どのシークレット**を使うか＋環境変数名 |
