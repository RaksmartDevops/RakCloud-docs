---
title: 访问应用
---

**pgAdmin 管理界面**：`http://服务器IP:pgadmin_port`（默认 5050）

**登录信息**：

- 邮箱：配置参数中的 `pgadmin_email`，默认为 `postgres@example.com`
- 密码：配置参数中的 `database_password`

> **提示**
>
> 首次连接数据库时需输入 `database_password`。

**psql 命令行连接**

在安装了 PostgreSQL 客户端且网络可连接到数据库服务器的机器上，使用以下命令，按提示输入配置的 `database_password`：

```bash
psql -h 服务器IP -p postgres_port -U database_user -d database_name
```
