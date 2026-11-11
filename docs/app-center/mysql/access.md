---
title: 访问应用
---

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
