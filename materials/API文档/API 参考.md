# API 参考

完整的接口说明，包括参数、请求示例和响应示例，请参见在线 API 参考：

**<https://rak-api.raksmart.com/>**

## 接口索引

### 账户

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/user` | 查询账户信息 |

### 服务

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/services` | 查询服务列表 |
| `GET` | `/services/{id}` | 查询服务详情 |

### VPS

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/vps` | 查询 VPS 列表 |
| `GET` | `/vps/regions` | 查询 VPS 可用区域 |
| `GET` | `/vps/{id}` | 查询 VPS 详情 |
| `POST` | `/vps/{id}/start` | 开机 |
| `POST` | `/vps/{id}/stop` | 关机 |
| `POST` | `/vps/{id}/restart` | 重启 |
| `POST` | `/vps/{id}/hard_stop` | 强制关机 |
| `POST` | `/vps/{id}/hard_restart` | 强制重启 |

### 裸机云

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/bare-metals` | 查询裸机云列表 |
| `GET` | `/bare-metals/regions` | 查询裸机云可用区域 |
| `GET` | `/bare-metals/{id}` | 查询裸机云详情 |
| `POST` | `/bare-metals/{id}/start` | 开机 |
| `POST` | `/bare-metals/{id}/stop` | 关机 |
| `POST` | `/bare-metals/{id}/restart` | 重启 |
| `POST` | `/bare-metals/{id}/hard_stop` | 强制关机 |
| `POST` | `/bare-metals/{id}/hard_restart` | 强制重启 |

### 独立服务器

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/dedicated-servers` | 查询独立服务器列表 |
| `GET` | `/dedicated-servers/regions` | 查询独立服务器可用区域 |
| `GET` | `/dedicated-servers/{id}` | 查询独立服务器详情 |
| `POST` | `/dedicated-servers/{id}/start` | 开机 |
| `POST` | `/dedicated-servers/{id}/stop` | 关机 |
| `POST` | `/dedicated-servers/{id}/restart` | 重启 |

### 独立云盘

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/volumes` | 查询云盘列表 |
| `GET` | `/volumes/regions` | 查询云盘可用区域 |
| `GET` | `/volumes/{id}` | 查询云盘详情 |
| `POST` | `/volumes/{id}/attach` | 挂载到 VPS，请求体：`{"instance_id": <VPS 服务 ID>}` |
| `POST` | `/volumes/{id}/detach` | 卸载 |

### 弹性 IP

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/elastic-ips` | 查询弹性 IP 列表 |
| `GET` | `/elastic-ips/regions` | 查询弹性 IP 可用区域 |
| `GET` | `/elastic-ips/{id}` | 查询弹性 IP 详情 |
| `POST` | `/elastic-ips/{id}/attach` | 绑定到 VPS，请求体：`{"instance_id": <VPS 服务 ID>}` |
| `POST` | `/elastic-ips/{id}/detach` | 解绑 |

### 快照

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/snapshots` | 查询快照列表，可按 `region`、`serviceid`（实例或云盘的服务 ID）、`volume_uuid` 筛选 |
| `GET` | `/snapshots/{id}` | 查询快照详情，`id` 为快照 UUID |
| `POST` | `/snapshots/{id}/restore` | 恢复快照 |

::: danger 风险提示
恢复快照会将磁盘数据回滚到快照创建时的状态，快照之后写入的数据将丢失。请在操作前确认。
:::
