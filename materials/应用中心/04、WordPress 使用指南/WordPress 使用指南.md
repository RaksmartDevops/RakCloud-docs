---
title: 应用中心产品手册
split_at: 2
sub_max_level: 2
version: 1.0.0
keywords: raksmart，应用中心，wordpress，建站，博客，lets encrypt，https，域名解析。
description: WordPress® 是全球最流行的建站系统，本文介绍在 RakSmart 应用中心部署后的访问方式、证书配置、初始化、常用操作与常见问题。
---
# WordPress 使用指南

## 访问应用

**获取访问信息**：登录 RakSmart 控制台，进入应用详情页面，查看访问地址。

**访问方式**：

- 博客首页：`https://您的域名`
- 管理后台：`https://您的域名/wp-admin/`

## 配置说明

WordPress® 应用通过域名访问，自动启用 HTTPS 加密保护您的站点和访客数据。

### 基础配置（自动申请证书）

如果您只有域名，还没有购买 SSL 证书，系统将自动从 Let's Encrypt 申请免费证书。

| 参数 | 说明 | 必填 |
| --- | --- | --- |
| `domain_name` | 您的域名（如 `blog.example.com`） | 是 |

> **注意**
>
> 域名需已解析到服务器 IP，并确认 80 端口可公网访问（用于证书验证）。

### 使用自有证书（可选）

如果您已购买商业证书，可额外提供以下参数：

| 参数 | 说明 | 必填 |
| --- | --- | --- |
| `cert_fullchain_b64` | 证书链（Base64 编码） | 否 |
| `cert_privkey_b64` | 私钥（Base64 编码） | 否 |

> **注意**
>
> 自有证书需与域名匹配。

配置完成后，访问地址为 `https://您的域名`。

## 初始化配置

首次访问时，WordPress® 将引导您完成安装：

1. 选择语言，点击 **Continue**。
2. 在 Welcome 页面填写站点信息：Site Title、Username、Password、Email。
3. 可选：设置搜索引擎可见性。
4. 点击 **Install WordPress** 完成安装。

## 关键信息

| 项目 | 路径/位置 |
| --- | --- |
| 运维脚本目录 | `/opt/cloud/wordpress` |
| 凭证信息 | `/opt/cloud/wordpress/credentials.txt` |
| 部署日志 | `/var/log/wordpress-setup.log` |
| 证书续期日志 | `/var/log/letsencrypt/renewal.log`（Let's Encrypt 模式） |

> **提示**
>
> MySQL 数据库密码由系统自动生成，可在 `/opt/cloud/wordpress/credentials.txt` 文件中查看。

## 常用操作

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

## 常见问题

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

## 深入学习

- [官方 WordPress® 文档](https://wordpress.org/documentation/)
- [WordPress® 开发者手册](https://developer.wordpress.org/)
- [学习 WordPress®（免费教程）](https://learn.wordpress.org/)
