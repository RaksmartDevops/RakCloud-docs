---
title: 如何验证 IP 属性
---

### 通过 IPinfo 查询

1. 访问 [ipinfo.io](https://ipinfo.io/)。
    
2. 输入您的 IP 地址进行查询。
    
3. 查看 **ASN Type** 与 **Company Type**，两项均为 `isp`，即为双 ISP。
    

---

### 通过 WHOIS / BGP 查询

使用 WHOIS 或 [bgp.he.net](https://bgp.he.net/) 查询 IP，可查看 IP 的登记组织、ASN 编号和线路信息。

---

### 通过 IPQuality 检测脚本查询

[IPQuality](https://github.com/xykt/IPQuality) 是开源的 IP 质量检测脚本，可在服务器上运行，用于查看：

- IP 的基础信息与类型属性。
- 各数据库的风险评分与风险因子。
- 流媒体与 AI 平台的检测结果。
- 邮件端口连通性与黑名单情况。

具体使用方法请参考该项目主页说明。

> **说明**
> 
> - IPQuality 为第三方开源脚本，建议在使用前先查看脚本内容，并在测试环境中运行。
> - 不同数据库对同一 IP 的分类可能不一致，且数据存在更新延迟，检测结果仅供参考，具体识别结果以各平台实际策略为准。
