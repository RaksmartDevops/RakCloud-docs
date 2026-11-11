---
title: 应用中心产品手册
split_at: 2
sub_max_level: 2
version: 1.0.0
keywords: raksmart，应用中心，postgresql，pgadmin，psql，数据库，数据库备份。
description: PostgreSQL 是主流关系型数据库，本文介绍在 RakSmart 应用中心部署后的访问方式、关键信息、常用操作与安装验证。
---
# PostgreSQL 使用指南

## 访问应用

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

## 关键信息

| 项目 | 值/路径 |
| --- | --- |
| 默认数据库 | 配置参数 `database_name` |
| 管理脚本目录 | `/opt/cloud/postgres` |
| 数据存储目录 | `/opt/cloud/postgres/dbdata` |
| 备份目录 | `/opt/cloud/postgres/backups` |
| 凭证文件 | `/opt/cloud/postgres/credentials.txt` |
| PostgreSQL 端口 | 配置参数 `postgres_port`（默认 5432） |
| pgAdmin 端口 | 配置参数 `pgadmin_port`（默认 5050） |

## 常用操作

```bash
cd /opt/cloud/postgres

./start.sh      # 启动服务
./stop.sh       # 停止服务
./restart.sh    # 重启服务
./logs.sh       # 查看日志
./status.sh     # 查看状态
./backup.sh     # 执行数据库备份
```

## 验证安装

登录 pgAdmin 后，从左侧服务器列表展开“PostgreSQL Server”，确认默认数据库已创建。

## 深入学习

- [PostgreSQL 官方文档](https://www.postgresql.org/docs/)
- [pgAdmin 文档](https://www.pgadmin.org/docs/)
- [PostgreSQL 练习平台](https://pgexercises.com/)
