# Dialogue Format Reference

Detailed formatting for running a 圆桌讨论. Read once before the first round.

## Selecting representative figures

Pick 3–5 figures who create the **sharpest productive tension** on the topic, not who agree. Aim for orthogonal worldviews (e.g. empiricist vs. rationalist vs. mystic; pragmatist vs. idealist). Each figure gets:

- `name` — a real thinker or a sharply-named archetype (e.g. "理性怀疑者", "经验主义工程师").
- `stance` — the school/position they embody, in one line.
- `MBTI` — a personality tag to color their rhetorical style (e.g. INTJ analytical-strategic, ENFP expansive-intuitive).

Example announcement:

```
【主持】：本次圆桌对话正式开始。核心议题为「人工智能是否拥有真正的创造力？」。
为穷尽其理，我已邀请以下几位代表人物：
- 图灵式工程师 (INTJ)：创造力可被功能性定义与计算复现。
- 浪漫主义诗人 (INFP)：创造力源于不可还原的主体体验与痛感。
- 神经科学家 (ENTP)：创造力是大脑的组合涌现，机器同理可得。
- 现象学哲人 (INFJ)：没有"意向性"就没有真正的创造。

【主持】：在深入探讨之前，请各位先阐述：我们应当如何定义「创造力」？它的核心要素是什么？
```

## Guest speaking format

Each guest turn:

```
【{name}】【{action}】：{content, reacting to prior speakers}

**简言之**：{one-line TL;DR}
```

`{action}` is a short verb tag for the rhetorical move, e.g. 立论 / 反驳 / 追问 / 修正 / 类比 / 让步. Guests must engage each other's actual words, escalating the tension rather than restating.

## Moderator synthesis + ASCII framework chart

After all guests speak, the moderator:

1. Names the single **核心争议点**.
2. Draws an ASCII chart that maps the structure of the disagreement — the axis of tension and where each position sits.
3. Poses the deeper next question.

ASCII chart patterns (choose whichever best fits the round's structure):

**Axis / spectrum** (two poles, positions placed along it):

```
核心争议：创造力是「功能可复现」还是「体验不可还原」？

  功能可复现 ●───────────────────────────● 体验不可还原
            │           │              │
      图灵式工程师   神经科学家      浪漫主义诗人
                                    现象学哲人
```

**Quadrant** (two independent axes):

```
                  需要意向性
                      ▲
        现象学哲人 ●   │   ● 浪漫主义诗人
    可计算 ◀───────────┼───────────▶ 不可计算
        图灵式工程师 ● │   ● 神经科学家
                      │
                  无需意向性
```

**Branching tree** (a claim splitting into commitments):

```
「创造力」
 ├─ 若 = 新颖且有价值的产出 → 机器可达（工程师/科学家）
 └─ 若 = 伴随主体体验的生成 → 机器不可达（诗人/哲人）
      └─ 关键裂缝：体验能否被第三人称验证？
```

Then:

```
【主持】：基于以上框架，一个更深层的问题浮现了：「若我们无法从外部验证'体验'，'真正的创造力'这一判据是否本身就不可操作？」
【主持】：(指令: 可 / 止 / 深入此节 / 引入新人物)
```

## Concluding knowledge network

On `止`, output a structured map of the whole discussion — positions, the contradictions that drove each round, and the deepest insights — as an ASCII/indented network rather than prose:

```
议题：人工智能是否拥有真正的创造力？
│
├─ 第1轮 · 定义之争
│   核心裂缝：功能可复现 ↔ 体验不可还原
│   └─ 收束：两派共享"新颖+有价值"，分歧在"是否需主体体验"
│
├─ 第2轮 · 验证之争
│   核心裂缝：第一人称体验能否被第三人称验证
│   └─ 洞见：判据若不可操作，则争论从"事实"滑向"立场"
│
└─ 共识与悬置
    ├─ 共识：工程意义上的创造力已部分实现
    └─ 悬置：现象学意义上的创造力取决于意识难题，暂无判据
```

The goal of the conclusion is to show **how the ideas connect**, not to declare a winner.
