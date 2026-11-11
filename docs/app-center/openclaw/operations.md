---
title: 常用操作
---

进入 `/opt/cloud/openclaw` 目录，或直接执行以下预设管理脚本：

| 操作 | 命令 |
| --- | --- |
| 启动服务 | `/opt/cloud/openclaw/start.sh` |
| 停止服务 | `/opt/cloud/openclaw/stop.sh` |
| 重启服务 | `/opt/cloud/openclaw/restart.sh` |
| 查看日志 | `/opt/cloud/openclaw/logs.sh` 或 `docker logs openclaw-gateway` |
| 更新至最新版并重启 | `/opt/cloud/openclaw/update.sh` |
| 执行 OpenClaw 配置命令 | `/opt/cloud/openclaw/openclaw_cmd.sh` |

> **提示**
>
> 更新后 Gateway 会自动重启并加载新版本。若更新后出现异常，可参考“深入学习”中的官方文档进行故障排查。
