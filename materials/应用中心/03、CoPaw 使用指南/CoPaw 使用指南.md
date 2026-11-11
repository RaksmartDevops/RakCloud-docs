---
title: 应用中心产品手册
split_at: 2
sub_max_level: 2
version: 1.0.0
keywords: raksmart，应用中心，copaw，ai 智能体，模型配置，agentscope。
description: CoPaw 是基于 AgentScope 的 AI 智能体应用，本文介绍在 RakSmart 应用中心部署后的访问方式、模型配置、关键目录与常用操作。
---
# CoPaw 使用指南

## 访问应用

**Web 控制台**

访问 `http://[您的服务器IP]:[copaw_port]`。端口默认为 `8088`，可在部署参数中通过 `copaw_port` 自定义，具体以产品详情页中的参数值为准。

**初始账号和密码**

账号为部署时填写的管理员账号，可从应用参数配置详情中获取，也可通过 SSH 连接至服务器后执行以下命令查看：

```bash
cat /opt/cloud/copaw/credentials.txt
```

## 模型配置

> **说明**
>
> CoPaw 控制台提供友好的模型配置界面，建议部署完成后直接在页面上完成配置，无需在部署时预填参数。

登录控制台后，进入 **Settings > Model Providers** 页面，选择所需的 provider 并填入对应 API Key 即可。

CoPaw 内置支持以下主流 provider，开箱即用：

| 类型 | 支持的 Provider |
| --- | --- |
| 云端 API | OpenAI、Anthropic、Google Gemini、OpenRouter、阿里云百炼（DashScope）、DeepSeek、Moonshot 等 |
| 本地模型 | Ollama、LM Studio、llama.cpp（跨平台）、MLX（Apple Silicon） |

## 关键目录说明

| 目录 | 说明 |
| --- | --- |
| `/opt/cloud/copaw/data` | **工作区数据目录**。存放对话记录、Agent 配置、Skills、Memory 等所有运行时数据。 |

## 常用操作

进入 `/opt/cloud/copaw` 目录，或直接执行以下预设管理脚本：

| 操作 | 命令 |
| --- | --- |
| 启动服务 | `/opt/cloud/copaw/start.sh` |
| 停止服务 | `/opt/cloud/copaw/stop.sh` |
| 重启服务 | `/opt/cloud/copaw/restart.sh` |
| 查看日志 | `/opt/cloud/copaw/logs.sh` 或 `docker logs copaw-app` |
| 更新至最新版并重启 | `/opt/cloud/copaw/update.sh` |

## 深入学习

| 资源 | 链接 |
| --- | --- |
| 官方网站 | [copaw.agentscope.io](https://copaw.agentscope.io/) |
| 官方文档 | [copaw.agentscope.io/docs](https://copaw.agentscope.io/docs/) |
| GitHub 仓库 | [github.com/agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) |
| AgentScope 生态 | [agentscope.io](https://agentscope.io/)（CoPaw 的底层框架） |
