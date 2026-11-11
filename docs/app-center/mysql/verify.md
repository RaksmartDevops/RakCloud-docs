---
title: 验证安装
---

登录 phpMyAdmin 后，从左侧数据库列表确认默认数据库已创建，或通过命令行验证：

```bash
mysql -h 服务器IP -P mysql_port -u root -p -e "SHOW DATABASES;"
```
