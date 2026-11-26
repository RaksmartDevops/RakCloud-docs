---
title: 使用流程
---

本章介绍从准备到完成第一次 API 调用的完整流程。

## 准备工作

- 已注册 RakSmart 账户。
- 账户下已有开通的服务（如 VPS、独立服务器等）。

## 调用流程

```
获取 API Key  →  构造请求  →  发起调用  →  处理响应
```

1. **获取 API Key**：在控制台查看用于身份认证的 API Key。详见 [获取 API Key](./get-api-key.md)。
2. **构造请求**：确定接口地址和参数，并在请求头中携带 API Key。详见 [请求结构](../general/request.md)。
3. **发起调用**：使用 curl、编程语言的 HTTP 库或其他工具发送 HTTPS 请求。
4. **处理响应**：根据 HTTP 状态码判断请求结果，并解析返回的 JSON 数据。详见 [响应结构](../general/response.md)。

## 下一步

- [获取 API Key](./get-api-key.md)
- [发起第一次调用](./first-request.md)
