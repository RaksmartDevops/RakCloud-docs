---
title: 应用中心产品手册
split_at: 2
sub_max_level: 2
version: 1.0.0
keywords: raksmart，应用中心，mysql，phpmyadmin，数据库，数据库备份，数据库恢复。
description: MySQL 是主流关系型数据库，本文介绍在 RakSmart 应用中心部署后的访问方式、关键信息、常用操作与安装验证。
---
# MySQL 使用指南

## 访问应用

**phpMyAdmin 管理界面**：`http://服务器IP:phpmyadmin_port`（默认 8080）

**登录信息**：使用配置的数据库用户登录。

- 用户名：配置参数中的 `database_user`（不可为 `root`）
- 密码：配置参数中的 `database_password`

**MySQL 命令行连接**

在安装了 MySQL 客户端且网络可连接到数据库服务器的机器上，使用以下命令：

```bash
mysql -h 服务器IP -P mysql_port -u database_user -p database_name
```

输入配置的 `database_password` 后进入数据库。

## 关键信息

| 项目 | 值/路径 |
| --- | --- |
| MySQL 端口 | 配置参数 `mysql_port`（默认 3306） |
| phpMyAdmin 端口 | 配置参数 `phpmyadmin_port`（默认 8080） |
| 默认数据库 | 配置参数 `database_name` |
| 管理脚本目录 | `/opt/cloud/mysql` |
| 数据库用户 | 配置参数 `database_user`（不可为 `root`） |
| 数据库密码 | 配置参数 `database_password` |
| Root 密码 | 默认为配置参数 `database_password` |
| 数据存储目录 | `/opt/cloud/mysql/dbdata` |
| 备份目录 | `/opt/cloud/mysql/backups` |
| 凭证文件 | `/opt/cloud/mysql/credentials.txt` |

## 常用操作

```bash
cd /opt/cloud/mysql

./start.sh      # 启动服务
./stop.sh       # 停止服务
./restart.sh    # 重启服务
./status.sh     # 查看状态
./logs.sh       # 查看日志
./backup.sh     # 执行数据库备份
./restore.sh    # 恢复数据库
```

## 验证安装

登录 phpMyAdmin 后，从左侧数据库列表确认默认数据库已创建，或通过命令行验证：

```bash
mysql -h 服务器IP -P mysql_port -u root -p -e "SHOW DATABASES;"
```

## 深入学习

- [MySQL 官方文档](https://dev.mysql.com/doc/)
- [phpMyAdmin 官方文档](https://docs.phpmyadmin.net/)
- [W3Schools MySQL 教程](https://www.w3schools.com/mysql/)
