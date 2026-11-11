---
title: 应用中心产品手册
split_at: 2
sub_max_level: 2
version: 1.0.0
keywords: raksmart，应用中心，openclaw，ai 智能体，gateway token，模型配置，openai，anthropic，gemini。
description: OpenClaw 是可本地优先运行的 AI 智能体应用，本文介绍在 RakSmart 应用中心部署后的访问方式、模型配置、关键目录与常用操作。
---
# OpenClaw 使用指南

## 访问应用

**Web 控制台**

访问 `http://[您的服务器IP]:[gateway_port]`。端口默认为 `18789`，若有自定义配置，请以产品详情页中的 `gateway_port` 参数为准。

**Gateway 令牌登录**

首次访问时需要输入 Gateway 令牌。通过 SSH 连接至服务器后，执行以下命令查看凭据中的 `Gateway Token`（以实际部署为准）：

```bash
cat /opt/cloud/openclaw/credentials.txt
```

凭据文件内容示例：

```text
Gateway Port:    18789
Default Model:   anthropic/claude-sonnet-4-6
Gateway Token:   <您的 Gateway Token>
```

将 `Gateway Token` 填入登录页面即可登录。

## 模型配置

> **说明**
>
> 模型配置为可选项。部署时预填可让应用开箱即用；若部署时留空，安装完成后也可通过管理控制台或 CLI 随时补充。

### 方式一：部署时预配置

在应用部署参数页面的高级参数（默认折叠）中填写以下字段，仅填写需要的项，留空则不启用。

**原生供应商 API Key**

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| `openai_api_key` | OpenAI API Key | `sk-...` |
| `anthropic_api_key` | Anthropic API Key | `sk-ant-...` |
| `google_api_key` | Google Gemini API Key | `AIza...` |

**OpenAI 兼容接口**（如阿里云百炼、DeepSeek、Moonshot 等，以下三项需同时填写）

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| `compat_base_url` | 兼容接口的 Base URL | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| `compat_api_key` | 对应服务的 API Key | `sk-xxxxx` |
| `compat_provider_name` | 自定义 provider 名称（即后续模型的前缀） | `bailian` |

**默认模型**

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| `default_model` | 格式为 `<provider>/<model-id>` | `openai/gpt-4o`、`bailian/qwen3-max` |

### 方式二：部署后通过 CLI 配置（进阶）

具体步骤参见本章“模型配置指引”。

### 方式三：部署后通过管理控制台配置

访问 Web 控制台（`http://[您的服务器IP]:[gateway_port]`），登录后进入 **AI Model Configurations and Providers** 配置页面，添加所需的 provider 及 API Key。

> **提示**
>
> OpenAI、Anthropic、Google Gemini 等主流 provider 无需额外配置，只需填入对应 API Key 即可直接使用。对于阿里云百炼、DeepSeek、Moonshot 等 OpenAI 兼容接口，需同时填写 Base URL、API Key 和 Provider 名称。详见 [Model Providers 文档](https://docs.openclaw.ai/concepts/model-providers)。

## 关键目录说明

| 目录 | 说明 |
| --- | --- |
| `/opt/cloud/openclaw/data` | **Config 数据目录**（即 `.openclaw` 所在目录）。OpenClaw 的所有核心配置均保存于此，包括 `openclaw.json`（模型、渠道、工具等配置）、cron 任务定义、Agent 配置等。 |
| `/opt/cloud/openclaw/workspace` | **Workspace 数据目录**。存放 Agent 的工作区文件，包括 Skills（技能包）、长期记忆（Memory）、会话记录及 Heartbeat 检查清单（`HEARTBEAT.md`）等运行时数据。 |

> **说明**
>
> OpenClaw 采用本地优先（local-first）架构，所有对话记录、配置和技能均以 Markdown / YAML 文件形式存储于本地，可直接用文本编辑器查看或用 Git 备份。

## 常用操作

进入 `/opt/cloud/openclaw` 目录，或直接执行以下预设管理脚本：

| 操作 | 命令 |
| --- | --- |
| 启动服务 | `/opt/cloud/openclaw/start.sh` |
| 停止服务 | `/opt/cloud/openclaw/stop.sh` |
| 重启服务 | `/opt/cloud/openclaw/restart.sh` |
| 查看日志 | `/opt/cloud/openclaw/logs.sh` 或 `docker logs openclaw-gateway` |
| 更新至最新版并重启 | `/opt/cloud/openclaw/update.sh` |
| 执行 OpenClaw 配置命令 | `/opt/cloud/openclaw/openclaw_cmd.sh` |

> **提示**
>
> 更新后 Gateway 会自动重启并加载新版本。若更新后出现异常，可参考“深入学习”中的官方文档进行故障排查。

## 深入学习

| 资源 | 链接 |
| --- | --- |
| 官方网站 | [openclaw.ai](https://openclaw.ai/) |
| 官方文档 | [docs.openclaw.ai](https://docs.openclaw.ai/) |
| GitHub 仓库 | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) |
| ClawHub（技能市场） | 可通过 `npm i -g clawhub` 安装命令行工具，搜索、安装和更新 Skills |
| 社区 Discord | 可通过官方网站或 GitHub 首页找到加入链接 |

## 模型配置指引

### 前置说明

由于本系统采用 Docker 方式部署，原生的 OpenClaw CLI 命令需要进入容器内部才能执行。为了方便操作，我们**推荐使用系统提供的命令包装脚本** `/opt/cloud/openclaw/openclaw_cmd.sh`，该脚本支持在主机上直接调用 OpenClaw CLI，无需手动进入 Docker 容器。

可通过以下两种方式配置参数，效果等价，可按习惯选择：

- **引导向导**：运行 `/opt/cloud/openclaw/openclaw_cmd.sh onboard`，跟随交互提示完成配置（适合初次配置）。
- **命令行（推荐）**：使用 `/opt/cloud/openclaw/openclaw_cmd.sh config set` 命令逐项直接修改。

配置完成后，可运行以下命令验证当前模型状态：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh models list    # 查看所有已配置的模型
/opt/cloud/openclaw/openclaw_cmd.sh models status  # 查看主模型、备用模型及各 Provider 认证状态
```

### 场景一：配置 OpenAI API Key

1. 设置 API Key。

   交互式引导配置：

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh onboard --openai-api-key "sk-xxxxxxxxxxxxxxxx"
   ```

   或通过环境变量方式配置（推荐用于服务器环境）：

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh config set env.OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxx"
   ```

2. 设置主模型。

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh config set agents.defaults.model.primary "openai/gpt-4o"
   ```

常用 OpenAI 模型 ID 示例：

| 模型 | 引用格式 |
| --- | --- |
| GPT-4o | `openai/gpt-4o` |
| GPT-4o mini | `openai/gpt-4o-mini` |
| GPT-4.1 | `openai/gpt-4.1` |

> **说明**
>
> 模型 ID 随 OpenAI 版本迭代可能变更，请以 [OpenAI 官方文档](https://platform.openai.com/docs/models) 为准。

### 场景二：配置 Anthropic API Key

1. 设置 API Key。

   交互式引导配置：

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh onboard --anthropic-api-key "sk-ant-xxxxxxxxxxxxxxxx"
   ```

   或通过环境变量方式配置：

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh config set env.ANTHROPIC_API_KEY "sk-ant-xxxxxxxxxxxxxxxx"
   ```

2. 设置主模型。

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh config set agents.defaults.model.primary "anthropic/claude-sonnet-4-6"
   ```

常用 Anthropic 模型 ID 示例：

| 模型 | 引用格式 |
| --- | --- |
| Claude Sonnet 4.6 | `anthropic/claude-sonnet-4-6` |
| Claude Opus 4.6 | `anthropic/claude-opus-4-6` |

> **提示**
>
> Anthropic API Key 认证是官方推荐的认证方式，稳定性优于 setup-token 方式。API Key 可在 [Anthropic Console](https://console.anthropic.com/settings/keys) 创建。

### 场景三：配置 Google Gemini API Key

1. 设置 API Key。

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh config set env.GOOGLE_API_KEY "AIzaxxxxxxxxxxxxxxxx"
   ```

2. 设置主模型。

   ```bash
   /opt/cloud/openclaw/openclaw_cmd.sh config set agents.defaults.model.primary "google/gemini-2.5-pro"
   ```

常用 Gemini 模型 ID 示例：

| 模型 | 引用格式 |
| --- | --- |
| Gemini 2.5 Pro | `google/gemini-2.5-pro` |
| Gemini 2.5 Flash | `google/gemini-2.5-flash` |

> **说明**
>
> Google API Key 可在 [Google AI Studio](https://aistudio.google.com/app/apikey) 创建。

### 场景四：接入自定义 OpenAI 兼容模型

适用于阿里云百炼（DashScope）、Moonshot、DeepSeek 等提供 OpenAI 兼容接口的模型服务。

命令格式：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh config set models.providers.<provider_name> \
  '{"baseUrl":"<接口地址>","apiKey":"<你的APIKey>","api":"openai-completions","models":[{"id":"<model_id>","name":"<显示名称>"}]}' \
  --strict-json
```

示例：接入阿里云百炼（DashScope）

```bash
/opt/cloud/openclaw/openclaw_cmd.sh config set models.providers.bailian \
  '{"baseUrl":"https://dashscope.aliyuncs.com/compatible-mode/v1","apiKey":"sk-xxxxxxxxxxxxxxxx","api":"openai-completions","models":[{"id":"kimi-k2.5","name":"kimi-k2.5"}]}' \
  --strict-json
```

配置后，设置该 Provider 下的模型为主模型：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh config set agents.defaults.model.primary "bailian/kimi-k2.5"
```

字段说明：

| 字段 | 说明 |
| --- | --- |
| `<provider_name>` | 自定义标识符，字母数字下划线，如 `bailian`、`deepseek` |
| `baseUrl` | 服务商提供的兼容接口地址 |
| `apiKey` | 对应服务商的 API Key |
| `api` | 固定填写 `openai-completions` |
| `models[].id` | 模型 ID，与服务商文档一致 |
| `models[].name` | 展示名称，可自定义 |

### 场景五：设置主模型与备用模型

当主模型因限流、故障或超时无法响应时，OpenClaw 会自动按顺序尝试备用模型，无需人工干预。

设置主模型：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh config set agents.defaults.model.primary "anthropic/claude-sonnet-4-6"
```

添加备用模型：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh models fallbacks add "anthropic/claude-opus-4-6"
/opt/cloud/openclaw/openclaw_cmd.sh models fallbacks add "openai/gpt-4o"
/opt/cloud/openclaw/openclaw_cmd.sh models fallbacks add "google/gemini-2.5-flash"
```

查看当前备用模型列表：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh models fallbacks list
```

移除某个备用模型：

```bash
/opt/cloud/openclaw/openclaw_cmd.sh models fallbacks remove "openai/gpt-4o"
```

配置效果等同于以下 JSON 结构：

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-sonnet-4-6",
        "fallbacks": [
          "anthropic/claude-opus-4-6",
          "openai/gpt-4o",
          "google/gemini-2.5-flash"
        ]
      }
    }
  }
}
```

> **说明**
>
> 跨 Provider 的 Fallback 需要对应 Provider 都已完成 API Key 配置，否则该备用模型会被跳过。

### 常用排查命令

```bash
/opt/cloud/openclaw/openclaw_cmd.sh models status     # 查看主模型、备用模型及认证状态总览
/opt/cloud/openclaw/openclaw_cmd.sh models list       # 列出所有可用模型
/opt/cloud/openclaw/openclaw_cmd.sh doctor            # 检查整体配置健康状态（含 Provider 认证）
```

如遇模型 ID 无效报错，通常是模型版本已更新，请查阅对应服务商的最新模型列表后更新配置。
