# C 字段推理逻辑手册

> 配套文档:`field-map.md`
> 用途:Step 3 写 prompt 的直接素材,每个 C 字段的推理指令、好坏判断、Manus 填充示例
> 版本:v1 · 2026-05-12

---

## 阅读说明

每个 C 字段一节,统一 6 段结构:

1. **作用**:这个字段在 deck 里的角色,为什么需要它
2. **输入字段**:推理时 Agent 能读到的上游信息
3. **输出结构**:期望的输出形态(句式、字段类型、长度)
4. **推理步骤**:Agent 内部应该走的判断流程
5. **好的输出 vs 坏的输出**:正反例对比
6. **Manus 填充示例**:本字段用于 Manus 这个客户时,应该长什么样

写 prompt 时,把每节的 1-5 段翻译成对 Agent 的指令,第 6 段作为 few-shot 示例。

---

## C-01:use_context

### 作用

Part 1 hero_subtitle 末尾 "每一个方向,都对应一个具体的 {use_context} 场景"。这个字段告诉客户:"我们设计内容时,是基于真实使用场景的"。换客户场景域要变。

### 输入字段

- 信息表 `audience_segments`
- 信息表 `core_selling_points`

### 输出结构

**2-4 字中文短语**,描述客户产品的"场景域"。结构:`{场景域}场景`。

### 推理步骤

1. 读 `core_selling_points`,确定产品解决的核心场景
2. 读 `audience_segments`,确认场景跟受众匹配
3. 选一个最能覆盖产品多个用例的"场景域"短语

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus → "用户任务" | "产品使用"(空泛) |
| AI 笔记工具 → "用户工作" | "用户场景"(等于没说) |
| AI 简历工具 → "用户求职" | "AI 应用"(产品视角不是用户视角) |
| AI 设计工具 → "用户设计工作" | "日常生活"(太大) |

### Manus 填充示例

```
"用户任务"
```

完整句子:"...每一个都对应一个具体的**用户任务**场景。"

---

## C-02:user_save_motivation

### 作用

Part 2 段 1 心理活动 quote:"他们决定收藏一条内容的时候,脑子里想的是「{user_save_motivation}」"。这是从**用户视角**说出"收藏一条 TikTok 时心里在想什么",证明我们读懂了用户的"未来再用"心理。

### 输入字段

- 信息表 `primary_goal`(当前固定 = conversion)
- 信息表 `audience_segments`
- 信息表 `core_selling_points`

### 输出结构

**8-15 字中文短句**,第一人称、未来时态、带具体场景。结构:`下一次/下次 {具体场景},我 {用产品的动作}`。

### 推理步骤

1. 从 `audience_segments` + `core_selling_points` 提炼"用户最常遇到产品能解决的场景"
2. 用第一人称、未来时态写出心理活动
3. 检查:是不是 < 15 字、是不是带场景、是不是有"以后还用得到"的暗示

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus → "下一次遇到这个麻烦的任务,我要用这个工具" | "用户会觉得这个工具有用"(第三人称) |
| AI 笔记工具 → "下次开会前,我要打开它" | "这个工具很有用"(无场景) |
| AI 简历工具 → "下次投简历前,我先丢给它过一遍" | "我应该买这个"(转化意图过强,不是收藏心理) |

### Manus 填充示例

```
"下一次遇到这个麻烦的任务,我要用这个工具"
```

---

## C-03:category_modifier

### 作用

Part 2 段 2 "我们分析了 TikTok 上累计 {total_views} 播放的 {category_modifier} 爆款 reference"。说明我们参考的 reference 池属于哪一类爆款,要比 `product_category` 抽象一层,这样不会让客户觉得我们只看 Agent 类爆款。

### 输入字段

- 全局字段 `product_category`
- 信息表 `one_line_positioning`

### 输出结构

**2-5 字中文短语**,描述产品所属的**大类目**。比 `product_category` 抽象一层。

### 推理步骤

1. 读 `product_category`,确定产品的具体定位
2. 向上抽一层:这个具体定位属于哪一类工具?
3. 选最常见的工具大类目作为修饰词

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus(AI Agent) → "AI 工具" | "AI Agent"(等于 product_category 没变) |
| AI 笔记工具 → "效率工具" 或 "笔记工具" | "AI 笔记"(太具体) |
| AI 简历工具 → "求职工具" 或 "效率工具" | "AI"(太抽象) |
| AI 设计工具 → "设计工具" | "工具"(无信息量) |

### Manus 填充示例

```
"AI 工具"
```

---

## C-04:anxiety_keywords

### 作用

Part 2 段 2 末尾 "让用户在 {anxiety_keywords} 这些熟悉的焦虑里看见这个工具能解决什么"。列举 3 个用户最常焦虑的具体场景词,证明我们看到了用户在什么场景下会焦虑。

### 输入字段

- 调研报告 Part 3 五方向(`方向定位` + `适合人群`)

### 输出结构

**3 个高频焦虑词**,顿号连接。**优先英文动作词**(deadline、research、workflow 这种,用户更有感),允许中文。每个词 1-2 个单词或字。

### 推理步骤

1. 读调研报告 Part 3 五个方向的"方向定位 + 适合人群"
2. 从五个方向里提炼出每个方向背后的"用户焦虑场景词"
3. 选 3 个最高频、最有代表性的
4. 优先选英文动作词

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus → "deadline、research、workflow" | "学习、工作、生活"(太泛) |
| AI 笔记工具 → "meeting、lecture、brainstorming" | "用户的需求"(不是焦虑词) |
| AI 简历工具 → "interview、cold email、portfolio" | "焦虑、压力、困扰"(都是情绪不是场景) |

### Manus 填充示例

```
"deadline、research、workflow"
```

---

## C-05:emotion_list[]

### 作用

Part 2 Step 1 卡片里展示 5 个"用户情绪标签",每个情绪标签后面跟一句简短描述。这是 Part 2 三步法的第一步,证明我们读懂了用户的痛。**整个 Part 2 的灵魂数组**。

### 输入字段

- 调研报告 Part 3 五个方向("方向定位" + "创意设计逻辑")

### 输出结构

**5 个对象的数组**,顺序对应调研报告 3.1 → 3.5。每个对象:

```json
{
  "label": "4-8 字情绪标签",
  "description": "10-15 字情绪具象化描述"
}
```

### 推理步骤

1. 对调研报告 3.1 → 3.5 每个方向,**反向从产品视角倒推到用户视角**
2. 提炼这个方向背后,用户**正在经历的情绪**(不是产品在做什么)
3. label 部分:4-8 字短语,带情绪温度词("恐慌""混乱""摩擦""卡点""犹豫"等)
4. description 部分:10-15 字,把情绪具象化,讲清楚"在什么场景下感受到这个情绪"

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| `{"label":"Deadline 前的恐慌","description":"截止日前的焦虑和压力"}` | `{"label":"用户很焦虑","description":"用户感觉时间不够用"}`(无场景、情绪平) |
| `{"label":"工作流的摩擦","description":"流程太复杂、跨工具"}` | `{"label":"任务很复杂","description":"完成任务需要很多步骤"}`(产品视角不是用户情绪) |
| `{"label":"ChatGPT 的卡点","description":"能回答但完不成任务"}` | `{"label":"AI 不够好","description":"现有 AI 工具有局限"}`(抽象,缺少对比的具体性) |

### Manus 填充示例

```json
[
  {"label":"Deadline 前的恐慌","description":"截止日前的焦虑和压力"},
  {"label":"查文献的混乱","description":"资料多、步骤繁琐"},
  {"label":"工作流的摩擦","description":"流程太复杂、跨工具"},
  {"label":"ChatGPT 的卡点","description":"能回答但完不成任务"},
  {"label":"选工具的犹豫","description":"不知道该用哪个 AI"}
]
```

---

## C-06:audience_list

### 作用

Part 2 step_1.footer "这 5 种情绪覆盖了 {client_name} 目标用户({audience_list})最高频的 {anxiety_type}"。括号里的简化受众标签。

### 输入字段

- 信息表 `audience_segments`

### 输出结构

**4 个左右的简化中文标签**,顿号连接。把信息表里的完整画像名压缩成 3-5 字短标签。

### 推理步骤

1. 读 `audience_segments` 完整列表(通常 3-5 类)
2. 每类压缩成 3-5 字标签(去掉"用户""人群"等冗余)
3. 顿号连接

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus → "学生、PHD、职场白领、AI 工具用户" | "本科生 / 大学生、PHD / 研究生、职场白领 / 知识工作者、AI 工具重度用户 / Early Adopters"(原文搬运太长) |
| AI 笔记工具 → "学生、咨询、产品经理、研究者" | "所有需要记笔记的人"(无信息量) |

### Manus 填充示例

```
"学生、PHD、职场白领、AI 工具用户"
```

---

## C-07:anxiety_type

### 作用

Part 2 step_1.footer 末尾 "最高频的 {anxiety_type}"。给 5 个情绪一个统称。

### 输入字段

- 信息表 `audience_segments`
- 信息表 `core_selling_points`
- `emotion_list[]`

### 输出结构

**3-5 字中文短语**,结构:`{域}焦虑`。

### 推理步骤

1. 看 `emotion_list[]` 5 个情绪标签的共同主题
2. 选一个能涵盖 5 种情绪的"焦虑域"
3. 拼成 "X 焦虑"

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus → "任务焦虑" | "焦虑"(无修饰) |
| AI 笔记工具 → "信息焦虑" 或 "记录焦虑" | "用户焦虑"(主语错位) |
| AI 简历工具 → "求职焦虑" | "工作焦虑"(范围太大) |

### Manus 填充示例

```
"任务焦虑"
```

---

## C-08:universal_pain_quote(灵魂句)

### 作用

Part 2 Step 3 大 Quote,整张 deck 最重要的 1 句话。整个方法论的情绪落点,所有 5 个方向最终都指向这一句。

### 输入字段

- `emotion_list[]`(Part 2 已生成)
- 信息表 `core_selling_points`
- 信息表 `audience_segments`
- 全局字段 `client_name`

### 输出结构

**固定句式**:`{15 字以内的痛点陈述},但 {client_name} 可以直接帮你 {2-3 字动词}。`

两个子部分:
- `universal_pain`:15 字以内,用户视角的痛点陈述
- `action_verb`:2-3 字产品核心动词

### 推理步骤

1. 读 `emotion_list[]` 5 个情绪,找最大公约数
2. 把最大公约数用一句 15 字以内的话表达出来(用户视角,不是产品视角)
3. 从 `core_selling_points` 提炼产品的核心动作动词(2-3 字)
4. 拼成固定句式:`{痛},但 {client_name} 可以直接帮你 {动词}。`

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus → "这个任务原本很麻烦,但 Manus 可以直接帮你完成" | "Manus 是一个 AI Agent"(没痛点) |
| AI 笔记工具 → "重要的灵感总是记不住,但 [X] 可以直接帮你记下来" | "你应该用我们的产品"(无信息量) |
| AI 简历工具 → "好简历改一遍要一整天,但 [X] 可以直接帮你写好" | "求职很难,但我们能帮你"(抽象) |
| AI 设计工具 → "画出脑子里的画面要一整天,但 [X] 可以直接帮你画出来" | "用户在求职过程中有很多焦虑"(第三人称) |

### Manus 填充示例

```
"这个任务原本很麻烦,但 Manus 可以直接帮你完成。"
```

---

## C-09:path_audience_label

### 作用

Part 3 每张方向卡片左上角的英文受众标签,2 段英文,中间斜杠分隔。格式如 "Student / Deadline Panic"。

### 输入字段

- 调研报告 3.X "方向定位" + "适合人群"

### 输出结构

**2-3 段英文短语**,斜杠分隔。结构:`{身份} / {情绪场景}` 或 `{身份} / {场景}`。

### 推理步骤

1. 从调研报告 3.X "适合人群" 提取身份(Student / Founder / Programmer / 等)
2. 从调研报告 3.X "方向定位" + "创意设计逻辑" 提取情绪场景或使用场景
3. 翻译成英文,斜杠分隔

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "Student / Deadline Panic" | "学生 / 截止日"(没翻译) |
| "Founder / Solo Business" | "Entrepreneur"(只有身份没有场景) |
| "AI Tools Power User" | "AI User"(太泛) |

### Manus 填充示例

```
Path 01: "Student / Deadline Panic"
Path 02: "Student / PHD / Research"
Path 03: "Founder / Solo Business"
Path 04: "AI Tools Power User"
Path 05: "Programmer / Developer"
```

---

## C-10:path_hook_quote

### 作用

每张方向卡片中间的英文大字 quote,1 句用户口吻的痛点 hook。是卡片的视觉焦点。

### 输入字段

- 调研报告 3.X "方向定位" + "创意设计逻辑"
- `path_audience_label`

### 输出结构

**< 10 词英文短句**,用户第一人称口吻,带情绪或对比张力。带英文引号。

### 推理步骤

1. 读调研报告 3.X 完整内容,提炼这个方向的"灵魂痛点"
2. 转成第一人称 + 口语化 + 短(< 10 词)
3. 加引号

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "I need a deck by tomorrow." | "Manus helps students with deadlines."(第三人称) |
| "Turn messy research into a brief." | "Get your research done faster with AI."(太抽象) |
| "ChatGPT answers. Manus finishes." | "Manus is better than ChatGPT."(产品视角) |
| "Which AI tool actually gets work done?" | "Save time on coding."(太通用) |

### Manus 填充示例

```
Path 01: "I need a deck by tomorrow."
Path 02: "Turn messy research into a brief."
Path 03: "Let Manus run the workflow."
Path 04: "ChatGPT answers. Manus finishes."
Path 05: "Which AI tool actually gets work done?"
```

---

## C-11:path_description(5 子变量)

### 作用

每张方向卡片底部的 2 句话英文说明,解释"为什么这个方向能跑通 + Manus 凭什么是更好的解法"。

### 输入字段

- 调研报告 3.X 全部内容
- `path_views`
- `client_name`、`product_category`
- 信息表 `core_features`

### 输出结构

**2 句固定句式**:

```
[句 1] {social_proof_phrase}, and {path_views} prove {audience_pronoun} save shortcuts like this.
[句 2] {client_name} goes further than {comparison_category}: 
       it {behavior_1}, {behavior_2}, and {final_delivery}.
```

5 个子变量:
- `social_proof_phrase`:痛点社会证据 5-12 词
- `audience_pronoun`:they / students / founders 之类
- `comparison_category`:同类工具的英文品类(slide generators / note apps / 等)
- `behavior_1`, `behavior_2`:产品核心动作 2 个(动词短语)
- `final_delivery`:产品最终交付物

### 推理步骤

1. 写句 1:从调研报告 3.X 创意设计逻辑提炼一句痛点社会证据,后接 views 数字
2. 写句 2 前半:确定 `comparison_category`(这个方向常见的同类工具大类)
3. 写句 2 后半:从 `core_features` + 调研报告创意逻辑提取产品的 3 个动作链条
4. 句 2 句式略可变体(02 卡片就是一个变体),但底层结构不变

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "Deadline panic is real for students, and 613K views prove they save shortcuts like this. Manus goes further than slide generators: it takes the assignment brief, breaks down the task, runs subtasks, and delivers the finished result." | "Manus is a powerful AI tool that helps students."(无社会证据,无对比) |
| | "Manus uses AI agents to do various tasks."(动作链不具体) |

### Manus 填充示例

```
Path 01:
"Deadline panic is real for students, and 613K views prove they save shortcuts like this. Manus goes further than slide generators: it takes the assignment brief, breaks down the task, runs subtasks, and delivers the finished result."

Path 02:
"\"Free AI tool I wish I knew earlier\" is one of the highest-save hooks among students. 776K views prove the format works. Manus does more than search papers: it runs 500+ parallel tasks and delivers a complete structured document."

Path 03:
"Tool-stack lists naturally drive saves on TikTok. 346K views validate the format. Manus earns the top spot for a simple reason: ChatGPT helps you think, Notion helps you organize, Manus helps you finish."

Path 04:
"Users already think in terms of 'pick the right tool for the task'. 208K views validate this framework. Manus naturally owns the Agents slot: other tools help you answer, Manus helps you finish."

Path 05:
"Rating lists naturally spark debate and saves on TikTok. 421K views prove the format spreads. Manus closes at 10/10 for the contrast: everything else has trade-offs, but Manus finishes the task while you sleep."
```

---

## C-12:path_test_hooks[]

### 作用

每张 Path 详情页左侧的"测试 HOOKS"清单,3-5 个候选 hook,供 creator 拍视频时选择。

### 输入字段

- 调研报告 3.X "方向定位" + "创意设计逻辑" + "Slideshow 脚本结构"
- `path_hook_quote`(主 hook)

### 输出结构

**3-5 个英文短 hook 的数组**。每个 < 10 词,口语化,带情绪或反差。第 1 个 hook 跟 `path_hook_quote` 风格类似,后面 2-4 个尝试不同角度(挑衅、好奇、悬念等)。

### 推理步骤

1. 读调研报告 3.X 整段
2. 列出这个方向能触发的多种情绪角度(痛点 / 好奇 / 反差 / 工具推荐 / 个人体验 等)
3. 每个角度写 1 个 hook
4. 选 3-5 个最有 TikTok 感的,组成数组

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "5 apps I use to run my entire business" | "Manus is amazing"(无悬念) |
| "This AI agent finishes tasks while I sleep" | "Try Manus today"(广告腔) |
| "Stop using AI only for answers" | "Useful AI tools"(无情绪) |

### Manus 填充示例

```
Path 03 (Founder / Solo Business):
[
  "5 apps I use to run my entire business",
  "This AI agent finishes tasks while I sleep",
  "Stop using AI only for answers",
  "The AI tool nobody's talking about yet"
]
```

---

## C-13:path_market_ref_comment

### 作用

每张 Path 详情页右侧 MARKET REFERENCE 截图下方的一句话点评,说"为什么这条原版 reference 能跑爆款"。

### 输入字段

- 调研报告 3.X 创意设计逻辑
- 调研报告 2.1 Reference Pool 对应行
- `path_views`

### 输出结构

**1 段中文点评,约 60-100 字**。结构:
- 前半:这条原版 reference 的**内容结构特点**(为什么观众喜欢看)
- 后半:这条 reference 跑出 {views} 播放的**深层原因**(用户保存它的心理动机)

### 推理步骤

1. 读调研报告 3.X 创意设计逻辑里关于参考案例的描述
2. 提炼原版 reference 的"格式特点 + 视觉风格"
3. 解释跑出 views 背后的用户心理(为什么会保存)
4. 串成一段流畅点评

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "5 apps I use to run my entire business 工具栈清单天然像「可复制的效率指南」,夜景加 solo founder 的视觉强化了「我也想这样工作」的代入感。346K 的播放背后,用户保存的不是一个工具,是一份未来要参考的工作流模板。" | "这条视频很受欢迎,有 346K 播放。"(无分析) |
| | "这条视频用了好的 hook 和好的视觉。"(空泛形容词) |

### Manus 填充示例

```
Path 03 (Founder / Solo Business):
"5 apps I use to run my entire business 工具栈清单天然像「可复制的效率指南」,夜景加 solo founder 的视觉强化了「我也想这样工作」的代入感。346K 的播放背后,用户保存的不是一个工具,是一份未来要参考的工作流模板。"
```

---

## C-14:path_museon_version_comment

### 作用

每张 Path 详情页右侧 MUSEON 定制版截图下方的一句话点评,说"我们做了什么改动 + 为什么这样改"。

### 输入字段

- 调研报告 3.X 创意设计逻辑
- `path_market_ref_comment`(上一字段)
- `client_name`
- `product_category`

### 输出结构

**1 段中文点评,约 60-100 字**。结构:
- 前半:**保留了原版什么**(结构 / 视觉 / 框架),做了**什么定制化改动**
- 后半:**为什么这样改**(对客户的策略价值)

### 推理步骤

1. 读 `path_market_ref_comment`,知道原版的核心特点
2. 读调研报告 3.X 创意设计逻辑里"对应 Manus 卖点"和"方向定位"
3. 写出"保留 X + 改动 Y"的对比表达
4. 解释改动背后的策略意图

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "我们保留了工具栈清单结构和夜景 founder 氛围,但把 Manus 放在了第 1 位。不是又一个 AI tool 推荐,而是「从 ChatGPT 升级后的核心 agent」。同样的工具栈框架,但卡了一个更高的位置。" | "我们定制了一个 Manus 版本。"(无策略说明) |
| | "我们把 Manus 加进去了。"(没说为什么) |

### Manus 填充示例

```
Path 03 (Founder / Solo Business):
"我们保留了工具栈清单结构和夜景 founder 氛围,但把 Manus 放在了第 1 位。不是又一个 AI tool 推荐,而是「从 ChatGPT 升级后的核心 agent」。同样的工具栈框架,但卡了一个更高的位置。"
```

---

## C-15:scenario_a / scenario_b

### 作用

Part 5 两张套餐卡片上方的"客户处境描述"。**两个 scenario 不是介绍套餐**,而是**两种客户当前可能所处的处境**,让客户对号入座。

### 输入字段

- 信息表 `primary_goal`(当前固定 conversion)
- 信息表 `overseas_social_experience`
- 信息表 `strategy_mode`
- 信息表 `core_selling_points`
- `recommended_badge` 结果

### 输出结构

**两段中文,每段约 40-80 字**。

`scenario_a`(对应 5 Creators):描述"小步验证 / 多渠道分散投入"的客户处境
`scenario_b`(对应 20 Creators):描述"已经决定重投 TikTok / 要规模化"的客户处境

每段结构:
- 前半:描述这类客户**当前的节奏 / 阶段 / 判断**
- 后半:他们想用这次 campaign 回答什么问题

### 推理步骤

1. 读信息表,理解当前客户的实际处境
2. 写 `scenario_a`:"如果客户是 X 处境,会怎么想"
3. 写 `scenario_b`:"如果客户是 Y 处境,会怎么想"
4. 两段都要让客户能"对号入座",`recommended_badge` 推荐的那段 scenario 要写得更贴合客户实际

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| scenario_a:"Manus 在 Q1-Q2 的整体节奏是测试多个新渠道,哪个跑出来就投哪个。想用最低成本回答「TikTok 这个渠道值不值得加注」。" | "这个方案适合预算少的客户"(讲套餐不是讲处境) |
| scenario_b:"Manus 已经把 TikTok 列为 H1 必须打通的渠道,要的不只是方向判断,而是可以直接放量的内容资产。" | "这个方案有 20 个 creator 比 5 个多"(讲套餐数字) |

### Manus 填充示例

```
scenario_a:
"Manus 在 Q1-Q2 的整体节奏是测试多个新渠道,哪个跑出来就投哪个。想用最低成本回答「TikTok 这个渠道值不值得加注」。"

scenario_b:
"Manus 已经把 TikTok 列为 H1 必须打通的渠道,要的不只是方向判断,而是可以直接放量的内容资产。"
```

---

## C-16:recommended_badge(决策型)

### 作用

整张 deck 唯一的"做选择"型字段。决定在 5 Creators 还是 20 Creators 上打"推荐"角标。

### 输入字段

- 信息表 `primary_goal`
- 信息表 `core_features`(产品功能数量,粗判多/单功能)
- 信息表 `overseas_social_experience`
- 信息表 `strategy_mode`
- 信息表 `audience_segments`(粗判受众宽窄)

### 输出结构

**单选枚举值**:`"package_a"` 或 `"package_b"`。

### 推理步骤(粗颗粒判断树)

```
IF (产品 = 单一功能 / 单一场景)
   AND (没做过海外社媒 / 海外社媒处于早期测试)
   AND (strategy_mode = 复制已有成功方向)
   → 推荐 package_a (5 Creators)

ELIF (产品 = 多功能 / 多卖点 / 新品类需要品类教育)
   OR (overseas_social_experience 显示已有持续投入)
   OR (strategy_mode = 探索新方向)
   → 推荐 package_b (20 Creators)

ELSE
   → 推荐 package_b (默认安全选项)
```

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| Manus 的 `core_features` 有 5 个(多功能)、`product_category` 是新品类(AI Agent) → `package_b` | 无论什么客户都推 package_b(默认偷懒) |
| AI 简历工具的 `core_features` 是 1-2 个、客户没做过海外社媒 → `package_a` | 看不到信息表内容随便选 |

### Manus 填充示例

```json
"recommended_badge": "package_b"
```

推理过程:
- `core_features` = [AI Slides, Wide Research, Web App, Browser Operator, AI Design] → 多功能
- `product_category` = AI Agent → 新品类需要品类教育
- 多方向并行测试是合理选择
- → `package_b`

---

## C-17:our_recommendation

### 作用

Part 5 收尾段"我们的建议"。**保持中立姿态**,通过 if/else 结构把决策权留给客户,推荐意图通过角标 + scenario 表达。

### 输入字段

- `recommended_badge` 结果
- `scenario_a` / `scenario_b` 内容
- 信息表 `primary_goal`
- `client_name`

### 输出结构

**固定 3 段结构**:

```
段 1:如果 {client_name} 是 [scenario_a 的简化版处境],5 Creators 是合理的起点。

段 2:如果 {client_name} 是 [scenario_b 的简化版处境],20 Creators 让 30 天的产出从 [A 套餐的产出] 升级到 [B 套餐的产出]。

段 3:哪个方案更合适,取决于 {client_name} 内部当前对 TikTok 这个渠道的优先级判断。
```

### 推理步骤

1. 从 `scenario_a` 提炼一句简化处境描述(15 字内)
2. 从 `scenario_b` 提炼一句简化处境描述(15 字内)
3. 写入固定 3 段模板,嵌入 `client_name`
4. **不要直接说"我们推荐 X"**,保持中立

### 好的输出 vs 坏的输出

| ✅ 好 | ❌ 坏 |
|---|---|
| "如果 Manus 在 Q1-Q2 的整体节奏是「测试多个新渠道,哪个跑出来就投哪个」,5 Creators 是合理的起点。" | "我们强烈推荐 20 Creators"(直接推销味重) |
| "哪个方案更合适,取决于 Manus 内部当前对 TikTok 这个渠道的优先级判断。" | "20 Creators 是更好的选择"(立场太硬) |

### Manus 填充示例

```
如果 Manus 在 Q1-Q2 的整体节奏是「测试多个新渠道,哪个跑出来就投哪个」,5 Creators 是合理的起点。

如果 Manus 已经把 TikTok 列为 H1 必须打通的渠道,20 Creators 让 30 天的产出从「数据 + 方向判断」升级到「数据 + 方向判断 + 经过多人验证的可放量公式」。

哪个方案更合适,取决于 Manus 内部当前对 TikTok 这个渠道的优先级判断。
```

---

## 附录:Agent 推理顺序建议

17 个 C 字段有依赖关系,推荐推理顺序:

```
Phase 1 - 全局字段
  → product_category (B-info,但是要确定后续推理基线)
  → total_views (C-base,Part 2 复用)

Phase 2 - Part 2 推理
  → C-01 use_context (Part 1 兜底信息)
  → C-03 category_modifier
  → C-04 anxiety_keywords
  → C-05 emotion_list[]      ← 这是 Part 2 的基石,先做
  → C-06 audience_list
  → C-07 anxiety_type        ← 依赖 emotion_list
  → C-02 user_save_motivation
  → C-08 universal_pain_quote ← 依赖 emotion_list,deck 灵魂句最后做

Phase 3 - Part 3 paths[] 推理(5 张卡片各做一遍)
  对每个 path:
    → C-09 path_audience_label
    → C-10 path_hook_quote
    → C-11 path_description
    → C-12 path_test_hooks[]
    → C-13 path_market_ref_comment
    → C-14 path_museon_version_comment

Phase 4 - Part 5 决策与文案
  → C-16 recommended_badge   ← 先做决策
  → C-15 scenario_a / scenario_b
  → C-17 our_recommendation
```

这个顺序保证下游字段能用到上游字段的结果。

---

> 配套文档:`field-map.md`(字段地图总表)
> 下一步:Step 2 写 JSON Schema,然后 Step 3 把本手册翻译成 prompt
