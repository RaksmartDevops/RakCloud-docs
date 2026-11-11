---
title: 访问应用
---

**Web 控制台**

访问 `http://[您的服务器IP]:[gateway_port]`。端口默认为 `18789`，若有自定义配置，请以产品详情页中的 `gateway_port` 参数为准。

**Gateway 令牌登录**

首次访问时需要输入 Gateway 令牌。通过 SSH 连接至服务器后，执行以下命令查看凭据中的 `Gateway Token`（以实际部署为准）：

```bash
cat /opt/cloud/openclaw/credentials.txt
```

凭据文件内容示例：

```text
Gateway Port:    18789
Default Model:   anthropic/claude-sonnet-4-6
Gateway Token:   <您的 Gateway Token>
```

将 `Gateway Token` 填入登录页面即可登录。
