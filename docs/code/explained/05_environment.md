# 環境変数と.envファイル

「`import os` は GCP限定？」「`.env` ファイルって何？」という疑問に答えます。

---

## 環境変数とは？

**環境変数 = パソコン（サーバー）に設定された「名前付きの値」**

!!! example "自分のパソコンにも環境変数がある"

    | 名前 | 値 |
    |------|-----|
    | `USERNAME` | tanaka |
    | `HOME` | /Users/tanaka |
    | `PATH` | /usr/bin:/usr/local/bin |

    - **Windows**: 「システムの詳細設定」→「環境変数」で見れる
    - **Mac/Linux**: ターミナルで `env` コマンドで見れる

---

## `import os` は GCP限定ではない！

**結論：`os` はPython標準ライブラリで、どこでも使える**

```python
import os

# どのパソコンでも動く
username = os.environ.get('USERNAME')  # ユーザー名を取得
home = os.environ.get('HOME')          # ホームディレクトリを取得
```

### 各環境での動作

| 環境 | `os.environ.get()` が読む場所 |
|------|------------------------------|
| 自分のPC（ローカル） | PCの環境変数 |
| GCP Cloud Run | GCPコンソールで設定した環境変数 |
| AWS Lambda | AWSコンソールで設定した環境変数 |
| Heroku | Heroku設定画面の環境変数 |
| Docker | `docker run -e` で渡した環境変数 |

**つまり：`os.environ` はどこでも動くが、値の「設定場所」が環境ごとに違う**

---

## ローカル開発での問題

!!! warning "問題：ローカルで開発したい"

    **コード:**
    ```python
    api_key = os.environ.get('OPENAI_API_KEY')
    ```

    **でも...**

    - 自分のPCには `OPENAI_API_KEY` が設定されていない！
    - `None` が返ってきてエラーになる

    **解決策:**

    1. PCに環境変数を設定する（面倒）
    2. **.env ファイルを使う（簡単！）** ← これがおすすめ

---

## .env ファイルとは？

**.env ファイル = 環境変数を書いておくテキストファイル**

### ファイルの例

```bash
# .env ファイルの中身
OPENAI_API_KEY=sk-abc123def456...
ALLOWED_EMAILS=tanaka@example.com,yamada@test.com
ALLOWED_DOMAINS=@yourcompany.co.jp
```

### 特徴

| 特徴 | 説明 |
|------|------|
| ファイル名 | `.env`（ドットで始まる） |
| 場所 | プロジェクトのルートフォルダ |
| 形式 | `名前=値` を1行ずつ書く |
| コメント | `#` で始まる行はコメント |

---

## .env ファイルの使い方

### Python の場合

```python
# 1. ライブラリをインストール
#    pip install python-dotenv

# 2. コードで読み込む
from dotenv import load_dotenv
import os

# .env ファイルを読み込む
load_dotenv()

# 環境変数として使える！
api_key = os.environ.get('OPENAI_API_KEY')
print(api_key)  # → sk-abc123def456...
```

### Node.js の場合

```javascript
// 1. ライブラリをインストール
//    npm install dotenv

// 2. コードで読み込む
require('dotenv').config();

// 環境変数として使える！
const apiKey = process.env.OPENAI_API_KEY;
console.log(apiKey);  // → sk-abc123def456...
```

---

## なぜ .env ファイルを使う？

!!! success "メリット"

    1. **秘密情報をコードに書かなくて済む** → GitHubに公開しても安全
    2. **環境ごとに値を変えられる** → ローカル用、テスト用、本番用を分けられる
    3. **設定変更がコード変更なしでできる** → .env を書き換えるだけ

!!! danger "重要：.env は公開しない！"

    **.gitignore に追加する**

    ```
    # .gitignore の中身
    .env
    .env.local
    .env.*.local
    ```

    これにより、.env は Git で追跡されず、GitHubにアップロードされない

---

## 環境変数の設定場所まとめ

!!! info "ローカル開発"

    **.env ファイル**

    ```
    OPENAI_API_KEY=sk-abc123...
    ALLOWED_EMAILS=tanaka@example.com
    ```

    ↓ `load_dotenv()` で読み込み

    ```python
    os.environ.get('OPENAI_API_KEY')
    ```

!!! info "GCP Cloud Run"

    **GCPコンソール → Cloud Run → 環境変数**

    | 名前 | 値 |
    |------|-----|
    | `OPENAI_API_KEY` | sk-abc123... |

    ↓ 自動で設定される

    ```python
    os.environ.get('OPENAI_API_KEY')
    ```

!!! info "GCP Secret Manager（より安全）"

    - 機密情報を暗号化して保存
    - Cloud Run から参照可能
    - アクセス権限を細かく制御

---

## Python版 vs Node.js版 の違い

### 環境変数の読み方

=== "Python"

    ```python
    import os

    # 環境変数を取得
    api_key = os.environ.get('OPENAI_API_KEY')

    # デフォルト値を指定（見つからなかった場合）
    api_key = os.environ.get('OPENAI_API_KEY', 'default_value')
    ```

=== "Node.js"

    ```javascript
    // 環境変数を取得
    const apiKey = process.env.OPENAI_API_KEY;

    // デフォルト値を指定（見つからなかった場合）
    const apiKey = process.env.OPENAI_API_KEY || 'default_value';
    ```

### .env ファイルの読み込み

=== "Python"

    ```python
    # ライブラリ: python-dotenv
    from dotenv import load_dotenv
    load_dotenv()  # .env を読み込む
    ```

=== "Node.js"

    ```javascript
    // ライブラリ: dotenv
    require('dotenv').config();  // .env を読み込む
    ```

---

## このアプリでの使い方

### GCP Cloud Run にデプロイする場合

```
【.env ファイルは不要】

GCPコンソールで環境変数を設定すれば、
コードはそのまま動く。

┌─────────────────────────────────────────┐
│ GCPコンソール → Cloud Run → 環境変数    │
├─────────────────────────────────────────┤
│ OPENAI_API_KEY    sk-abc123...         │
│ ALLOWED_EMAILS    tanaka@example.com   │
└─────────────────────────────────────────┘
```

### ローカルで開発する場合

```
【.env ファイルを使う】

1. プロジェクトルートに .env ファイルを作成
2. 必要な環境変数を記入
3. コードに load_dotenv() を追加

※ 本番コードでは load_dotenv() は不要
  （GCPが自動で環境変数を設定するため）
```

---

## よくある質問

### Q: .env ファイルを Git にコミットしてしまった！

**A: すぐに以下を実行**

```bash
# 1. .env を .gitignore に追加
echo ".env" >> .gitignore

# 2. Git から削除（ファイル自体は残す）
git rm --cached .env

# 3. コミット
git commit -m "Remove .env from tracking"

# 4. APIキーを再発行（漏れた可能性があるため）
```

### Q: 本番環境で .env を使ってもいい？

**A: 推奨しない**

- .env ファイルはローカル開発用
- 本番環境では各サービスの環境変数設定を使う
- より安全な Secret Manager などを検討

### Q: .env.example って何？

**A: 設定項目のテンプレート**

```bash
# .env.example（Git にコミットしてOK）
OPENAI_API_KEY=your_api_key_here
ALLOWED_EMAILS=your_email@example.com

# 使い方
# 1. .env.example をコピーして .env を作成
# 2. 実際の値を入力
```

---

## まとめ

| 項目 | 説明 |
|------|------|
| `os` / `process.env` | どの環境でも使える標準機能 |
| 環境変数 | コードの外に置く設定値 |
| .env ファイル | ローカル開発用の環境変数ファイル |
| 本番環境 | 各サービスの設定画面で環境変数を設定 |
| 重要 | .env は .gitignore に追加して公開しない |

!!! success "覚えること"

    1. **`import os` は GCP 限定ではなく、どこでも使える**
    2. 値の「設定場所」が環境ごとに違うだけ
        - ローカル → .env ファイル
        - GCP → GCPコンソールの環境変数
    3. **.env ファイルは秘密情報を含むので Git に含めない**
