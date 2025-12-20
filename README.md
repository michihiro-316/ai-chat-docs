# AIチャットアプリ構築ガイド

非エンジニア向けのAIチャットアプリ構築手順書です。
2つの構成方法を比較し、目的に応じて選択できます。

---

## 構成比較表

| 項目 | GCP + Firebase | Bolt + Supabase |
|------|----------------|-----------------|
| **構築時間** | 1〜2時間 | **30分〜1時間** |
| **難易度** | ★★★☆☆ | **★★☆☆☆** |
| **管理画面** | 2つ（GCP + Firebase） | **1つ（Supabase）** |
| **月額費用（小規模）** | $5〜30 | **$0（無料枠内）** |
| **スケーラビリティ** | ◎ 大規模対応 | ○ 中規模まで |
| **エンタープライズ** | ◎ | △ |
| **Google Workspace連携** | ◎ | △ |

---

## どちらを選ぶべきか？

### Bolt + Supabase を推奨するケース

- 初めてクラウドサービスを使う
- とにかく早く動くものを作りたい
- コストを最小限に抑えたい（$0〜）
- 小〜中規模のプロジェクト（〜1000人）

### GCP + Firebase を推奨するケース

- 大規模なユーザー数を想定（1000人以上）
- エンタープライズレベルのSLAが必要
- Google Workspaceとの連携が必須
- 将来的な拡張性を重視

---

## フォルダ構成

```
docs/
├── README.md                 # この比較表
├── gcp-firebase/             # GCP + Firebase版
│   ├── 01_構築設計書.md
│   ├── 02_構築手順書.md
│   ├── 03_追加デプロイ手順_費用見積もり.md
│   ├── 99_補足_CloudRun版構築手順.md
│   ├── 99_補足_カスタムドメイン設定.md
│   ├── 99_補足_コンテナイメージとは.md
│   └── 99_補足_サービスアカウントとは.md
│
└── bolt-supabase/            # Bolt + Supabase版
    ├── 01_構築設計書.md
    └── 02_構築手順書.md
```

---

## 費用比較（詳細）

### 月額費用シミュレーション

| 規模 | GCP + Firebase | Bolt + Supabase |
|------|----------------|-----------------|
| 1テナント（〜100人） | $5〜15 | **$0** |
| 1テナント（〜500人） | $10〜30 | **$0** |
| 3テナント | $15〜90 | $0〜25 |
| 5テナント | $25〜150 | $25〜50 |

> **注意**: AI API（OpenAI等）の利用料金は別途発生します。

### 無料枠比較

| 項目 | GCP + Firebase | Supabase + Vercel |
|------|----------------|-------------------|
| 認証 | 月5万人 | 月5万人 |
| バックエンド実行 | 月200万リクエスト | 月50万回 |
| データベース | - | 500MB |
| ストレージ | - | 1GB |
| 帯域幅 | - | 100GB/月 |

---

## 技術スタック比較

### GCP + Firebase

```
フロントエンド: Cloud Run functions内で配信
バックエンド:   Cloud Run functions
認証:          Firebase Authentication
シークレット:   Secret Manager
ホスティング:   Cloud Run
```

### Bolt + Supabase

```
フロントエンド: Vercel（自動デプロイ）
バックエンド:   Supabase Edge Functions
認証:          Supabase Auth
シークレット:   Supabase Vault
データベース:   PostgreSQL（Supabase）
```

---

## 学習リソース

### GCP + Firebase

- [Firebase公式ドキュメント](https://firebase.google.com/docs?hl=ja)
- [Cloud Run公式ドキュメント](https://cloud.google.com/run/docs?hl=ja)

### Bolt + Supabase

- [Supabase公式ドキュメント](https://supabase.com/docs)
- [Bolt.new公式サイト](https://bolt.new)
- [Vercel公式ドキュメント](https://vercel.com/docs)

---

## 作成日

2025年12月
