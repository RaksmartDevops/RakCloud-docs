---
title: 模型配置
---

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
