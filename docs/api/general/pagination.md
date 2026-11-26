---
title: 分页
---

所有列表接口均采用 `offset` + `limit` 的方式分页。

## 请求参数

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `offset` | integer | `0` | 跳过的记录数，必须为非负整数 |
| `limit` | integer | `10` | 每页返回的记录数，必须为正整数，最大 `100` |

`limit` 超过 `100` 时按 `100` 处理。

## 响应字段

| 字段 | 说明 |
| --- | --- |
| `count` | 符合条件的记录总数 |
| `offset` | 本次请求实际使用的 `offset` |
| `limit` | 本次请求实际使用的 `limit` |
| 列表字段 | 当前页的记录，字段名因接口而异，例如 `services`、`regions` |

```json
{
  "count": 35,
  "offset": 20,
  "limit": 10,
  "services": [ ... ]
}
```

## 获取全部数据

依次增加 `offset`，直到 `offset` 大于或等于 `count`：

::: code-group

```python [Python]
import os
import requests

BASE = "https://rak-api.raksmart.com/rakapi/v2"
HEADERS = {"X-API-Key": os.environ["RAKSMART_API_KEY"]}

def list_all_vps():
    items, offset, limit = [], 0, 100
    while True:
        resp = requests.get(f"{BASE}/vps", headers=HEADERS,
                            params={"offset": offset, "limit": limit}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        items.extend(data["services"])
        offset += limit
        if offset >= data["count"]:
            return items
```

```bash [curl]
curl -s "https://rak-api.raksmart.com/rakapi/v2/vps?offset=0&limit=100" \
  -H "X-API-Key: $RAKSMART_API_KEY"
curl -s "https://rak-api.raksmart.com/rakapi/v2/vps?offset=100&limit=100" \
  -H "X-API-Key: $RAKSMART_API_KEY"
```

:::

::: tip 提示
批量获取数据时，建议使用 `limit=100` 以减少请求次数，并注意 [请求频率限制](./rate-limits.md)。
:::
