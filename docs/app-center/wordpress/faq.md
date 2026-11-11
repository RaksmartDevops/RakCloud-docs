---
title: 常见问题
---

| 问题 | 解决方案 |
| --- | --- |
| Let's Encrypt 证书申请失败 | 检查域名是否已解析到服务器 IP，确认 80 端口可公网访问 |
| 域名无法访问 WordPress® 站点 | 参考下方“本机 DNS 缓存说明” |

### 本机 DNS 缓存说明

> **注意**
>
> 如果您配置的域名之前指向过其他服务器，本地电脑可能存在旧的 DNS 缓存，导致访问不到 WordPress® 站点。

**方法一：等待自动刷新**

DNS 缓存通常会在几分钟到几小时内自动更新。

**方法二：手动清除 DNS 缓存**

根据您的操作系统选择对应命令。

Windows：

```cmd
ipconfig /flushdns
```

macOS：

```bash
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

Linux：

```bash
sudo systemd-resolve --flush-caches
```

**方法三：验证域名解析是否生效**

```bash
nslookup 您的域名
```

确认返回的 IP 地址是否为您的服务器 IP。如果 IP 地址正确但仍无法访问，请检查防火墙设置和 80/443 端口是否开放。
