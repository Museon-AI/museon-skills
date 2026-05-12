# Pitch Deck 字段地图

> Step 1 产出:整张 Pitch Deck 的字段拆解总表
> 用途:研发对接、JSON Schema 设计、prompt 编写的字段索引
> 版本:v1 · 2026-05-12

---

## 1. 总览

### 1.1 拆解范围

- **覆盖区域**:Part 1 至 Part 5 全部内容,Path 详情页 5 张
- **已剔除**:Track Record 区块(暂不纳入模板)
- **当前阶段**:仅支持 `primary_goal = conversion`;Awareness 版作为未来扩展点保留接口

### 1.2 字段类型

| 类型 | 含义 | 数量 |
|---|---|---|
| **A** | 写死在模板里,不随客户变 | 大量(机制描述、章节标题、套餐配置、决策树、按钮文本) |
| **A 可枚举** | 当前固定,未来支线切换时启用 | 2 个(`key_signal_word` / `key_signal_action`) |
| **B-info** | 从客户信息表直接抄 | 7 个上游字段 |
| **B-report** | 从创意调研报告直接抄 | 8 个字段 |
| **C** | Agent 推理生成 | 17 个核心推理字段 |
| **资源(非 prompt)** | 图片资源,由设计师人工产出,Agent 输出 null | 1 个(`path_museon_version_image`) |

### 1.3 整体输入输出

```
输入:
  ① 客户信息表(JSON,Chatbot 在 A → B-① 阶段收集)
  ② 创意调研报告(B 阶段全流程产出,5 个 Part)

输出:
  Pitch Deck 数据 JSON(主 Agent 一次性生成,前端渲染)
```

---

## 2. 客户信息表 → Deck 字段映射

只列举 deck 中实际使用的信息表字段。其余 12 个 machine_key 在调研 B 阶段使用,deck 渲染层不直接消费。

| 信息表字段 (machine_key) | 用途 | 派生出的 deck 字段 |
|---|---|---|
| `product_name` | 客户产品名 | `client_name`(全 deck 复用) |
| `one_line_positioning` | 产品一句话定位 | 派生 `product_category` |
| `audience_segments` | 受众 | 派生 `audience_list`、`use_context`、scenario 系列 |
| `core_selling_points` | 核心卖点 | 派生 `user_save_motivation`、`universal_pain_quote`、scenario 系列 |
| `core_features` | 核心功能 | 派生 path_description 子变量、`recommended_badge` 判断树 |
| `primary_goal` | 曝光 or 转化 | **全局支线开关**(当前固定 conversion);`recommended_badge` 判断树 |
| `strategy_mode` | 复制 or 探索 | `recommended_badge` 判断树、scenario 系列 |
| `overseas_social_experience` | 海外社媒经验 | `recommended_badge` 判断树、scenario 系列 |

---

## 3. 全 deck 共享字段

| 字段 ID | 类型 | 来源 | 备注 |
|---|---|---|---|
| `client_name` | B-info | 信息表 `product_name` | 整张 deck 高频引用,只存一次 |
| `product_category` | B-info | 信息表 `one_line_positioning` 提取品类词 | 例如 "AI Agent" / "AI 笔记工具" |
| `total_views` | C | 调研报告 2.1 Reference Pool views 加总,化成 "XXX 万+" | Part 1、Part 2 共用 |
| `key_signal_word` | A 可枚举 | 当前固定 = "收藏" | 未来 awareness 切 "分享/传播" |
| `key_signal_action` | A 可枚举 | 当前固定 = "收藏" | 同上,动词形式 |

---

## 4. Part 1 字段(开篇 Hero + 三张卡片)

| 字段 ID | 在 deck 里的位置 | 类型 | 来源 / 推理 | 语言 |
|---|---|---|---|---|
| `nav_labels` | 顶部 nav:"方向/机制/方案" | A | 写死 | 中 |
| `hero_kicker` | "Personalized Pitch · Prepared for {client_name}" | A 的壳 + B-info | 嵌 `client_name` | 中英混 |
| `hero_title` | "{client_name} 的矩阵号 方案创意调研" | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `hero_subtitle` | "基于 {client_name} 的核心卖点 + TikTok 热门关键词,我们筛出 5 个高潜力内容方向,每一个都对应一个具体的 {use_context} 场景。" | A 的壳 + B-info + C | 嵌 `client_name`、`use_context` | 中 |
| `use_context` | hero_subtitle 末尾 "用户 X 场景" 的 X | **C** | Agent 推理(详见 reasoning-spec §C-01) | 中 |
| `card_1_title` | "5 条定制内容方向" | A | 写死 | 中 |
| `card_1_desc` | "基于 {total_views} 播放的 TikTok 爆款验证,为 {client_name} 定制。" | A 的壳 + C + B-info | 嵌 `total_views`、`client_name` | 中 |
| `card_2_title` / `card_2_desc` | "1 套动态测试机制" + 描述 | A | 写死 | 中 |
| `card_3_title` / `card_3_desc` | "2 种推进方案" + 描述 | A | 写死(套餐数字也写死) | 中 |

**Part 1 给 Agent 的活**:2 个 C 字段(`total_views`、`use_context`)+ 嵌 `client_name`

---

## 5. Part 2 字段(方法论:我们怎么想出这 5 个方向)

| 字段 ID | 位置 | 类型 | 来源 / 推理 | 语言 |
|---|---|---|---|---|
| `section_2_heading` | 标题 | A | 写死 | 中 |
| `opening_para_1` | 开场段 1(关于"不要直接讲品类") | A 的壳 + B-info + C | 嵌 `client_name`、`product_category`、`user_save_motivation` | 中 |
| `user_save_motivation` | 段 1 心理活动 quote | **C** | Agent 推理(详见 §C-02) | 中 |
| `opening_para_2` | 段 2(关于"分析了多少播放") | A 的壳 + 复用 + C | 嵌 `total_views`、`category_modifier`、`anxiety_keywords` | 中 |
| `category_modifier` | 段 2 "{X} 工具" | **C** | Agent 推理(详见 §C-03) | 中 |
| `anxiety_keywords` | 段 2 末尾 3 个焦虑词 | **C** | Agent 推理(详见 §C-04) | 中英混(优先英文) |
| `opening_para_3` | 段 3(过渡到三步法) | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `step_1.title` | "拆解爆款情绪" | A | 写死 | 中 |
| `step_1.subtitle` | "从 TikTok 爆款中提取最容易触发 {key_signal_word} 的 5 种情绪时刻" | A 的壳 + 复用 | 嵌 `key_signal_word` | 中 |
| `emotion_list[]` | Step 1 卡片 5 个情绪条目 | **C(数组)** | Agent 推理(详见 §C-05) | 中 |
| `step_1.footer` | "这 5 种情绪覆盖了 {client_name} 目标用户({audience_list})最高频的 {anxiety_type}" | A 的壳 + 嵌 | 嵌多字段 | 中 |
| `audience_list` | step_1.footer 简化受众标签 | **C** | Agent 推理(详见 §C-06) | 中 |
| `anxiety_type` | step_1.footer 末尾"X 焦虑" | **C** | Agent 推理(详见 §C-07) | 中 |
| `step_2.title` | "匹配 {client_name} 能力" | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `step_2.subtitle` | "每个情绪痛点对应一个具体的 {client_name} 卖点" | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `capability_list[]` | Step 2 卡片 5 个卖点 | **B-report** | 调研报告 Part 3 各方向"对应 Manus 卖点"字段直接抄 | 中 |
| `step_2.emotion_to_capability[]` | Step 2 卡片 5 条映射 | 复用 | `emotion_list[i].label` ↔ `capability_list[i]` 一一对应 | — |
| `step_2.footer` | "不依赖 {product_category} 这个抽象概念..." | A 的壳 + B-info | 嵌 `product_category` | 中 |
| `step_3.title` / `step_3.subtitle` | "定制 5 个内容方向" + 副标 | A | 写死 | 中 |
| `step_3.big_text` | "我们为 {client_name} 定制了 5 条内容方向。" | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `universal_pain_quote` | Step 3 大 Quote | **C** | Agent 推理(详见 §C-08) | 中 |
| `step_3.footer` | "下面是这 5 条方向" | A | 写死 | 中 |

**Part 2 给 Agent 的活**:7 个核心 C 字段(`user_save_motivation`、`category_modifier`、`anxiety_keywords`、`emotion_list`、`audience_list`、`anxiety_type`、`universal_pain_quote`)+ 1 个 B-report 数组(`capability_list[]`)

---

## 6. Part 3 卡片层字段(5 张方向卡片)

每张卡片字段相同,以下是**单张卡片字段**(`paths[i]`),整张 deck 重复 5 次。

| 字段 ID | 位置 | 类型 | 来源 / 推理 | 语言 |
|---|---|---|---|---|
| `section_3_heading` | 标题 "5 个方向具体是什么" | A | 写死 | 中 |
| `section_3_opening` | "每一个方向,都源自一个已经被用户 {key_signal_action} 了数十万次的真实痛点场景。" | A 的壳 + 复用 | 嵌 `key_signal_action` | 中 |
| `path_index` | 卡片左上角 "01" | A | 数组下标 + 1 | — |
| `path_audience_label` | "Student / Deadline Panic" | **C** | Agent 推理(详见 §C-09) | **英** |
| `path_views` | "613K views" | B-report | 调研报告 2.1 Reference Pool views 字段 | **英** |
| `path_likes` | "70K likes" | B-report | 调研报告 2.1 Reference Pool likes 字段 | **英** |
| `path_hook_quote` | 卡片大字 quote "I need a deck by tomorrow." | **C** | Agent 推理(详见 §C-10) | **英** |
| `path_description` | 卡片底部 2 句话说明 | **C** | Agent 推理(详见 §C-11) | **英** |
| `cta_button_text` | 按钮 "See creative direction & script" | A | 写死 | 英 |

**卡片顺序锁定 = 调研报告 3.1 → 3.5 顺序,Agent 不重排。**

---

## 7. Part 3 详情层字段(每张 Path 点开后的详情页)

每张卡片对应一个详情页,字段结构相同。以下字段属于 `paths[i]` 的细节层。

| 字段 ID | 位置 | 类型 | 来源 / 推理 | 语言 |
|---|---|---|---|---|
| `path_capability_label` | 详情页顶部"对应卖点" | B-report | 调研报告 3.X "对应 Manus 卖点"字段,Agent 翻译成英文 | **英** |
| `path_slideshow_script[]` | 左侧 SLIDESHOW 脚本结构 | B-report | 调研报告 3.X "Slideshow 脚本结构"字段原文搬运,每步一个数组 item | 中 |
| `path_test_hooks[]` | 左侧 测试 HOOKS,3-5 个候选 | **C** | Agent 推理(详见 §C-12) | **英** |
| `path_move_to` | 左侧 后续拓展(Move to) | B-report | 调研报告 4.4 第二周放量逻辑表对应行 | 中 |
| `path_market_ref_image` | 右侧 MARKET REFERENCE 截图 | 资源 | 调研报告 2.1 Reference 视频截图(图片资源) | — |
| `path_market_ref_comment` | 截图下方一句话点评 | **C** | Agent 推理(详见 §C-13) | 中 |
| `path_museon_version_image` | 右侧 MUSEON 定制版截图 | **资源(非 prompt)** | 设计师人工产出,prompt 输出此字段为 null,等后续回填 | — |
| `path_museon_version_comment` | 截图下方一句话点评 | **C** | Agent 推理(详见 §C-14) | 中 |

**Part 3 总给 Agent 的活**(卡片 + 详情):
- 卡片层每张 × 3 个 C 字段 = 15 个 C 子任务
- 详情层每张 × 3 个 C 字段 = 15 个 C 子任务
- 共 30 个 C 子任务(`paths[]` 数组级别)

---

## 8. Part 4 字段(测试机制)

Part 4 几乎全 A 类,只嵌入 `client_name` 和 `key_signal_word`。

| 字段 ID | 位置 | 类型 | 来源 | 备注 |
|---|---|---|---|---|
| `section_4_heading` | 标题 | A | 写死 | — |
| `opening_para` | 开场段 | A | 写死 | — |
| `step_1.title` | "决策树" | A | 写死 | — |
| `step_1.metric_intro` | "我们盯两个指标" | A | 写死 | 当前 conversion 版默认 |
| `step_1.metric_1` | "avg views — hook 抓不抓人" | A | 写死 | 当前 conversion 版默认 |
| `step_1.metric_2` | "save rate — 用户是不是觉得「以后还用得上」" | A | 写死 | 当前 conversion 版默认 |
| `step_1.tree_diagram` | 决策树图 | A | 写死(SVG/前端组件) | — |
| `step_1.tree_data_destination` | 树中 "Data checkpoint shared with {client_name}" | A 的壳 + B-info | 嵌 `client_name` | — |
| `step_1.threshold_low/mid/high` | < 300 / 300-1000 / > 1000 三档阈值 | A | 写死 | 当前 conversion 版默认 |
| `step_1.description` | 决策树文字说明 | A | 写死 | — |
| `step_1.faq[]` | 2 个折叠 FAQ(baseline / SCALE) | A | 写死(纯方法论,不随客户变) | — |
| `step_2.title` | "5 个方向之间的进化" | A | 写死 | — |
| `step_2.intro` | 进化机制开场 | A | 写死 | — |
| `step_2.evolution_types[]` | 3 类沉淀物(人设/hook 公式/卖点表达) | A 的壳 + 复用 | 第 3 类嵌 `key_signal_word` | — |
| `step_2.loop_diagram` | 4 步循环图 | A | 写死 | — |
| `step_2.examples[]` | 3 个例子(Path 02/01/04) | A | **完全写死**,所有客户一样 | — |
| `step_2.closing` | "X 拿到的最终内容资产..." | A 的壳 + B-info | 嵌 `client_name` | — |
| `closing_para` | Part 4 整体收尾 | A 的壳 + B-info | 嵌 `client_name` | — |
| `cta_button` | "见 4 种数据组合的应对参考" | A | 写死(详情页内容也是 A) | — |

**Part 4 给 Agent 的活**:0,纯模板渲染。

---

## 9. Part 5 字段(套餐推荐)

| 字段 ID | 位置 | 类型 | 来源 / 推理 | 语言 |
|---|---|---|---|---|
| `section_5_heading` | "{client_name} 怎么开始" | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `opening_para` | 开场段 | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `package_a.label/name/price/fit_tagline/deliverables/cta` | 5 Creators 套餐配置 | A | 全部写死 | 中英混 |
| `package_a.scenario` | A 套餐客户处境描述 | **C** | Agent 推理(详见 §C-15) | 中 |
| `package_a.core_value` | A 套餐核心价值 | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `package_b.recommended_badge` | "推荐"角标 | **C(决策型)** | Agent 推理(详见 §C-16) | — |
| `package_b.label/name/price/fit_tagline/deliverables/cta` | 20 Creators 套餐配置 | A | 全部写死 | 中英混 |
| `package_b.scenario` | B 套餐客户处境描述 | **C** | Agent 推理(详见 §C-15,与 scenario_a 同节) | 中 |
| `package_b.core_value` | B 套餐核心价值 | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `comparison_section.heading` | "同一套机制,两种推进节奏" | A | 写死 | 中 |
| `comparison_section.diagram` | 左右对照图 | A | 写死(前端组件) | — |
| `comparison_section.bottom_note` | "两个方案都让 {client_name}..." | A 的壳 + B-info | 嵌 `client_name` | 中 |
| `our_recommendation` | 整段"我们的建议" | **C** | Agent 推理(详见 §C-17) | 中 |

**Part 5 给 Agent 的活**:3 个 C 字段(`scenario_a` / `scenario_b` / `our_recommendation`)+ 1 个决策型 C(`recommended_badge`)

---

## 10. C 字段索引表

按 Part 顺序列出所有 17 个 C 字段,详见 `reasoning-spec.md`。

| 编号 | 字段 ID | 所在 Part | 推理难度 |
|---|---|---|---|
| C-01 | `use_context` | Part 1 | 低 |
| C-02 | `user_save_motivation` | Part 2 | 中 |
| C-03 | `category_modifier` | Part 2 | 低 |
| C-04 | `anxiety_keywords` | Part 2 | 中 |
| C-05 | `emotion_list[]` | Part 2 | **高(数组,5 项)** |
| C-06 | `audience_list` | Part 2 | 低 |
| C-07 | `anxiety_type` | Part 2 | 低 |
| C-08 | `universal_pain_quote` | Part 2 | **高(灵魂句)** |
| C-09 | `path_audience_label` | Part 3 卡片 | 中 |
| C-10 | `path_hook_quote` | Part 3 卡片 | **高(数组,5 个)** |
| C-11 | `path_description` | Part 3 卡片 | **高(数组,5 个 × 5 子变量)** |
| C-12 | `path_test_hooks[]` | Part 3 详情 | **高(数组,5×3-5 个)** |
| C-13 | `path_market_ref_comment` | Part 3 详情 | 中(数组,5 项) |
| C-14 | `path_museon_version_comment` | Part 3 详情 | 中(数组,5 项) |
| C-15 | `scenario_a` / `scenario_b` | Part 5 | 中 |
| C-16 | `recommended_badge` | Part 5 | **决策型** |
| C-17 | `our_recommendation` | Part 5 | 中 |

---

## 11. 字段 ID 总索引(按字母排序)

```
anxiety_keywords          → §5 Part 2 / §10 C-04
anxiety_type              → §5 Part 2 / §10 C-07
audience_list             → §5 Part 2 / §10 C-06
capability_list[]         → §5 Part 2 (B-report)
card_1_title / desc       → §4 Part 1 (A 类)
category_modifier         → §5 Part 2 / §10 C-03
client_name               → §3 全局共享 (B-info)
emotion_list[]            → §5 Part 2 / §10 C-05
hero_kicker / title / subtitle  → §4 Part 1
key_signal_word / action  → §3 全局共享 (A 可枚举)
nav_labels                → §4 Part 1 (A 类)
opening_para_1/2/3        → §5 Part 2
our_recommendation        → §9 Part 5 / §10 C-17
package_a / package_b     → §9 Part 5
path_audience_label       → §6 Part 3 卡片 / §10 C-09
path_capability_label     → §7 Part 3 详情 (B-report)
path_description          → §6 Part 3 卡片 / §10 C-11
path_hook_quote           → §6 Part 3 卡片 / §10 C-10
path_index                → §6 Part 3 卡片 (A)
path_likes                → §6 Part 3 卡片 (B-report)
path_market_ref_comment   → §7 Part 3 详情 / §10 C-13
path_market_ref_image     → §7 Part 3 详情 (资源)
path_move_to              → §7 Part 3 详情 (B-report)
path_museon_version_comment  → §7 Part 3 详情 / §10 C-14
path_museon_version_image    → §7 Part 3 详情 (资源,非 prompt)
path_slideshow_script[]   → §7 Part 3 详情 (B-report)
path_test_hooks[]         → §7 Part 3 详情 / §10 C-12
path_views                → §6 Part 3 卡片 (B-report)
product_category          → §3 全局共享 (B-info 派生)
recommended_badge         → §9 Part 5 / §10 C-16 (决策型)
scenario_a / scenario_b   → §9 Part 5 / §10 C-15
section_X_heading         → 各 Part (A 类)
step_1 / step_2 / step_3  → §5 Part 2、§8 Part 4
total_views               → §3 全局共享 (C)
universal_pain_quote      → §5 Part 2 / §10 C-08 (灵魂句)
use_context               → §4 Part 1 / §10 C-01
```

---

## 12. 当前阶段边界与未来扩展点

### 12.1 当前固定项

- `primary_goal = conversion`(默认且唯一)
- `key_signal_word = "收藏"`
- 套餐数字(5 Creators / 20 Creators / 价格 / 模版数)写死
- 决策树阈值(< 300 / 300-1000 / > 1000)写死
- Part 4 进化机制例子(Path 02/01/04)所有客户一样
- 卡片顺序绑定调研报告 3.1 → 3.5 顺序

### 12.2 未来扩展点(已预留接口)

- **Awareness 支线**:`primary_goal = awareness` 时,启用 awareness 版叙事
  - `key_signal_word` 切 "分享" / "传播"
  - Part 4 主指标切 share rate / avg views
  - Part 5 推荐逻辑调整
- **Track Record 模块**:当前移除,未来按客户行业匹配 case 时启用
- **行业 baseline 表**:决策树阈值未来支持按客户行业调整
- **多语言输出**:当前固定中文骨架 + Part 3 paths[] 英文,未来可支持全英文 deck

### 12.3 已知不在 prompt 范围内的事

- `path_museon_version_image`:MuseOn 设计师人工产出
- 决策树 SVG 图、套餐对照图:前端组件,prompt 不输出
- 套餐购买跳转:前端路由,prompt 不输出

---

> 下一步参考:`reasoning-spec.md`(17 个 C 字段的详细推理逻辑)
