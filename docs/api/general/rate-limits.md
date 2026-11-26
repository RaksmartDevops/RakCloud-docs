---
title: 请求频率限制
---

为保障服务的稳定性，API 对请求频率进行限制。

## 限制规则

API 按请求来源 IP 统计请求频率。超过限制的请求将被拒绝，并返回 HTTP 状态码 `429`。

::: tip 提示
`429` 响应的响应体可能不是 JSON 格式。请以 HTTP 状态码 `429` 作为判断依据。
:::

## 处理建议

- **控制并发**：避免同一时刻发出大量请求。批量操作时，建议依次执行，或限制并发数量。
- **合理分页**：使用 `limit=100` 减少获取列表所需的请求次数。
- **合理轮询**：查询异步操作结果时，轮询间隔建议不低于 5 秒。
- **缓存结果**：区域列表等不常变化的数据，可以在本地缓存。

## 收到 429 后重试

收到 `429` 后，请等待一段时间再重试，并逐次增加等待时间（指数退避）：

```python
import time
import requests

def get_with_retry(url, headers, max_retries=5):
    delay = 1
    for _ in range(max_retries):
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code != 429:
            return resp
        time.sleep(delay)
        delay = min(delay * 2, 30)
    return resp
```
