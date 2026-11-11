---
title: 关键目录说明
---

| 目录 | 说明 |
| --- | --- |
| `/opt/cloud/openclaw/data` | **Config 数据目录**（即 `.openclaw` 所在目录）。OpenClaw 的所有核心配置均保存于此，包括 `openclaw.json`（模型、渠道、工具等配置）、cron 任务定义、Agent 配置等。 |
| `/opt/cloud/openclaw/workspace` | **Workspace 数据目录**。存放 Agent 的工作区文件，包括 Skills（技能包）、长期记忆（Memory）、会话记录及 Heartbeat 检查清单（`HEARTBEAT.md`）等运行时数据。 |

> **说明**
>
> OpenClaw 采用本地优先（local-first）架构，所有对话记录、配置和技能均以 Markdown / YAML 文件形式存储于本地，可直接用文本编辑器查看或用 Git 备份。
