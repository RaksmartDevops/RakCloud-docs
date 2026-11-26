---
title: HTTP 状态码
---

## 状态码一览

| 状态码 | 含义 | 说明 | 处理建议 |
| --- | --- | --- | --- |
| `200` | OK | 查询成功 | 解析响应体 |
| `204` | No Content | 操作指令已下发 | 查询资源状态确认结果，详见 [异步操作](./async-operations.md) |
| `400` | Bad Request | 请求参数不合法 | 根据 `error_message` 检查参数，修正后重新请求 |
| `401` | Unauthorized | 认证失败 | 检查 API Key，详见 [认证方式](../authentication/api-key.md) |
| `404` | Not Found | 资源不存在，或不属于当前账户 | 确认资源 ID 正确且属于当前账户 |
| `409` | Conflict | 资源当前状态不允许此操作 | 查询资源状态，待状态满足后再操作 |
| `429` | Too Many Requests | 请求频率超过限制 | 降低请求频率并稍后重试，详见 [请求频率限制](./rate-limits.md) |
| `502` | Bad Gateway | 服务暂时不可用 | 稍后重试，详见 [错误处理与重试](./error-handling.md) |

## 常见错误示例

### 400 参数错误

| `error_message` 示例 | 原因 |
| --- | --- |
| `limit is invalid` | `limit` 不是正整数 |
| `offset is invalid` | `offset` 不是非负整数 |
| `search is invalid` | `search` 参数不符合要求 |
| `instance_id is invalid` | 请求体中缺少 `instance_id` 或取值不正确 |
| `duplicate X-API-Key header` | 请求中携带了多个 `X-API-Key` 请求头 |

### 404 资源不存在

访问不存在或不属于当前账户的资源，均返回 `404`。请确认：

- 资源 ID 是否正确；
- 资源是否属于当前 API Key 对应的账户；
- 接口路径与资源类型是否匹配，例如独立服务器的服务 ID 不能用于 `/vps/{id}`。

### 409 状态冲突

| `error_message` 示例 | 原因 |
| --- | --- |
| `service is suspended` | 服务已暂停，无法执行操作 |
| `ip is already attached` | 弹性 IP 已绑定到其他实例 |
| `ip is not attached` | 弹性 IP 未绑定，无法解绑 |
| `ip is not active` | 弹性 IP 服务未处于有效状态 |
