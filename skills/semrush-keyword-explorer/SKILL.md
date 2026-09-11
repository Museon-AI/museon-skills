---
name: semrush-keyword-explorer
description: "Guide for performing keyword research and domain analysis using SEMrush via the dash.3ue.com proxy platform. Use for: finding high-value keywords, analyzing competitor domains, discovering content gaps, and generating SEO content strategies."
---

# SEMrush Keyword Explorer

This skill provides a standardized workflow for conducting SEO keyword research and domain analysis using SEMrush through the `dash.3ue.com` proxy platform.

## 1. Accessing SEMrush

1. Navigate to the proxy login page: `https://dash.3ue.com/zh-Hans/#/login`
2. Log in using the following credentials:
   - **账号 (Username)**: 样米
   - **密码 (Password)**: 2026.04.17
3. In the dashboard, locate the "SEMrush" tool card (you can use the filter input to search for "semrush").
4. Click the "打开" (Open) button on the SEMrush card to access the tool. This will open `https://sem.3ue.com/`.

## 2. Core Workflows

### Workflow A: Keyword Research (Finding Opportunities)

Use this workflow to discover new keyword opportunities, assess their difficulty, and identify search intent.

1. In the SEMrush sidebar, navigate to **SEO > 关键词研究 (Keyword Research) > 关键词魔法工具 (Keyword Magic Tool)**.
2. Enter a seed keyword related to your niche (e.g., "tiktok marketing", "ai creators").
3. **CRITICAL**: Wait for the keyword table to fully load. If the page shows "未找到任何数据" (No data found) because of a domain filter, click "清除域名筛选器" (Clear domain filter).
4. **CRITICAL**: Once the table is loaded, use the `browser_view` tool to capture the full HTML of the page. This saves the HTML to `/home/ubuntu/upload/`.
5. Repeat steps 2-4 for any additional seed keywords you want to research.
6. Use the bundled script to parse the saved HTML files into a structured CSV:
   ```bash
   python3 /home/ubuntu/skills/semrush-keyword-explorer/scripts/parse_semrush_html.py /path/to/output.csv "seed keyword 1" "seed keyword 2"
   ```
7. Analyze the generated CSV to select target keywords based on the criteria below.

### Workflow B: Domain Overview (Competitor Analysis)

Use this workflow to analyze a specific domain (e.g., a competitor or your own site) to understand its overall SEO health, traffic sources, and top-ranking keywords.

1. In the SEMrush sidebar, navigate to **SEO > 竞品分析 (Competitive Research) > 域名概览 (Domain Overview)**.
2. Enter the target domain (e.g., `competitor.com`) in the search bar and click Search.
3. Review the following key metrics:
   - **Authority Score**: Indicates the overall strength of the domain.
   - **自然流量 (Organic Search Traffic)**: Estimated monthly traffic from organic search.
   - **反向链接 (Backlinks)**: Total number of backlinks pointing to the domain.
4. Scroll down to the **自然搜索研究 (Organic Research)** section to identify the top keywords driving traffic to the domain.
5. Analyze the **主要的引用来源 (Main Referring Domains)** to understand their backlink profile.

### Workflow C: Content Gap Analysis

Use this workflow to find keywords that your competitors rank for, but you do not.

1. In the SEMrush sidebar, navigate to **SEO > 竞品分析 (Competitive Research) > 关键词差异 (Keyword Gap)**.
2. Enter your domain and up to 4 competitor domains.
3. Click "Compare".
4. Review the "Missing" and "Weak" tabs to identify keywords where competitors are outperforming you.
5. Prioritize keywords with high volume and manageable KD to create new content or optimize existing pages.

## 3. Keyword Selection Criteria

When selecting keywords for website exposure, prioritize those that meet the following criteria:

- **High Relevance**: The keyword must be directly related to the product or service offered.
- **Manageable Difficulty (KD)**: Use SEMrush's KD tiers to balance opportunity and effort:
  - **0-14 (Very Easy)** & **15-29 (Easy)**: Best for quick wins and new pages.
  - **30-49 (Possible)**: Good targets for well-structured, high-quality content.
  - **50-69 (Difficult)**: Requires strong content and some backlinks. Target these for core pillar pages.
  - **70+ (Hard/Very Hard)**: Avoid unless the domain has high authority (AS > 50) or you are willing to invest heavily in link building.
- **Sufficient Volume**: Look for keywords with a monthly search volume of at least 50-100.
- **Clear Intent**: Prioritize keywords with Informational or Commercial intent, as these are often easier to target with blog posts and landing pages.

## 4. Tracking Completed Keywords

To avoid duplicating effort, it is crucial to track which keywords have already been targeted.

1. Maintain a central tracking document (e.g., a spreadsheet or a dedicated Markdown file in the project repository, like `docs/seo/keyword-tracker.md`).
2. Before starting research on a new seed keyword, check the tracking document to ensure it hasn't been covered recently.
3. After completing research and selecting target keywords, update the tracking document with the chosen keywords, their metrics (Volume, KD), and the planned content type.
4. Regularly review the tracking document to identify gaps and plan future content.
