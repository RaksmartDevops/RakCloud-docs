---
title: 常用操作
---

进入脚本目录后执行相应命令：

```bash
cd /opt/cloud/wordpress

./start.sh      # 启动服务
./stop.sh       # 停止服务
./restart.sh    # 重启服务（配置变更后执行）
./status.sh     # 查看服务状态
./logs.sh       # 查看应用日志
```

查看日志：

```bash
./logs.sh                          # 查看实时应用日志（Ctrl+C 退出）
cat /var/log/wordpress-setup.log   # 查看部署日志
```
