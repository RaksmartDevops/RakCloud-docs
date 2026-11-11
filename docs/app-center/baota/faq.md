---
title: 常见问题
---

| 问题 | 解决方案 |
| --- | --- |
| 无法访问面板 | 首次部署需等待几分钟初始化，请耐心等待，可登录虚拟机执行 `/opt/cloud/baota/logs.sh` 查看日志 |
| 在宿主机执行 `mysql` 命令提示未找到 | 应用运行在容器内，需先执行 `docker exec -it baota /bin/bash` 进入容器后再使用命令 |
| 忘记宝塔面板登录密码 | 查看 `/opt/cloud/baota/credentials.txt` 文件获取初始凭证 |
