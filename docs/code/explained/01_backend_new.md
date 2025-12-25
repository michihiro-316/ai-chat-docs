# backend.py 隧ｳ邏ｰ隗｣隱ｬ

縺薙・繝輔ぃ繧､繝ｫ縺ｯ繧ｵ繝ｼ繝舌・蛛ｴ縺ｮ蜃ｦ逅・ｒ諡・ｽ薙＠縺ｾ縺吶ゅ悟耳謌ｿ縺ｮ繧ｷ繧ｧ繝輔阪・繧医≧縺ｪ蠖ｹ蜑ｲ縺ｧ縺吶・

**縺薙・繝峨く繝･繝｡繝ｳ繝医〒縺ｯ縲￣ython縺ｮ蝓ｺ遉取ｧ区枚縺九ｉ荳∝ｯｧ縺ｫ隗｣隱ｬ縺励∪縺吶・*

---

## 逶ｮ谺｡ { data-toc-skip }

1. [Python蝓ｺ遉趣ｼ壹％繧後□縺題ｦ壹∴繧医≧](#1-python蝓ｺ遉弱％繧後□縺題ｦ壹∴繧医≧)
2. [繝ｩ繧､繝悶Λ繝ｪ隱ｭ縺ｿ霎ｼ縺ｿ](#2-繝ｩ繧､繝悶Λ繝ｪ隱ｭ縺ｿ霎ｼ縺ｿ)
3. [險ｭ螳夐Κ蛻・(#3-險ｭ螳夐Κ蛻・
4. [繝倥Ν繝代・髢｢謨ｰ](#4-繝倥Ν繝代・髢｢謨ｰ)
5. [繧｢繧ｯ繧ｻ繧ｹ蛻ｶ蠕｡](#5-繧｢繧ｯ繧ｻ繧ｹ蛻ｶ蠕｡)
6. [繝｡繧､繝ｳ繝上Φ繝峨Λ](#6-繝｡繧､繝ｳ繝上Φ繝峨Λ)

---

## 1. Python蝓ｺ遉趣ｼ壹％繧後□縺題ｦ壹∴繧医≧

繧ｳ繝ｼ繝峨ｒ隱ｭ繧蜑阪↓縲∝ｿ・ｦ√↑Python讒区枚繧定ｧ｣隱ｬ縺励∪縺吶・

### 1-1. 霎樊嶌・・ictionary・峨→縺ｯ・・

**霎樊嶌 = 縲悟錐蜑阪阪→縲悟､縲阪・繝壹い繧剃ｿ晏ｭ倥☆繧九ｂ縺ｮ**

```python
# 霎樊嶌繧剃ｽ懊ｋ
person = {
    'name': '逕ｰ荳ｭ',
    'age': 25,
    'email': 'tanaka@example.com'
}

# 蛟､繧貞叙繧雁・縺・
print(person['name'])   # 竊・逕ｰ荳ｭ
print(person['age'])    # 竊・25

# 蛟､繧定ｿｽ蜉繝ｻ螟画峩縺吶ｋ
person['phone'] = '090-1234-5678'  # 霑ｽ蜉
person['age'] = 26                  # 螟画峩
```

!!! tip "繧､繝｡繝ｼ繧ｸ・夊ｾ樊嶌 = 蠑輔″蜃ｺ縺励↓蜷榊燕繝ｩ繝吶Ν縺後▽縺・◆譽・

    | 繝ｩ繝吶Ν・医く繝ｼ・・| name | age | email |
    |---------------|------|-----|-------|
    | 荳ｭ霄ｫ・亥､・・| 逕ｰ荳ｭ | 25 | tanaka@.. |

    `person['name']` 竊・縲系ame繝ｩ繝吶Ν縺ｮ蠑輔″蜃ｺ縺励ｒ髢九￠縺ｦ荳ｭ霄ｫ繧定ｦ九ｋ縲・

**縺薙・繧ｳ繝ｼ繝峨〒縺ｮ菴ｿ繧上ｌ譁ｹ**
```python
# headers 縺ｨ縺・≧霎樊嶌縺ｫ蛟､繧定ｿｽ蜉縺励※縺・￥
headers = {}  # 遨ｺ縺ｮ霎樊嶌繧剃ｽ懊ｋ
headers['Content-Type'] = 'text/html'  # 霑ｽ蜉
headers['X-Frame-Options'] = 'DENY'    # 霑ｽ蜉

# 邨先棡
# headers = {
#     'Content-Type': 'text/html',
#     'X-Frame-Options': 'DENY'
# }
```

---

### 1-2. in 貍皮ｮ怜ｭ・

**in = 縲後懊・荳ｭ縺ｫ蜷ｫ縺ｾ繧後ｋ・溘阪ｒ遒ｺ隱阪☆繧・*

```python
# 繝ｪ繧ｹ繝茨ｼ磯・蛻暦ｼ峨〒縺ｮ菴ｿ逕ｨ
fruits = ['繧翫ｓ縺・, '縺ｿ縺九ｓ', '縺ｶ縺ｩ縺・]

'繧翫ｓ縺・ in fruits    # 竊・True・亥性縺ｾ繧後ｋ・・
'繝舌リ繝・ in fruits    # 竊・False・亥性縺ｾ繧後↑縺・ｼ・

# 譁・ｭ怜・縺ｧ縺ｮ菴ｿ逕ｨ
email = 'tanaka@example.com'

'@' in email          # 竊・True・・縺悟性縺ｾ繧後ｋ・・
'@example.com' in email  # 竊・True
'@test.com' in email     # 竊・False
```

**if譁・〒縺ｮ菴ｿ縺・婿**
```python
allowed_list = ['tanaka@example.com', 'yamada@test.com']
email = 'tanaka@example.com'

if email in allowed_list:
    print('險ｱ蜿ｯ縺輔ｌ縺ｦ縺・∪縺・)
else:
    print('險ｱ蜿ｯ縺輔ｌ縺ｦ縺・∪縺帙ｓ')

# 竊・險ｱ蜿ｯ縺輔ｌ縺ｦ縺・∪縺・
```

---

### 1-3. `or` 縺ｨ縺ｯ・・

**`or` = 縲後∪縺溘・縲搾ｼ医←縺｡繧峨°縺卦rue縺ｪ繧欝rue・・*

```python
# 譚｡莉ｶ縺ｧ縺ｮ菴ｿ逕ｨ
age = 20
is_student = True

if age >= 18 or is_student:
    print('OK')  # 縺ｩ縺｡繧峨°縺卦rue縺ｪ縺ｮ縺ｧOK

# 竊・OK
```

**蛟､縺ｮ驕ｸ謚槭〒縺ｮ菴ｿ逕ｨ・医％繧後′驥崎ｦ・ｼ・ｼ・*
```python
# 縲悟､ or 繝・ヵ繧ｩ繝ｫ繝亥､縲阪→縺・≧譖ｸ縺肴婿
name = None
result = name or '蜷咲┌縺・
print(result)  # 竊・'蜷咲┌縺・

name = '逕ｰ荳ｭ'
result = name or '蜷咲┌縺・
print(result)  # 竊・'逕ｰ荳ｭ'
```

!!! info "莉慕ｵ・∩・哂 or B 縺ｮ蜍輔″"

    1. 縺ｾ縺・A 繧堤｢ｺ隱・
    2. A 縺後後≠繧九搾ｼ・rue逶ｸ蠖難ｼ峨↑繧・竊・**A 繧定ｿ斐☆**
    3. A 縺後後↑縺・搾ｼ・alse逶ｸ蠖難ｼ峨↑繧・竊・**B 繧定ｿ斐☆**

    **萓具ｼ・*

    - `origin = None` 縺ｮ蝣ｴ蜷茨ｼ啻origin or '*'` 竊・`'*'` 繧定ｿ斐☆
    - `origin = 'https://example.com'` 縺ｮ蝣ｴ蜷茨ｼ啻origin or '*'` 竊・`'https://example.com'` 繧定ｿ斐☆

---

### 1-4. `with open()` 縺ｨ縺ｯ・・

**`with open()` = 繝輔ぃ繧､繝ｫ繧貞ｮ牙・縺ｫ髢九＞縺ｦ隱ｭ繧譁ｹ豕・*

```python
with open('front.html', 'r', encoding='utf-8') as f:
    content = f.read()
```

!!! note "蜷・Κ蛻・・諢丞袖"

    ```
    with open('front.html', 'r', encoding='utf-8') as f:
    ```

    | 驛ｨ蛻・| 諢丞袖 |
    |------|------|
    | `open` | 繝輔ぃ繧､繝ｫ繧帝幕縺城未謨ｰ |
    | `'front.html'` | 繝輔ぃ繧､繝ｫ蜷・|
    | `'r'` | read・郁ｪｭ縺ｿ蜿悶ｊ・・|
    | `encoding='utf-8'` | 譁・ｭ励さ繝ｼ繝会ｼ域律譛ｬ隱槫ｯｾ蠢懶ｼ・|
    | `as f` | 螟画焚蜷搾ｼ井ｽ輔〒繧０K・・|

    ```
    content = f.read()
    ```

    - `f.read()` 竊・繝輔ぃ繧､繝ｫ縺ｮ荳ｭ霄ｫ繧貞・驛ｨ隱ｭ繧
    - `content` 竊・隱ｭ繧薙□蜀・ｮｹ繧貞､画焚縺ｫ菫晏ｭ・

**縺ｪ縺・`with` 繧剃ｽｿ縺・ｼ・*
```python
# 謔ｪ縺・ｾ具ｼ医ヵ繧｡繧､繝ｫ繧帝哩縺伜ｿ倥ｌ繧句庄閭ｽ諤ｧ・・
f = open('file.txt', 'r')
content = f.read()
f.close()  # 髢峨§蠢倥ｌ繧九→蝠城｡後′襍ｷ縺阪ｋ・・

# 濶ｯ縺・ｾ具ｼ・ith繧剃ｽｿ縺・→閾ｪ蜍輔〒髢峨§縺ｦ縺上ｌ繧具ｼ・
with open('file.txt', 'r') as f:
    content = f.read()
# 竊・縺薙％縺ｧ閾ｪ蜍慕噪縺ｫ繝輔ぃ繧､繝ｫ縺碁哩縺倥ｉ繧後ｋ
```

!!! example "繧､繝｡繝ｼ繧ｸ・嗹ith = 閾ｪ蜍輔〒迚・ｻ倥￠縺ｦ縺上ｌ繧倶ｻ慕ｵ・∩"

    **萓具ｼ壼・阡ｵ蠎ｫ繧帝幕縺代※鬟滓攝繧貞叙繧雁・縺・*

    | 譁ｹ豕・| 豬√ｌ |
    |------|------|
    | 譎ｮ騾・| 蜀ｷ阡ｵ蠎ｫ繧帝幕縺代ｋ 竊・鬟滓攝繧貞叙繧・竊・**髢峨ａ蠢倥ｌ繧具ｼ・* |
    | with | 蜀ｷ阡ｵ蠎ｫ繧帝幕縺代ｋ 竊・鬟滓攝繧貞叙繧・竊・**閾ｪ蜍輔〒髢峨∪繧・* |

---

### 1-5. Base64繧ｨ繝ｳ繧ｳ繝ｼ繝峨・繝・さ繝ｼ繝峨→縺ｯ・・

- **繧ｨ繝ｳ繧ｳ繝ｼ繝・* = 繝・・繧ｿ繧貞挨縺ｮ蠖｢蠑上↓螟画鋤縺吶ｋ縺薙→
- **繝・さ繝ｼ繝・* = 螟画鋤縺輔ｌ縺溘ョ繝ｼ繧ｿ繧貞・縺ｫ謌ｻ縺吶％縺ｨ

!!! example "譌･蟶ｸ縺ｮ萓具ｼ壽囓蜿ｷ縺斐▲縺・

    | 繧ｹ繝・ャ繝・| 繝・・繧ｿ |
    |---------|--------|
    | 蜈・・繝｡繝・そ繝ｼ繧ｸ | 縲後％繧薙↓縺｡縺ｯ縲・|
    | 竊・繧ｨ繝ｳ繧ｳ繝ｼ繝会ｼ亥､画鋤・・| |
    | 螟画鋤蠕・| `44GT44KT44Gr44Gh44Gv` 竊・隱ｭ繧√↑縺・ｼ・|
    | 竊・繝・さ繝ｼ繝会ｼ亥ｾｩ蜈・ｼ・| |
    | 蠕ｩ蜈・ｾ・| 縲後％繧薙↓縺｡縺ｯ縲・竊・蜈・↓謌ｻ縺｣縺滂ｼ・|

!!! info "縺ｪ縺廝ase64繧剃ｽｿ縺・ｼ・

    **JWT繝医・繧ｯ繝ｳ・医Ο繧ｰ繧､繝ｳ險ｼ譏取嶌・峨・3縺､縺ｮ驛ｨ蛻・°繧峨〒縺阪※縺・ｋ**

    ```
    eyJhbGci... . eyJlbWFpbCI... . SflKxwRJ...
    ```

    | 驛ｨ蛻・| 蜷榊燕 | 蠖ｹ蜑ｲ |
    |------|------|------|
    | 1逡ｪ逶ｮ | 繝倥ャ繝繝ｼ | 蠖｢蠑乗ュ蝣ｱ |
    | 2逡ｪ逶ｮ | 繝壹う繝ｭ繝ｼ繝・| 繝ｦ繝ｼ繧ｶ繝ｼ諠・ｱ・・*繝｡繝ｼ繝ｫ繧｢繝峨Ξ繧ｹ縺沓ase64縺ｧ蜈･縺｣縺ｦ縺・ｋ**・・|
    | 3逡ｪ逶ｮ | 鄂ｲ蜷・| 謾ｹ縺悶ｓ髦ｲ豁｢ |

**蜈ｷ菴謎ｾ・*
```python
import base64
import json

# JWT繝医・繧ｯ繝ｳ縺ｮ萓具ｼ医・繧､繝ｭ繝ｼ繝蛾Κ蛻・ｼ・
encoded = "eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSIsIm5hbWUiOiLnlLDkuK0ifQ"

# 繧ｹ繝・ャ繝・: Base64繝・さ繝ｼ繝・
decoded_bytes = base64.urlsafe_b64decode(encoded + '==')
# 竊・b'{"email":"tanaka@example.com","name":"\xe7\x94\xb0\xe4\xb8\xad"}'

# 繧ｹ繝・ャ繝・: 譁・ｭ怜・縺ｫ螟画鋤
decoded_str = decoded_bytes.decode('utf-8')
# 竊・'{"email":"tanaka@example.com","name":"逕ｰ荳ｭ"}'

# 繧ｹ繝・ャ繝・: JSON縺ｨ縺励※隗｣譫・
data = json.loads(decoded_str)
# 竊・{'email': 'tanaka@example.com', 'name': '逕ｰ荳ｭ'}

# 繧ｹ繝・ャ繝・: 繝｡繝ｼ繝ｫ繧｢繝峨Ξ繧ｹ繧貞叙繧雁・縺・
email = data.get('email')
# 竊・'tanaka@example.com'
```

**蝗ｳ隗｣**
```
eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSIsIm5hbWUiOiLnlLDkuK0ifQ
                            竊・
                    Base64繝・さ繝ｼ繝・
                            竊・
{"email":"tanaka@example.com","name":"逕ｰ荳ｭ"}
                            竊・
                    JSON縺ｨ縺励※隗｣譫・
                            竊・
                    email 繧貞叙繧雁・縺・
                            竊・
                 tanaka@example.com
```

---

## 2. 繝ｩ繧､繝悶Λ繝ｪ隱ｭ縺ｿ霎ｼ縺ｿ

```python
import os
import json
import base64
from datetime import datetime
import functions_framework
from openai import OpenAI
```

### 蜷・Λ繧､繝悶Λ繝ｪ縺ｮ蠖ｹ蜑ｲ

| 繝ｩ繧､繝悶Λ繝ｪ | 蠖ｹ蜑ｲ | 菴ｿ縺・ｴ髱｢ |
|-----------|------|---------|
| `os` | 迺ｰ蠅・､画焚繧定ｪｭ繧 | API繧ｭ繝ｼ繧・ｨｱ蜿ｯ繝ｪ繧ｹ繝医・蜿門ｾ・|
| `json` | JSON繝・・繧ｿ繧呈桶縺・| 繝医・繧ｯ繝ｳ隗｣譫舌√Ξ繧ｹ繝昴Φ繧ｹ菴懈・ |
| `base64` | 繝・・繧ｿ繧貞､画鋤縺吶ｋ | JWT繝医・繧ｯ繝ｳ縺ｮ繝・さ繝ｼ繝・|
| `datetime` | 譌･譎ゅｒ謇ｱ縺・| 繝倥Ν繧ｹ繝√ぉ繝・け縺ｮ譎ょ綾陦ｨ遉ｺ |
| `functions_framework` | Cloud Run蟇ｾ蠢・| HTTP繝ｪ繧ｯ繧ｨ繧ｹ繝医ｒ蜿励￠蜿悶ｋ |
| `openai` | ChatGPT API | AI縺ｫ雉ｪ蝠上ｒ騾√ｋ |

---

## 繧ｻ繧ｭ繝･繝ｪ繝・ぅ縺ｮ蜈ｨ菴灘ワ・医↑縺懷ｮ牙・・滂ｼ・

繧ｳ繝ｼ繝峨・隧ｳ邏ｰ縺ｫ蜈･繧句燕縺ｫ縲・*縺薙・繧ｷ繧ｹ繝・Β縺後←縺・ｮ医ｉ繧後※縺・ｋ縺・*繧堤炊隗｣縺励∪縺励ｇ縺・・

### 螟壼ｱ､髦ｲ蠕｡縺ｮ莉慕ｵ・∩

縺薙・繧ｷ繧ｹ繝・Β縺ｯ**隍・焚縺ｮ髦ｲ蠕｡螻､**縺ｧ螳医ｉ繧後※縺・∪縺吶・

```text
Request (who is accessing?)
         |
         v
+-------------------------------------+
| Layer 1: CORS                       |
| Is access from allowed site?        |
| -> No: Browser blocks response      |
+-------------------------------------+
         | Yes
         v
+-------------------------------------+
| Layer 2: JWT Verification           |
| Is login valid?                     |
| -> No: Return error (no processing) |
+-------------------------------------+
         | Yes
         v
+-------------------------------------+
| Layer 3: Allow List                 |
| Is email/domain allowed?            |
| -> No: Return error (no processing) |
+-------------------------------------+
         | Yes
         v
+-------------------------------------+
| OpenAI API Call (Billing happens!)  |
+-------------------------------------+
```

**譌･譛ｬ隱槭〒縺ｮ隱ｬ譏趣ｼ・*

| 螻､ | 菴輔ｒ繝√ぉ繝・け・・| No縺ｮ蝣ｴ蜷・|
|:--:|---------------|----------|
| 隨ｬ1螻､ CORS | 險ｱ蜿ｯ縺輔ｌ縺溘し繧､繝医°繧会ｼ・| 繝悶Λ繧ｦ繧ｶ縺後ヶ繝ｭ繝・け |
| 隨ｬ2螻､ JWT讀懆ｨｼ | 繝ｭ繧ｰ繧､繝ｳ縺励※繧具ｼ・| 繧ｨ繝ｩ繝ｼ霑斐☆ |
| 隨ｬ3螻､ 險ｱ蜿ｯ繝ｪ繧ｹ繝・| 險ｱ蜿ｯ縺輔ｌ縺溘Θ繝ｼ繧ｶ繝ｼ・・| 繧ｨ繝ｩ繝ｼ霑斐☆ |
| 騾夐℃蠕・| - | OpenAI API蜻ｼ縺ｳ蜃ｺ縺暦ｼ郁ｪｲ驥托ｼ・|

### 蜷・ｱ､縺ｮ蠖ｹ蜑ｲ

| 螻､ | 蜷榊燕 | 菴輔ｒ螳医ｋ・・| 遯∫ｴ縺輔ｌ繧九→・・|
|:--:|------|-----------|---------------|
| 1 | CORS | 荳肴ｭ｣繧ｵ繧､繝医°繧峨・API蛻ｩ逕ｨ | 邨先棡縺檎尢縺ｾ繧後ｋ蜿ｯ閭ｽ諤ｧ |
| 2 | JWT讀懆ｨｼ | 譛ｪ繝ｭ繧ｰ繧､繝ｳ繝ｦ繝ｼ繧ｶ繝ｼ | **隱ｲ驥代＆繧後ｋ** |
| 3 | 險ｱ蜿ｯ繝ｪ繧ｹ繝・| 驛ｨ螟冶・・繧｢繧ｯ繧ｻ繧ｹ | **隱ｲ驥代＆繧後ｋ** |

!!! warning "CORS縺縺代〒縺ｯ荳榊香蛻・↑逅・罰"

    ```
    縲燭ORS縺ｮ髯千阜縲・

    evil.com 竊・繝ｪ繧ｯ繧ｨ繧ｹ繝・竊・繧ｵ繝ｼ繝舌・蜃ｦ逅・竊・OpenAI蜻ｼ縺ｶ 竊・隱ｲ驥托ｼ・
                                                  竊・
                                  繝ｬ繧ｹ繝昴Φ繧ｹ霑斐☆ 竊・繝悶Λ繧ｦ繧ｶ縺後ヶ繝ｭ繝・け
                                                  竊・
                                       縲瑚ｦ九○縺ｪ縺・阪□縺代〒蜃ｦ逅・・襍ｰ繧・

    縲辱WT + 險ｱ蜿ｯ繝ｪ繧ｹ繝医′縺ゅｋ蝣ｴ蜷医・

    evil.com 竊・繝ｪ繧ｯ繧ｨ繧ｹ繝・竊・JWT讀懆ｨｼ 竊・繝繝｡・≫・ 繧ｨ繝ｩ繝ｼ霑斐☆
                              竊・
                       縺薙％縺ｧ豁｢縺ｾ繧具ｼ郁ｪｲ驥代＆繧後↑縺・ｼ・
    ```

    CORS縺ｯ縲後ヶ繝ｩ繧ｦ繧ｶ縺檎ｵ先棡繧定ｦ九○縺ｪ縺・阪□縺代・
    **繧ｵ繝ｼ繝舌・蛛ｴ縺ｮ蜃ｦ逅・ｼ郁ｪｲ驥托ｼ峨・豁｢繧√ｉ繧後∪縺帙ｓ縲・*

    縺縺九ｉ**JWT讀懆ｨｼ縺ｨ險ｱ蜿ｯ繝ｪ繧ｹ繝・*縺ｧ縲・
    **鬮倅ｾ｡縺ｪ蜃ｦ逅・ｼ・I蜻ｼ縺ｳ蜃ｺ縺暦ｼ峨・蜑阪↓諡貞凄**縺励※縺・∪縺吶・

!!! tip "縺薙・蠕後・繧ｳ繝ｼ繝峨ｒ隱ｭ繧繝昴う繝ｳ繝・

    | 繧ｻ繧ｯ繧ｷ繝ｧ繝ｳ | 蟇ｾ蠢懊☆繧矩亟蠕｡螻､ | 螳溯｡碁・|
    |-----------|---------------|:------:|
    | 4-1. set_cors_headers | 隨ｬ1螻､・咾ORS | 1 |
    | 5-2. get_email_from_token | 隨ｬ2螻､・哽WT讀懆ｨｼ | 2 |
    | 5-1. is_email_allowed | 隨ｬ3螻､・夊ｨｱ蜿ｯ繝ｪ繧ｹ繝・| 3 |

    窶ｻ 繧ｻ繧ｯ繧ｷ繝ｧ繝ｳ逡ｪ蜿ｷ縺ｨ繧ｳ繝ｼ繝峨・螳溯｡碁・・逡ｰ縺ｪ繧翫∪縺吶・
    螳滄圀縺ｮ蜃ｦ逅・・縲繰WT讀懆ｨｼ 竊・險ｱ蜿ｯ繝ｪ繧ｹ繝医阪・鬆・分縺ｧ陦後ｏ繧後∪縺吶・

### 縺ｪ縺懊後・繝・ム繝ｼ縲阪〒髦ｲ蠕｡縺ｧ縺阪ｋ縺ｮ縺具ｼ・

繝倥ャ繝繝ｼ縺ｮ隧ｱ縺悟・縺ｦ縺上ｋ蜑阪↓縲・*HTTP騾壻ｿ｡縺ｮ莉慕ｵ・∩**繧堤炊隗｣縺励∪縺励ｇ縺・・

#### HTTP騾壻ｿ｡ = 謇狗ｴ吶・繧・ｊ縺ｨ繧・

```text
[Request]
Browser  ------>  Server
         "Give me /api/chat"

[Response]
Browser  <------  Server
         "Here you go"
```

#### 繧ｵ繝ｼ繝舌・縺九ｉ繝悶Λ繧ｦ繧ｶ縺ｸ縺ｮ霑比ｺ具ｼ医Ξ繧ｹ繝昴Φ繧ｹ・峨↓縺ｯ縲・縺､縺ｮ驛ｨ蛻・阪′縺ゅｋ

繧ｵ繝ｼ繝舌・縺後ヶ繝ｩ繧ｦ繧ｶ縺ｫ霑斐☆縲瑚ｿ比ｺ九阪・縲∽ｻ･荳九・讒矩縺ｫ縺ｪ縺｣縺ｦ縺・∪縺呻ｼ・

```text
+------------------------------------------+
| HEADER (Instructions for browser)        |
|                                          |
|   Content-Type: application/json         |
|   X-Frame-Options: DENY                  |
|   Access-Control-Allow-Origin: ...       |
+------------------------------------------+
| BODY (Actual data)                       |
|                                          |
|   {"message": "Hello"}                   |
+------------------------------------------+
```

| 驛ｨ蛻・| 蠖ｹ蜑ｲ | 萓・|
|------|------|-----|
| **繝倥ャ繝繝ｼ** | 繝悶Λ繧ｦ繧ｶ縺ｸ縺ｮ縲梧欠遉ｺ譖ｸ縲・| `X-Frame-Options: DENY` |
| **繝懊ョ繧｣** | 螳滄圀縺ｮ繝・・繧ｿ | `{"message": "Hello"}` |

**繝倥ャ繝繝ｼ = 縲後％縺ｮ霑比ｺ九ｒ縺薙≧謇ｱ縺｣縺ｦ縺ｭ縲阪→縺・≧繝悶Λ繧ｦ繧ｶ縺ｸ縺ｮ蜻ｽ莉､**

#### 繝悶Λ繧ｦ繧ｶ縺ｯ繝倥ャ繝繝ｼ縺ｫ蠕薙≧・井ｻ墓ｧ倥〒豎ｺ縺ｾ縺｣縺ｦ縺・ｋ・・

```text
Server: "X-Frame-Options: DENY"
   |
   v
Browser: "OK, I won't put this page in iframe"
```

縺薙ｌ縺ｯ**繝悶Λ繧ｦ繧ｶ縺ｮ莉墓ｧ假ｼ医Ν繝ｼ繝ｫ・・*縺ｧ縺吶・
Chrome縲：irefox縲・dge 縺ｪ縺ｩ縲√☆縺ｹ縺ｦ縺ｮ荳ｻ隕√ヶ繝ｩ繧ｦ繧ｶ縺後％縺ｮ繝ｫ繝ｼ繝ｫ縺ｫ蠕薙＞縺ｾ縺吶・

#### CORS縺ｮ蜍輔″・医す繝ｳ繝励Ν縺ｫ・・

```text
evil.com (JavaScript)
   |
   |  "Give me data from your-app.run.app"
   v
Server (your-app.run.app)
   |
   |  API processing... (Billing happens here!)
   |
   |  Response + Header:
   |  "Only your-app.run.app can receive this data"
   v
Browser
   |
   |  "evil.com is not allowed in the header..."
   v
BLOCKED! (Data not passed to JavaScript)
```

**CORS縺ｨ縺ｯ・・*
繝倥ャ繝繝ｼ縺ｫ縲瑚ｨｱ蜿ｯ縺輔ｌ縺溘し繧､繝医阪′譖ｸ縺・※縺ゅｊ縲√◎繧御ｻ･螟悶↓縺ｯ**繝・・繧ｿ繧呈ｸ｡縺輔↑縺・*莉慕ｵ・∩縲・

!!! danger "驥崎ｦ・ｼ夊ｪｲ驥代・髦ｲ縺偵↑縺・

    荳翫・蝗ｳ繧偵ｈ縺剰ｦ九※縺上□縺輔＞縲・

    - 繧ｵ繝ｼ繝舌・縺ｯ**蜃ｦ逅・ｒ螳溯｡・*縺励※縺・ｋ・・PI processing・・
    - 繝ｬ繧ｹ繝昴Φ繧ｹ繧・*霑斐＠縺ｦ縺・ｋ**

    縺､縺ｾ繧・*API縺ｯ菴ｿ繧上ｌ縺ｦ縺・ｋ = 隱ｲ驥代・逋ｺ逕溘☆繧・*・・

    CORS縺碁亟縺舌・縺ｯ縲檎ｵ先棡繧谷avaScript縺ｫ貂｡縺吶％縺ｨ縲阪□縺代・
    **蜃ｦ逅・・菴薙・豁｢繧√ｉ繧後∪縺帙ｓ縲・*

#### 縺､縺ｾ繧・

| 逍大撫 | 遲斐∴ |
|------|------|
| CORS縺ｯ菴輔ｒ縺吶ｋ・・| 險ｱ蜿ｯ縺輔ｌ縺ｦ縺ｪ縺・し繧､繝医↓縺ｯ繝・・繧ｿ繧呈ｸ｡縺輔↑縺・|
| 隱ｰ縺悟愛譁ｭ縺吶ｋ・・| 繝悶Λ繧ｦ繧ｶ・医・繝・ム繝ｼ繧定ｦ九※蛻､譁ｭ・・|
| 隱ｲ驥代・髦ｲ縺偵ｋ・・| **髦ｲ縺偵↑縺・*・亥・逅・・襍ｰ繧具ｼ・|
| 縺倥ｃ縺ゆｽ輔・縺溘ａ・・| 繝・・繧ｿ縺ｮ**逶励∩隕・*繧帝亟縺・|

!!! warning "驥崎ｦ√↑豕ｨ諢・

    繝倥ャ繝繝ｼ縺ｧ螳医ｌ繧九・縺ｯ**繝悶Λ繧ｦ繧ｶ縺九ｉ縺ｮ繧｢繧ｯ繧ｻ繧ｹ**縺縺代〒縺吶・

    ```
    繝悶Λ繧ｦ繧ｶ 竊・繝倥ャ繝繝ｼ縺ｫ蠕薙≧ 竊・髦ｲ蠕｡縺ｧ縺阪ｋ 笨・
    curl/Postman 竊・繝倥ャ繝繝ｼ辟｡隕悶〒縺阪ｋ 竊・髦ｲ蠕｡縺ｧ縺阪↑縺・笨・
    ```

    縺縺九ｉ**JWT讀懆ｨｼ繧・ｨｱ蜿ｯ繝ｪ繧ｹ繝・*繧ょｿ・ｦ√↑縺ｮ縺ｧ縺吶・

---

## 3. 險ｭ螳夐Κ蛻・

### ALLOWED_ORIGINS

```python
ALLOWED_ORIGINS = ['*']
```

**縺薙ｌ縺ｯ菴包ｼ・*
- 縺ｩ縺ｮWeb繧ｵ繧､繝医°繧峨・繧｢繧ｯ繧ｻ繧ｹ繧定ｨｱ蜿ｯ縺吶ｋ縺九・繝ｪ繧ｹ繝・
- `'*'` = 縺ｩ縺薙°繧峨〒繧０K・磯幕逋ｺ逕ｨ・・

---

### 繝輔ぃ繧､繝ｫ隱ｭ縺ｿ霎ｼ縺ｿ

```python
with open('front.html', 'r', encoding='utf-8') as f:
    HTML_CONTENT = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    SCRIPT_CONTENT = f.read()
```

**菴輔ｒ縺励※縺・ｋ・・*
1. `front.html` 繝輔ぃ繧､繝ｫ繧帝幕縺・
2. 荳ｭ霄ｫ繧貞・驛ｨ隱ｭ縺ｿ霎ｼ繧
3. `HTML_CONTENT` 縺ｨ縺・≧螟画焚縺ｫ菫晏ｭ・

**縺ｪ縺懈怙蛻昴↓隱ｭ縺ｿ霎ｼ繧・・*
- 繝ｪ繧ｯ繧ｨ繧ｹ繝医・縺溘・縺ｫ隱ｭ縺ｿ霎ｼ繧縺ｨ驕・￥縺ｪ繧・
- 荳蠎ｦ隱ｭ繧薙〒繝｡繝｢繝ｪ縺ｫ菫晏ｭ倥＠縺ｦ縺翫￥

---

## 4. 繝倥Ν繝代・髢｢謨ｰ

### 4-1. set_cors_headers・・ORS險ｭ螳夲ｼ・

```python
def set_cors_headers(headers, origin):
    if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
        headers['Access-Control-Allow-Origin'] = origin or '*'
    headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    headers['Access-Control-Max-Age'] = '3600'
```

#### 蠑墓焚縺ｮ隱ｬ譏・

| 蠑墓焚 | 蝙・| 隱ｬ譏・|
|------|-----|------|
| `headers` | 霎樊嶌 | 繝ｬ繧ｹ繝昴Φ繧ｹ縺ｫ莉倥￠繧九・繝・ム繝ｼ諠・ｱ |
| `origin` | 譁・ｭ怜・ | 繝ｪ繧ｯ繧ｨ繧ｹ繝亥・縺ｮURL・井ｾ具ｼ啻https://example.com`・・|

#### 1陦後★縺､隗｣隱ｬ

**1陦檎岼・壽擅莉ｶ蛻､螳・*
```python
if '*' in ALLOWED_ORIGINS or origin in ALLOWED_ORIGINS:
```

!!! note "縺薙・譚｡莉ｶ縺ｯ2縺､縺ｮ蛻､螳壹ｒ `or` 縺ｧ郢九＞縺ｧ縺・ｋ"

    | 蛻､螳・| 蜀・ｮｹ | 邨先棡 |
    |------|------|------|
    | 蛻､螳・ | `'*' in ALLOWED_ORIGINS` 竊・ALLOWED_ORIGINS 縺ｫ '*' 縺悟性縺ｾ繧後ｋ縺具ｼ・| `['*']` 縺ｪ縺ｮ縺ｧ True |
    | 蛻､螳・ | `origin in ALLOWED_ORIGINS` 竊・繝ｪ繧ｯ繧ｨ繧ｹ繝亥・URL縺瑚ｨｱ蜿ｯ繝ｪ繧ｹ繝医↓蜷ｫ縺ｾ繧後ｋ縺具ｼ・| URL谺｡隨ｬ |

    `or` 縺ｧ郢九＞縺ｧ縺・ｋ縺ｮ縺ｧ縲・*縺ｩ縺｡繧峨°縺卦rue縺ｪ繧我ｸｭ縺ｮ蜃ｦ逅・ｒ螳溯｡・*

**2陦檎岼・壹・繝・ム繝ｼ縺ｫ蛟､繧定ｨｭ螳・*
```python
headers['Access-Control-Allow-Origin'] = origin or '*'
```

!!! note "隗｣隱ｬ"

    - `headers['繧ｭ繝ｼ蜷・] = 蛟､` 竊・霎樊嶌縺ｫ蛟､繧定ｿｽ蜉縺吶ｋ譖ｸ縺肴婿
    - `origin or '*'` 竊・origin 縺ｫ蛟､縺後≠繧後・縺昴ｌ繧剃ｽｿ縺・・one 繧・ｩｺ縺ｪ繧・`'*'` 繧剃ｽｿ縺・

    **萓具ｼ・*

    | origin 縺ｮ蛟､ | 邨先棡 |
    |-------------|------|
    | `'https://example.com'` | `headers['Access-Control-Allow-Origin'] = 'https://example.com'` |
    | `None` | `headers['Access-Control-Allow-Origin'] = '*'` |

**3-5陦檎岼・壼崋螳壹・繝・ム繝ｼ縺ｮ險ｭ螳・*
```python
headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
headers['Access-Control-Max-Age'] = '3600'
```

| 繝倥ャ繝繝ｼ | 蛟､ | 諢丞袖 |
|---------|-----|------|
| `Access-Control-Allow-Methods` | `'GET, POST, OPTIONS'` | 縺薙・3縺､縺ｮHTTP繝｡繧ｽ繝・ラ繧定ｨｱ蜿ｯ |
| `Access-Control-Allow-Headers` | `'Content-Type, Authorization'` | 縺薙・2縺､縺ｮ繝倥ャ繝繝ｼ繧定ｨｱ蜿ｯ |
| `Access-Control-Max-Age` | `'3600'` | 縺薙・險ｭ螳壹ｒ3600遘抵ｼ・譎る俣・峨く繝｣繝・す繝･ |

#### CORS縺ｨ縺ｯ・滂ｼ郁ｩｳ邏ｰ隗｣隱ｬ・・

**CORS = Cross-Origin Resource Sharing・育焚縺ｪ繧九が繝ｪ繧ｸ繝ｳ髢薙・繝ｪ繧ｽ繝ｼ繧ｹ蜈ｱ譛会ｼ・*

!!! tip "雎・衍隴假ｼ壹が繝ｪ繧ｸ繝ｳ・・rigin・峨→縺ｯ・・

    繧ｪ繝ｪ繧ｸ繝ｳ縺ｯ縲・*繝励Ο繝医さ繝ｫ + 繝峨Γ繧､繝ｳ + 繝昴・繝・*縲阪・邨・∩蜷医ｏ縺帙〒縺吶・

    | 隕∫ｴ | 隱ｬ譏・| 萓・|
    |------|------|-----|
    | **繝励Ο繝医さ繝ｫ** | 騾壻ｿ｡縺ｮ譁ｹ蠑・| `https://` 縺ｾ縺溘・ `http://` |
    | **繝峨Γ繧､繝ｳ** | 繧ｵ繝ｼ繝舌・縺ｮ菴乗園 | `your-app.run.app` |
    | **繝昴・繝・* | 繧ｵ繝ｼ繝舌・縺ｮ蜈･蜿｣逡ｪ蜿ｷ | `:443`・・ttps・峨～:80`・・ttp・俄ｻ逵∫払蜿ｯ |

    ```
    https://your-app.run.app:443
    笏披楳笏ｬ笏笏笏・笏披楳笏笏笏笏笏笏笏ｬ笏笏笏笏笏笏笏笏倪粕笏ｬ笏笏・
    繝励Ο繝医さ繝ｫ   繝峨Γ繧､繝ｳ    繝昴・繝・
    ```

    **蜷後§繧ｪ繝ｪ繧ｸ繝ｳ vs 蛻･繧ｪ繝ｪ繧ｸ繝ｳ**

    | URL | `https://your-app.run.app` 縺ｨ豈碑ｼ・| 逅・罰 |
    |-----|----------------------------------|------|
    | `https://your-app.run.app/api/chat` | 蜷後§ | 繝代せ縺碁＆縺・□縺・|
    | `http://your-app.run.app` | **蛻･** | 繝励Ο繝医さ繝ｫ縺碁＆縺・|
    | `https://evil.com` | **蛻･** | 繝峨Γ繧､繝ｳ縺碁＆縺・|
    | `https://your-app.run.app:8080` | **蛻･** | 繝昴・繝医′驕輔≧ |

!!! info "https縺ｨhttp縺ｮ驕輔＞"

    | 鬆・岼 | http | https |
    |------|------|-------|
    | 證怜捷蛹・| 縺ｪ縺暦ｼ井ｸｸ隕九∴・・| 縺ゅｊ・域囓蜿ｷ蛹厄ｼ・|
    | 繝昴・繝・| 80 | 443 |
    | 螳牙・諤ｧ | 菴弱＞ | 鬮倥＞ |
    | 逕ｨ騾・| 髢狗匱迺ｰ蠅・・縺ｿ | 譛ｬ逡ｪ迺ｰ蠅・ｼ亥ｿ・茨ｼ・|

    ```
    縲辛ttp縺ｮ蝣ｴ蜷茨ｼ亥些髯ｺ・峨・
    縺ゅ↑縺・笏笏縲後ヱ繧ｹ繝ｯ繝ｼ繝・ 1234縲坂楳笏笆ｶ 繧ｵ繝ｼ繝舌・
                 竊・
             隱ｰ縺ｧ繧りｦ九ｌ繧具ｼ・

    縲辛ttps縺ｮ蝣ｴ蜷茨ｼ亥ｮ牙・・峨・
    縺ゅ↑縺・笏笏縲交沐呈囓蜿ｷ蛹悶＆繧後◆繝・・繧ｿ縲坂楳笏笆ｶ 繧ｵ繝ｼ繝舌・
                 竊・
             隗｣隱ｭ縺ｧ縺阪↑縺・
    ```

!!! success "繧ｷ繝翫Μ繧ｪ1・壽勸騾壹・菴ｿ縺・婿・亥撫鬘後↑縺暦ｼ・

    **縺ゅ↑縺溘・繧ｵ繧､繝・** `https://your-app.run.app`

    - `front.html`・育判髱｢・・
    - `/api/chat`・・PI・・

    **豬√ｌ・・*
    繝ｦ繝ｼ繧ｶ繝ｼ 竊・your-app.run.app 縺ｫ繧｢繧ｯ繧ｻ繧ｹ 竊・front.html 縺ｮ JavaScript 縺・`/api/chat` 繧貞他縺ｶ 竊・**蜷後§繧ｵ繧､繝医↑縺ｮ縺ｧ蝠城｡後↑縺・笨・*

!!! danger "繧ｷ繝翫Μ繧ｪ2・壽が諢上・縺ゅｋ繧ｵ繧､繝医°繧峨・謾ｻ謦・

    **謔ｪ諢上・縺ゅｋ繧ｵ繧､繝・** `https://evil.com`

    繝壹・繧ｸ蜀・・JavaScript縺ｧ縲√≠縺ｪ縺溘・ `/api/chat` 繧貞享謇九↓蜻ｼ縺ｼ縺・→縺吶ｋ・・

    ```javascript
    fetch('https://your-app.run.app/api/chat', {
        method: 'POST',
        body: JSON.stringify({ message: '...' })
    });
    ```

    **繝悶Λ繧ｦ繧ｶ縺ｮ蜍輔″・・*

    1. 繝悶Λ繧ｦ繧ｶ・壹悟ｾ・▲縺ｦ・‘vil.com 縺九ｉ your-app 縺ｸ縺ｮ繝ｪ繧ｯ繧ｨ繧ｹ繝医□縲りｨｱ蜿ｯ縺輔ｌ縺ｦ繧具ｼ溘・
    2. 繧ｵ繝ｼ繝舌・縺ｮ `Access-Control-Allow-Origin` 繧堤｢ｺ隱・
    3. evil.com 縺瑚ｨｱ蜿ｯ縺輔ｌ縺ｦ縺・↑縺代ｌ縺ｰ 竊・**繝悶Ο繝・け・・*

    **竊・險ｱ蜿ｯ縺励◆縺・ｴ蜷医・ `ALLOWED_ORIGINS` 縺ｫ縺昴・繧ｪ繝ｪ繧ｸ繝ｳ繧定ｿｽ蜉縺吶ｌ縺ｰOK・・*

    ```python
    # 萓具ｼ壹ヱ繝ｼ繝医リ繝ｼ莨∵･ｭ縺ｮ繧ｵ繧､繝医°繧陰PI繧剃ｽｿ縺医ｋ繧医≧縺ｫ縺励◆縺・ｴ蜷・
    ALLOWED_ORIGINS = [
        'https://your-app.run.app',      # 閾ｪ蛻・・繧ｵ繧､繝・
        'https://partner-site.com'       # 竊・縺薙％縺ｫ霑ｽ蜉・・
    ]
    ```

**縺､縺ｾ繧海ORS縺ｯ・・*
- 繝悶Λ繧ｦ繧ｶ縺瑚｡後≧繧ｻ繧ｭ繝･繝ｪ繝・ぅ繝√ぉ繝・け
- 縲後％縺ｮ繧ｵ繧､繝医°繧峨・繝ｪ繧ｯ繧ｨ繧ｹ繝医ｒ險ｱ蜿ｯ縺励∪縺吶°・溘阪ｒ繧ｵ繝ｼ繝舌・縺ｫ遒ｺ隱・
- 繧ｵ繝ｼ繝舌・縺後薫K縲阪→險繧上↑縺代ｌ縺ｰ繝悶Ο繝・け

!!! info "HTTP繝｡繧ｽ繝・ラ縺ｮ蠖ｹ蜑ｲ"

    | 繝｡繧ｽ繝・ラ | 逕ｨ騾・| 蜈ｷ菴謎ｾ・|
    |---------|------|--------|
    | **GET** | 繝・・繧ｿ繧貞叙蠕励☆繧・| 繝壹・繧ｸ陦ｨ遉ｺ縲√Θ繝ｼ繧ｶ繝ｼ諠・ｱ蜿門ｾ・|
    | **POST** | 繝・・繧ｿ繧帝∽ｿ｡繝ｻ蜃ｦ逅・☆繧・| 繝√Ε繝・ヨ騾∽ｿ｡縲√Ο繧ｰ繧､繝ｳ蜃ｦ逅・|
    | **OPTIONS** | 莠句燕遒ｺ隱搾ｼ医・繝ｪ繝輔Λ繧､繝茨ｼ・| 縲後％縺ｮ繝ｪ繧ｯ繧ｨ繧ｹ繝磯√▲縺ｦ縺・＞・溘阪→繝悶Λ繧ｦ繧ｶ縺後し繝ｼ繝舌・縺ｫ遒ｺ隱・|

    **POST縺ｮ蜍輔″・医う繝｡繝ｼ繧ｸ・・*

    ```
    [縺ゅ↑縺歉                    [API・・1縺吶ｋ蜃ｦ逅・ｼ云
       笏・                             笏・
       笏や楳笏笏笏 POST { value: 1 } 笏笏笏笏笏笏笆ｶ笏・
       笏・                             笏・竊・縺薙％縺ｧ1+1縺ｮ蜃ｦ逅・
       笏や沃笏笏笏笏笏 { result: 2 } 笏笏笏笏笏笏笏笏笏笏・
    ```

    竊・繝・・繧ｿ繧呈兜縺偵※縲、PI蛛ｴ縺ｧ蜃ｦ逅・＠縺ｦ縲∫ｵ先棡縺瑚ｿ斐▲縺ｦ縺上ｋ

!!! note "OPTIONS繝ｪ繧ｯ繧ｨ繧ｹ繝医・豬√ｌ・医・繝ｪ繝輔Λ繧､繝茨ｼ・

    繝悶Λ繧ｦ繧ｶ縺ｯ縲梧悽逡ｪ縺ｮ繝ｪ繧ｯ繧ｨ繧ｹ繝医阪ｒ騾√ｋ蜑阪↓縲√∪縺壹碁√▲縺ｦ縺・＞縺具ｼ溘阪ｒ遒ｺ隱阪＠縺ｾ縺吶・

    ```
    繝悶Λ繧ｦ繧ｶ: 縲訓OST繝ｪ繧ｯ繧ｨ繧ｹ繝磯√ｊ縺溘＞繧薙□縺代←縲√＞縺・ｼ溘搾ｼ・PTIONS・・
        竊・
    繧ｵ繝ｼ繝舌・: 縲後％縺ｮ繧ｪ繝ｪ繧ｸ繝ｳ縺九ｉ縺ｪ繧碓K縲阪∪縺溘・縲後ム繝｡縲・
        竊・
    繝悶Λ繧ｦ繧ｶ: OK縺ｪ繧画悽逡ｪ縺ｮPOST繧帝∽ｿ｡縲√ム繝｡縺ｪ繧峨ヶ繝ｭ繝・け
    ```

    縺薙・莉慕ｵ・∩縺ｫ繧医ｊ縲∬ｨｱ蜿ｯ縺輔ｌ縺ｦ縺・↑縺・し繧､繝医°繧峨・荳肴ｭ｣縺ｪ繝ｪ繧ｯ繧ｨ繧ｹ繝医ｒ髦ｲ縺・〒縺・∪縺吶・

!!! question "逋ｻ骭ｲ縺吶ｋ繧ｪ繝ｪ繧ｸ繝ｳ縺ｮ譖ｸ縺肴婿"

    繧ｪ繝ｪ繧ｸ繝ｳ縺ｯ縲・*繝励Ο繝医さ繝ｫ + 繝峨Γ繧､繝ｳ + 繝昴・繝・*縲阪〒縺吶ゅヱ繧ｹ・・/api/chat` 縺ｪ縺ｩ・峨・蜷ｫ繧√∪縺帙ｓ縲・

    ```
    https://your-app.run.app/page/chat?user=123
    笏披楳笏笏笏笏笏笏笏笏笏笏ｬ笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏倪粕笏笏笏笏笏笏笏笏ｬ笏笏笏笏笏笏笏笏笏・
          繧ｪ繝ｪ繧ｸ繝ｳ・医％繧後ｒ逋ｻ骭ｲ・・   繝代せ・亥性繧√↑縺・ｼ・
    ```

    | 逋ｻ骭ｲ萓・| 豁｣隱､ | 逅・罰 |
    |--------|:----:|------|
    | `https://your-app.run.app` | 笨・| 豁｣縺励＞蠖｢蠑・|
    | `https://your-app.run.app/api/chat` | 笨・| 繝代せ縺ｯ荳崎ｦ・|
    | `your-app.run.app` | 笨・| 繝励Ο繝医さ繝ｫ縺悟ｿ・ｦ・|

    **菴輔・繧ｪ繝ｪ繧ｸ繝ｳ繧堤匳骭ｲ縺吶ｋ・・竊・繝輔Ο繝ｳ繝医お繝ｳ繝会ｼ育判髱｢・峨・繧ｪ繝ｪ繧ｸ繝ｳ**

    繝ｦ繝ｼ繧ｶ繝ｼ縺後ヶ繝ｩ繧ｦ繧ｶ縺ｧ繧｢繧ｯ繧ｻ繧ｹ縺励※縺・ｋ逕ｻ髱｢縺ｮ繧ｪ繝ｪ繧ｸ繝ｳ繧堤匳骭ｲ縺励∪縺吶・

!!! example "隍・焚繧ｪ繝ｪ繧ｸ繝ｳ繧堤匳骭ｲ縺吶ｋ蝣ｴ蜷・

    髢狗匱迺ｰ蠅・・繧ｹ繝・・繧ｸ繝ｳ繧ｰ迺ｰ蠅・・譛ｬ逡ｪ迺ｰ蠅・↑縺ｩ縲∬､・焚縺ｮ繧ｪ繝ｪ繧ｸ繝ｳ縺九ｉ繧｢繧ｯ繧ｻ繧ｹ縺悟ｿ・ｦ√↑蝣ｴ蜷医・縲・・蛻励↓霑ｽ蜉縺励∪縺吶・

    ```python
    ALLOWED_ORIGINS = [
        'https://your-app.run.app',           # 譛ｬ逡ｪ
        'https://staging.your-app.run.app',   # 繧ｹ繝・・繧ｸ繝ｳ繧ｰ
        'http://localhost:3000',               # 髢狗匱・医Ο繝ｼ繧ｫ繝ｫ・・
        'http://localhost:5173'                # Vite縺ｪ縺ｩ蛻･繝昴・繝・
    ]
    ```

    髢狗匱荳ｭ縺ｯ `['*']` 縺ｧ蜈ｨ險ｱ蜿ｯ縺ｫ縺励※縺翫＞縺ｦ縲∵悽逡ｪ縺ｧ縺ｯ蜈ｷ菴鍋噪縺ｪ繧ｪ繝ｪ繧ｸ繝ｳ繧呈欠螳壹☆繧九√→縺・≧縺ｮ縺後ｈ縺上≠繧九ヱ繧ｿ繝ｼ繝ｳ縺ｧ縺吶・

!!! warning "`['*']`・亥・險ｱ蜿ｯ・峨・縺ｾ縺ｾ縺縺ｨ菴輔′襍ｷ縺阪ｋ・・

    ```python
    # 繝・ヵ繧ｩ繝ｫ繝郁ｨｭ螳夲ｼ亥些髯ｺ・・ｼ・
    ALLOWED_ORIGINS = ['*']  # 竊・縺ｩ縺薙°繧峨〒繧０K
    ```

    縺薙・迥ｶ諷九□縺ｨ縲・*謔ｪ諢上・縺ゅｋ繧ｵ繧､繝医°繧陰PI繧貞享謇九↓菴ｿ繧上ｌ縺ｾ縺・*縲・

    | 陲ｫ螳ｳ | 蜈ｷ菴謎ｾ・|
    |------|--------|
    | **隱ｲ驥代′逋ｺ逕・* | 蜍晄焔縺ｫ繝√Ε繝・ヨAPI繧貞娼縺九ｌ縲＾penAI API縺ｮ譁咎≡縺後≠縺ｪ縺溘↓隲区ｱゅ＆繧後ｋ |
    | **繧ｵ繝ｼ繝薙せ蛛懈ｭ｢** | 螟ｧ驥上Μ繧ｯ繧ｨ繧ｹ繝医〒繧ｵ繝ｼ繝舌・縺後ム繧ｦ繝ｳ縺吶ｋ |
    | **菫｡逕ｨ菴惹ｸ・* | 荳肴ｭ｣蛻ｩ逕ｨ縺ｮ雕上∩蜿ｰ縺ｫ縺輔ｌ繧句庄閭ｽ諤ｧ |

    **竊・譛ｬ逡ｪ縺ｧ縺ｯ蠢・★險ｱ蜿ｯ縺吶ｋ繧ｪ繝ｪ繧ｸ繝ｳ繧帝剞螳壹＠縺ｾ縺励ｇ縺・ｼ・*

---

### 4-2. set_security_headers・医そ繧ｭ繝･繝ｪ繝・ぅ險ｭ螳夲ｼ・

```python
def set_security_headers(headers):
    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Frame-Options'] = 'DENY'
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
```

#### 1陦後★縺､隗｣隱ｬ

**1. X-Content-Type-Options**
```python
headers['X-Content-Type-Options'] = 'nosniff'
```

!!! warning "謾ｻ謦・・萓・

    謾ｻ謦・・ｼ壹景mage.jpg縲阪→縺・≧蜷榊燕縺ｧ謔ｪ諢上・縺ゅｋJavaScript繧偵い繝・・繝ｭ繝ｼ繝・

    繝悶Λ繧ｦ繧ｶ・壹景mage.jpg 縺｣縺ｦ譖ｸ縺・※縺ゅｋ縺代←縲∽ｸｭ霄ｫ繧定ｦ九◆繧雨avaScript縺｣縺ｽ縺・↑縲ょｮ溯｡後＠縺｡繧・♀縺・ｼ√坂・ **謾ｻ謦・・蜉滂ｼ・*

!!! success "nosniff縺ｮ蜉ｹ譫・

    繝悶Λ繧ｦ繧ｶ・壹系osniff縺瑚ｨｭ螳壹＆繧後※繧九・ontent-Type騾壹ｊ縺ｫ隗｣驥医＠繧医≧縲ら判蜒上→縺励※謇ｱ縺・°繧牙ｮ溯｡後＠縺ｪ縺・坂・ **謾ｻ謦・､ｱ謨暦ｼ・*

**2. X-Frame-Options**
```python
headers['X-Frame-Options'] = 'DENY'
```

!!! warning "謾ｻ謦・・萓具ｼ壹け繝ｪ繝・け繧ｸ繝｣繝・く繝ｳ繧ｰ"

    **謾ｻ謦・・・繧ｵ繧､繝・evil.com 縺ｮ謇句哨・・*

    1. 縲檎┌譁吶・繝ｬ繧ｼ繝ｳ繝茨ｼ√％縺薙ｒ繧ｯ繝ｪ繝・け・√阪→縺・≧繝懊ち繝ｳ繧定｡ｨ遉ｺ
    2. 縺昴・荳九↓縲√≠縺ｪ縺溘・繧ｵ繧､繝医ｒiframe縺ｧ**騾乗・**縺ｫ驥阪・縺ｦ陦ｨ遉ｺ
    3. 縲後・繝ｬ繧ｼ繝ｳ繝医阪・繧ｿ繝ｳ縺ｮ菴咲ｽｮ縺ｫ縲√≠縺ｪ縺溘・繧ｵ繧､繝医・縲悟炎髯､縲阪・繧ｿ繝ｳ繧帝・鄂ｮ

    **邨先棡・・* 繝ｦ繝ｼ繧ｶ繝ｼ縺ｯ縲後・繝ｬ繧ｼ繝ｳ繝茨ｼ√阪ｒ繧ｯ繝ｪ繝・け縺励◆縺､繧ゅｊ縺後∝ｮ滄圀縺ｯ縲悟炎髯､縲阪・繧ｿ繝ｳ繧偵け繝ｪ繝・け縺励※縺・◆

!!! success "DENY縺ｮ蜉ｹ譫・

    縺ゅ↑縺溘・繧ｵ繧､繝医ｒiframe縺ｫ蝓九ａ霎ｼ繧縺薙→繧・*遖∵ｭ｢** 竊・縺薙・謾ｻ謦・′荳榊庄閭ｽ縺ｫ縺ｪ繧・

**3. X-XSS-Protection**
```python
headers['X-XSS-Protection'] = '1; mode=block'
```

!!! warning "謾ｻ謦・・萓具ｼ唸SS・医け繝ｭ繧ｹ繧ｵ繧､繝医せ繧ｯ繝ｪ繝励ユ繧｣繝ｳ繧ｰ・・

    謾ｻ謦・・′URL縺ｫ謔ｪ諢上・縺ゅｋ繧ｹ繧ｯ繝ｪ繝励ヨ繧剃ｻ戊ｾｼ繧・・

    `https://your-app.com/search?q=<script>謔ｪ諢上・縺ゅｋ繧ｳ繝ｼ繝・/script>`

!!! success "1; mode=block縺ｮ蜉ｹ譫・

    繝悶Λ繧ｦ繧ｶ・壹傾SS謾ｻ謦・ｒ讀懃衍・√・繝ｼ繧ｸ縺ｮ陦ｨ遉ｺ繧偵ヶ繝ｭ繝・け縲・

    窶ｻ 迴ｾ莉｣縺ｮ繝悶Λ繧ｦ繧ｶ縺ｯ迢ｬ閾ｪ縺ｮXSS蟇ｾ遲悶′縺ゅｋ縺溘ａ縲√％縺ｮ繝倥ャ繝繝ｼ縺ｯ陬懷勧逧・↑蠖ｹ蜑ｲ

**4. Referrer-Policy**
```python
headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
```

!!! info "Referrer・医Μ繝輔ぃ繝ｩ繝ｼ・峨→縺ｯ"

    縲後←縺ｮ繝壹・繧ｸ縺九ｉ譚･縺溘°縲阪・諠・ｱ

    **萓具ｼ・* A繝壹・繧ｸ縺ｮ繝ｪ繝ｳ繧ｯ繧偵け繝ｪ繝・け 竊・B繝壹・繧ｸ縺ｸ遘ｻ蜍・竊・B繝壹・繧ｸ縺ｯ繝ｪ繝輔ぃ繝ｩ繝ｼ縺ｨ縺励※A繝壹・繧ｸ縺ｮURL繧貞女縺大叙繧・

!!! warning "蝠城｡・

    繝ｪ繝輔ぃ繝ｩ繝ｼ縺ｫ縺ｯURL縺ｮ蜈ｨ菴薙′蜷ｫ縺ｾ繧後ｋ縺薙→縺後≠繧・

    萓具ｼ啻https://your-app.com/user/12345/secret-token`

    竊・URL縺ｫ繝医・繧ｯ繝ｳ繧ИD縺悟性縺ｾ繧後※縺・◆繧・*諠・ｱ貍乗ｴｩ・・*

!!! success "strict-origin-when-cross-origin縺ｮ蜉ｹ譫・

    | 騾∽ｿ｡蜈・| 騾∽ｿ｡蜀・ｮｹ |
    |--------|----------|
    | 蜷後§繧ｵ繧､繝亥・ | 螳悟・縺ｪURL騾∽ｿ｡ |
    | 蛻･繧ｵ繧､繝亥ｮ帙※ | 繝峨Γ繧､繝ｳ縺ｮ縺ｿ騾∽ｿ｡・・https://your-app.com` 縺ｮ縺ｿ・・|

---

## 5. 繧｢繧ｯ繧ｻ繧ｹ蛻ｶ蠕｡

### 5-1. is_email_allowed・医Γ繝ｼ繝ｫ險ｱ蜿ｯ繝√ぉ繝・け・・

```python
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

    if not allowed_emails and not allowed_domains:
        print('笞・・ALLOWED_EMAILS/ALLOWED_DOMAINS 譛ｪ險ｭ螳・)
        return True
    return False
```

#### 1陦後★縺､隗｣隱ｬ

**1-3陦檎岼・夂ｩｺ繝√ぉ繝・け**
```python
def is_email_allowed(email):
    if not email:
        return False
    lower_email = email.lower()
```

```
email = None or ''・育ｩｺ・峨・蝣ｴ蜷・
  竊・if not email: 縺・True
  竊・return False 縺ｧ邨ゆｺ・

email = 'Tanaka@Example.com' 縺ｮ蝣ｴ蜷・
  竊・lower_email = 'tanaka@example.com' 縺ｫ螟画鋤
    ・亥､ｧ譁・ｭ怜ｰ乗枚蟄励ｒ邨ｱ荳縺励※豈碑ｼ・＠繧・☆縺上☆繧具ｼ・
```

**4-5陦檎岼・夊ｨｱ蜿ｯ繝｡繝ｼ繝ｫ繝ｪ繧ｹ繝医・蜿門ｾ・*
```python
allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
allowed_emails = [e.strip().lower() for e in allowed_emails_str.split(',') if e.strip()]
```

**隧ｳ邏ｰ縺ｪ蛻・ｧ｣**
```python
# 迺ｰ蠅・､画焚縺ｮ萓・
# ALLOWED_EMAILS = "tanaka@example.com, yamada@test.com, admin@company.co.jp"

# 繧ｹ繝・ャ繝・: 迺ｰ蠅・､画焚繧貞叙蠕・
allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
# 竊・"tanaka@example.com, yamada@test.com, admin@company.co.jp"
# ・医ｂ縺礼腸蠅・､画焚縺後↑縺代ｌ縺ｰ遨ｺ譁・ｭ・'' 縺ｫ縺ｪ繧具ｼ・

# 繧ｹ繝・ャ繝・: 繧ｫ繝ｳ繝槭〒蛻・牡
parts = allowed_emails_str.split(',')
# 竊・["tanaka@example.com", " yamada@test.com", " admin@company.co.jp"]
#    窶ｻ 遨ｺ逋ｽ縺梧ｮ九▲縺ｦ縺・ｋ

# 繧ｹ繝・ャ繝・: 蜷・ｦ∫ｴ繧貞・逅・
allowed_emails = []
for e in parts:
    cleaned = e.strip()       # 蜑榊ｾ後・遨ｺ逋ｽ繧帝勁蜴ｻ
    if cleaned:               # 遨ｺ縺ｧ縺ｪ縺代ｌ縺ｰ
        allowed_emails.append(cleaned.lower())  # 蟆乗枚蟄励↓縺励※霑ｽ蜉

# 邨先棡
# 竊・["tanaka@example.com", "yamada@test.com", "admin@company.co.jp"]
```

**繝ｪ繧ｹ繝亥・蛹・｡ｨ險倥・隱ｭ縺ｿ譁ｹ**
```python
[e.strip().lower() for e in allowed_emails_str.split(',') if e.strip()]
 笏披楳笏笏笏笏笏笏笏笏笏笏笏笏笏笏・    笏披楳笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏笏・   笏披楳笏笏笏笏笏笏笏笏笏・
    縲御ｽ輔ｒ縺吶ｋ縲・        縲御ｽ輔°繧臥ｹｰ繧願ｿ斐☆縲・             縲梧擅莉ｶ縲・
```

**8-11陦檎岼・夊ｨｱ蜿ｯ繝√ぉ繝・け**
```python
if lower_email in allowed_emails:
    return True
for domain in allowed_domains:
    if lower_email.endswith(domain):
        return True
```

```
繝√ぉ繝・け1: 繝｡繝ｼ繝ｫ繧｢繝峨Ξ繧ｹ縺瑚ｨｱ蜿ｯ繝ｪ繧ｹ繝医↓螳悟・荳閾ｴ縺吶ｋ縺・
  萓・ tanaka@example.com in ["tanaka@example.com", "yamada@test.com"]
  竊・True

繝√ぉ繝・け2: 繝｡繝ｼ繝ｫ繧｢繝峨Ξ繧ｹ縺瑚ｨｱ蜿ｯ繝峨Γ繧､繝ｳ縺ｧ邨ゅｏ繧九°
  萓・ "tanaka@company.co.jp".endswith("@company.co.jp")
  竊・True・井ｼ夂､ｾ縺ｮ繝峨Γ繧､繝ｳ蜈ｨ蜩｡繧定ｨｱ蜿ｯ縺吶ｋ蝣ｴ蜷医↓菴ｿ縺・ｼ・
```

---

### 5-2. get_email_from_token・医ヨ繝ｼ繧ｯ繝ｳ縺九ｉ繝｡繝ｼ繝ｫ蜿門ｾ暦ｼ・

```python
def get_email_from_token(id_token):
    try:
        payload = id_token.split('.')[1]
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += '=' * padding
        decoded = base64.urlsafe_b64decode(payload).decode('utf-8')
        return json.loads(decoded).get('email')
    except:
        return None
```

#### 螳悟・縺ｪ蜃ｦ逅・・豬√ｌ

```python
# 蜈･蜉帙＆繧後ｋJWT繝医・繧ｯ繝ｳ縺ｮ萓・
id_token = "eyJhbGciOiJSUzI1NiJ9.eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9.abc123"

# 繧ｹ繝・ャ繝・: 繝斐Μ繧ｪ繝峨〒蛻・牡
parts = id_token.split('.')
# 竊・["eyJhbGciOiJSUzI1NiJ9", "eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9", "abc123"]
#         繝倥ャ繝繝ｼ                      繝壹う繝ｭ繝ｼ繝・                     鄂ｲ蜷・

# 繧ｹ繝・ャ繝・: 繝壹う繝ｭ繝ｼ繝会ｼ・逡ｪ逶ｮ・峨ｒ蜿門ｾ・
payload = parts[1]
# 竊・"eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9"

# 繧ｹ繝・ャ繝・: 繝代ョ繧｣繝ｳ繧ｰ隱ｿ謨ｴ・・ase64縺ｮ莉墓ｧ倥↓蜷医ｏ縺帙ｋ・・
# Base64縺ｯ4譁・ｭ励★縺､蜃ｦ逅・☆繧九・縺ｧ縲・縺ｮ蛟肴焚縺ｫ縺吶ｋ蠢・ｦ√′縺ゅｋ
padding = 4 - len(payload) % 4  # 菴墓枚蟄苓ｶｳ繧翫↑縺・°
if padding != 4:
    payload += '=' * padding  # '='縺ｧ蝓九ａ繧・

# 繧ｹ繝・ャ繝・: Base64繝・さ繝ｼ繝・
decoded_bytes = base64.urlsafe_b64decode(payload)
# 竊・b'{"email":"tanaka@example.com"}'

# 繧ｹ繝・ャ繝・: 繝舌う繝亥・繧呈枚蟄怜・縺ｫ螟画鋤
decoded_str = decoded_bytes.decode('utf-8')
# 竊・'{"email":"tanaka@example.com"}'

# 繧ｹ繝・ャ繝・: JSON譁・ｭ怜・繧定ｾ樊嶌縺ｫ螟画鋤
data = json.loads(decoded_str)
# 竊・{"email": "tanaka@example.com"}

# 繧ｹ繝・ャ繝・: email繧貞叙蠕・
email = data.get('email')
# 竊・"tanaka@example.com"
```

**蝗ｳ隗｣**
```
JWT繝医・繧ｯ繝ｳ
eyJhbGci...  .  eyJlbWFpbCI...  .  SflKxwRJ...
     |               |               |
  繝倥ャ繝繝ｼ       繝壹う繝ｭ繝ｼ繝・       鄂ｲ蜷・
                     竊・
            split('.')[1]縺ｧ蜿門ｾ・
                     竊・
        eyJlbWFpbCI6InRhbmFrYUBleGFtcGxlLmNvbSJ9
                     竊・
            Base64繝・さ繝ｼ繝・
                     竊・
        {"email":"tanaka@example.com"}
                     竊・
            json.loads()縺ｧ霎樊嶌縺ｫ
                     竊・
            .get('email')縺ｧ蜿門ｾ・
                     竊・
            tanaka@example.com
```

---

## 6. 繝｡繧､繝ｳ繝上Φ繝峨Λ

### 6-1. 繧ｨ繝ｳ繝医Μ繝昴う繝ｳ繝医・螳夂ｾｩ

```python
@functions_framework.http
def app(request):
```

!!! note "@ 縺ｨ縺ｯ・滂ｼ医ョ繧ｳ繝ｬ繝ｼ繧ｿ・・

    ```python
    @functions_framework.http
    def app(request):
    ```

    縲径pp 縺ｨ縺・≧髢｢謨ｰ繧偵？TTP繝ｪ繧ｯ繧ｨ繧ｹ繝医ｒ蜿励￠蜿悶ｋ髢｢謨ｰ縺ｨ縺励※Cloud Run 縺ｫ逋ｻ骭ｲ縺吶ｋ縲阪→縺・≧諢丞袖

    **@・医い繝・ヨ繝槭・繧ｯ・・ 髢｢謨ｰ縺ｫ逶ｮ蜊ｰ繧偵▽縺代ｋ莉慕ｵ・∩**

    | 蠖ｹ蜑ｲ | 隱ｬ譏・|
    |------|------|
    | Cloud Run | 縲悟女莉倅ｿょ供髮・ｸｭ縲・|
    | `def app(request):` | 縲後・縺・ｼ∫ｧ√′蜿嶺ｻ倅ｿゅ〒縺呻ｼ√・|
    | `@functions_framework.http` | 縲後％縺ｮ莠ｺ繧貞女莉倅ｿゅ→縺励※逋ｻ骭ｲ縺励※縺上□縺輔＞縲・|

### 6-2. request繧ｪ繝悶ず繧ｧ繧ｯ繝・

```python
def app(request):
    # request = 繝悶Λ繧ｦ繧ｶ縺九ｉ螻翫＞縺滓ュ蝣ｱ蜈ｨ驛ｨ
```

| 繝励Ο繝代ユ繧｣ | 隱ｬ譏・| 萓・|
|-----------|------|-----|
| `request.method` | HTTP繝｡繧ｽ繝・ラ | `'GET'`, `'POST'` |
| `request.path` | URL縺ｮ繝代せ | `'/'`, `'/api/chat'` |
| `request.headers` | 繝倥ャ繝繝ｼ諠・ｱ | `{'Authorization': 'Bearer xxx'}` |
| `request.get_json()` | 繝懊ョ繧｣・・SON・・| `{'message': '縺薙ｓ縺ｫ縺｡縺ｯ'}` |

### 6-3. 謌ｻ繧雁､

```python
return (HTML_CONTENT, 200, headers)
#         竊・         竊・     竊・
#       譛ｬ譁・    繧ｹ繝・・繧ｿ繧ｹ  繝倥ャ繝繝ｼ
```

| 繧ｹ繝・・繧ｿ繧ｹ繧ｳ繝ｼ繝・| 諢丞袖 |
|-----------------|------|
| `200` | 謌仙粥 |
| `400` | 繝ｪ繧ｯ繧ｨ繧ｹ繝医′荳肴ｭ｣・亥・蜉帙お繝ｩ繝ｼ・・|
| `401` | 隱崎ｨｼ縺悟ｿ・ｦ・ｼ医Ο繧ｰ繧､繝ｳ縺励※縺・↑縺・ｼ・|
| `403` | 讓ｩ髯舌↑縺暦ｼ医Ο繧ｰ繧､繝ｳ貂医∩縺縺瑚ｨｱ蜿ｯ縺輔ｌ縺ｦ縺・↑縺・ｼ・|
| `404` | 繝壹・繧ｸ縺瑚ｦ九▽縺九ｉ縺ｪ縺・|
| `500` | 繧ｵ繝ｼ繝舌・繧ｨ繝ｩ繝ｼ |

---

## 縺ｾ縺ｨ繧・

縺薙・繝峨く繝･繝｡繝ｳ繝医〒蟄ｦ繧薙□Python讒区枚・・

| 讒区枚 | 諢丞袖 | 萓・|
|------|------|-----|
| `dict['key'] = value` | 霎樊嶌縺ｫ蛟､繧定ｿｽ蜉 | `headers['Content-Type'] = 'text/html'` |
| `x in list` | 繝ｪ繧ｹ繝医↓蜷ｫ縺ｾ繧後ｋ縺・| `'*' in ALLOWED_ORIGINS` |
| `a or b` | a縺後≠繧後・a縲√↑縺代ｌ縺ｰb | `origin or '*'` |
| `with open() as f:` | 繝輔ぃ繧､繝ｫ繧貞ｮ牙・縺ｫ髢九￥ | 繝輔ぃ繧､繝ｫ隱ｭ縺ｿ霎ｼ縺ｿ |
| `base64.decode()` | Base64繧偵ョ繧ｳ繝ｼ繝・| 繝医・繧ｯ繝ｳ隗｣譫・|
| `@decorator` | 髢｢謨ｰ縺ｫ逶ｮ蜊ｰ繧偵▽縺代ｋ | `@functions_framework.http` |
| `[x for x in list]` | 繝ｪ繧ｹ繝亥・蛹・｡ｨ險・| 繝｡繝ｼ繝ｫ繝ｪ繧ｹ繝医・蜃ｦ逅・|

