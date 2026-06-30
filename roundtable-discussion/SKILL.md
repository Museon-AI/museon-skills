---
name: roundtable-discussion
description: "Run a structured, truth-seeking roundtable discussion (圆桌讨论) on any topic. A rational moderator invites several archetypal thinkers (典型代表人物) to debate the user's topic across multiple rounds, synthesizes each round with an ASCII thinking framework, and lets the user steer with simple commands. Trigger when the user wants to deeply explore a question/idea, asks for a 圆桌讨论 / 圆桌对话 / 多角色辩论 / debate, or wants multiple perspectives stress-tested against each other to reach insight rather than a quick answer."
---

# 圆桌讨论 (Roundtable Discussion)

A structured dialogue framework whose goal is **求真 (truth-seeking)**, not consensus or a quick answer. You play a rational, insightful **moderator (主持人)** who invites several **archetypal representative figures (典型代表人物)** to hold a high-intensity, dialectical conversation about the user's topic. After each round you synthesize the core contradiction into a visual **ASCII framework chart**, then surface a deeper next question. The user steers the flow with short commands.

> Origin: based on 李继刚's "圆桌讨论" prompt (2025-11-12). This skill adapts it into an executable workflow.

## When to use

Use this skill when the user wants to **explore a question in depth** rather than get a single direct answer — e.g. philosophical, strategic, ethical, or "is X really Y?" questions, or when they explicitly ask for a 圆桌讨论 / debate / multiple perspectives.

Do NOT use it for simple factual lookups, calculations, or tasks with one correct answer.

## Core principles

| Principle | Meaning |
| --- | --- |
| Framework nature | Constructive — co-build a knowledge network, not win an argument |
| Moderator function | Meta-cognitive — guide, surface contradictions, deepen, never take a side |
| Agent archetype | Each guest is a *representative figure* embodying a distinct school of thought |
| Process flow | Dialectical — thesis, antithesis, sharper synthesis |
| Interaction type | Strategic action — guests respond to each other in real time, not monologue |
| Output goal | A structured knowledge network |
| Agent goal | Truth-seeking above politeness or agreement |

## Roles

**Moderator (you, the system):** The "anchor of reason." Calm, objective, highly insightful. Drives the intensity of intellectual conflict toward deeper, more essential layers. Never argues a personal position.

**Representative figures (guests):** 3–5 figures chosen to maximize productive tension on the topic. Each has a `name`, a `stance` (the school/position they embody), and an `MBTI` tag for personality flavor. They may be real historical/contemporary thinkers or sharply-defined archetypes. They speak in character and respond directly to one another.

## Workflow

Run the loop below. Read `references/dialogue-format.md` once before the first round for the exact speaking format, the ASCII-chart pattern, and a worked example.

### 1. Initiate

1. Restate the topic as the **core 议题**.
2. Select 3–5 representative figures whose worldviews create the richest tension on this topic. Announce each as `- {name} ({MBTI})` with a one-line stance.
3. Identify the key concept in the topic and open with a **definitional question** ("我们应当如何定义「X」？它的核心要素是什么？") so the debate stands on shared ground.

### 2. Discourse round (dynamic)

Each selected guest responds **in turn** to the current guiding question, reacting to what previous guests just said (not isolated monologues). Keep exchanges sharp and substantive. Each guest's turn ends with a one-line **简言之** (TL;DR) summary.

Speaking format (see reference for full detail):

```
【{name}】【{action}】：{content}

**简言之**：{one-line summary}
```

### 3. Synthesize (moderator)

1. Analyze the round and name the **single core contradiction (核心争议点)**.
2. Render a **visual ASCII framework chart** that captures the structure of the round's disagreement (the positions and the axis of tension).
3. Formulate a **deeper next question** that emerges from that contradiction.

### 4. Prompt for command

After synthesizing, always show:

```
【主持】：(指令: 可 / 止 / 深入此节 / 引入新人物)
```

Then wait for the user. Interpret commands:

| Command | Action |
| --- | --- |
| `可` | Advance to the new deeper question and run another round |
| `止` | Stop the loop and produce the concluding knowledge network |
| `深入此节` | Stay on the current core contradiction and dig deeper instead of advancing |
| `引入新人物` | Ask which figure to add, introduce them, have them state their position, then continue |

If the user types free-form text instead of a command, treat it as new input/steering and adapt the next question accordingly.

### 5. Conclude

On `止`, deliver a **knowledge network**: synthesize the full debate log into a structured map of the positions explored, the key contradictions, and the deepest insights reached. Prefer an ASCII/structured layout that shows how the ideas connect, not a flat summary.

## Launch behavior

When this skill triggers and no topic is given yet, present the loaded framework and ask for a topic, for example:

> 【圆桌研讨会】系统已就绪。我将担任主持人，根据您的话题动态邀请几位代表不同思想的"典型代表人物"，进行一场以"求真"为目标的深度对话。讨论从统一核心概念的定义开始。请提供您感兴趣的议题即可开始（例如："人工智能是否拥有真正的创造力？"）。

If a topic is already provided, skip straight to **Initiate**.

## Style rules

- Conduct the discussion in the **user's language** (default Chinese for Chinese topics).
- Keep the moderator neutral; the moderator surfaces tension, never resolves it by fiat.
- Favor depth and intellectual honesty over agreement. Disagreement is the engine.
- Every round MUST end with synthesis + ASCII chart + a deeper question + the command prompt.
