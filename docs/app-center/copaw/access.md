---
title: 访问应用
---

**Web 控制台**

访问 `http://[您的服务器IP]:[copaw_port]`。端口默认为 `8088`，可在部署参数中通过 `copaw_port` 自定义，具体以产品详情页中的参数值为准。

**初始账号和密码**

账号为部署时填写的管理员账号，可从应用参数配置详情中获取，也可通过 SSH 连接至服务器后执行以下命令查看：

```bash
cat /opt/cloud/copaw/credentials.txt
```
