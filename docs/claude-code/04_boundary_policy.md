# 04_boundary_policy.md

境界（API、認証、フロント↔バック）の型管理方針を定義します。

## 内容

```markdown
# 境界と型管理方針

内部処理は柔軟に書く。
境界のみ構造を明示する。

境界：
- API Request / Response
- 認証・認可
- フロント ↔ バック

TypedDict 等を使用し、
目的は可読性と説明責任。
```

## 解説

### 境界とは

システムの「つなぎ目」を指します。

```
[フロント] ←境界→ [バックエンド] ←境界→ [外部API]
```

### なぜ境界だけ厳密にするのか

| 内部処理 | 境界 |
|---------|------|
| 柔軟に書いてよい | 型を明示する |
| リファクタリング自由 | 変更時は合意が必要 |
| 実装者の裁量 | 契約として扱う |

### 実装例

```python
from typing import TypedDict

class ChatRequest(TypedDict):
    message: str
    user_id: str

class ChatResponse(TypedDict):
    reply: str
    timestamp: str
```

### 目的

- 可読性：何を送って何が返るか一目でわかる
- 説明責任：「この形式で通信する」と断言できる
- 保守性：境界の変更を検知しやすい
