# 企业邮箱 FAQ

## 概述

本文解答 RAKsmart 配套企业邮箱的登录、管理与配置常见问题。

## 1. 邮件服务器在国内还是国外？

服务器节点全球分布：海外访问使用海外节点，国内访问使用国内节点，以保证不同地区的收发速度与稳定性。

## 2. 企业邮箱有独立的管理员账号吗？

有。邮箱开通后，平台会提供管理员账号和密码。

- 登录地址：[https://mail.chengmail.cn](https://mail.chengmail.cn/)
- 默认进入用户登录页面
- 在「欢迎登录邮箱」右侧点击「切换至管理员登录」
- 使用管理员账号登录后台

## 3. 忘记企业邮箱管理员密码怎么办？

管理员密码只能在后台重置，无法自助找回。请通过客户中心提交工单申请重置，并提供域名或邮箱产品订单信息。

## 4. 企业邮箱帮助中心

- <https://mail.chengmail.cn/help/index.php?_m=articleview&_a=view>
- [中文版使用手册](https://mail.chengmail.cn/help/index.php?_m=articleview&_a=view&category_id=044f972f81a3be258c2c35e8ae6ee6d8&lang=zh_CN)

## 5. 如何配置 SMTP？MX、CNAME、TXT 记录如何设置？

登录企业邮箱管理员后台，进入「域名管理」或「邮箱设置」，系统会显示该域名所需的记录，通常包括：

| 记录类型 | 用途 |
| --- | --- |
| MX | 邮件收发路由 |
| TXT（SPF） | 防伪造、提升投递成功率 |
| CNAME | 部分功能所需，以后台显示为准 |
| SMTP | 发信服务器地址与端口，以后台显示为准 |

具体记录值因域名而异，请以管理员后台显示为准。若无法找到，请提交工单并提供域名。

## 6. 如何创建和管理员工邮箱？

使用管理员账号登录 [mail.chengmail.cn](https://mail.chengmail.cn/) 后，可在管理后台创建或删除邮箱、分配容量、设置别名与转发。详细步骤见[企业邮箱帮助中心](https://mail.chengmail.cn/help/index.php?_m=articleview&_a=view&category_id=044f972f81a3be258c2c35e8ae6ee6d8&lang=zh_CN)。

## 7. 需要技术支持

请通过客户中心提交工单，并提供域名、问题描述及已尝试的步骤和截图。
