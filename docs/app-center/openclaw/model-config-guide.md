---
title: 模型配置指引
---

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
