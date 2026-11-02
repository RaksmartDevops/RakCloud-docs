# 文档服务器部署（拉取模式）

GitHub Actions 构建后把产物发布到 `dist` 分支；文档服务器**主动拉取**，先落到 staging 验证，再人工晋升到 production。服务器不需要对外开放 SSH，也不需要任何密钥（仓库公开，HTTPS 拉取）。

```text
push main → Actions 构建 → dist 分支
                              ↓ pull-dist.timer 每 2 分钟
              /var/www/releases/<sha>/   ← 每个版本一份，不可变
              /var/www/staging    → releases/<sha>   （自动更新）
              /var/www/production → releases/<sha>   （仅 promote.sh 改变）
```

## 文件

| 文件 | 作用 |
|---|---|
| `pull-dist.sh` | 发现 `dist` 有新版本就下载校验，切换 staging；保留最近 5 个版本，不删在用版本 |
| `promote.sh` | 把 production 指向 staging 当前版本；也用于回滚 |
| `nginx-docs.conf` | 测试机配置（按端口区分 staging / production） |
| `pull-dist.service` / `.timer` | systemd 定时拉取 |

## 在服务器上安装

需要 `git`、`nginx`、`systemd`、`flock`（Ubuntu 默认具备）。

```bash
sudo mkdir -p /opt/rakcloud-docs-deploy
sudo install -m 755 pull-dist.sh promote.sh /opt/rakcloud-docs-deploy/
sudo install -m 644 pull-dist.service pull-dist.timer /etc/systemd/system/
sudo /opt/rakcloud-docs-deploy/pull-dist.sh          # 首次手动拉取，确认无报错
sudo /opt/rakcloud-docs-deploy/promote.sh            # 首次晋升，创建 production 链接
sudo systemctl daemon-reload
sudo systemctl enable --now pull-dist.timer
```

## Nginx（正式服务器：按域名区分）

`nginx-docs.conf` 里的缓存、压缩、404 配置可直接沿用，只需把两个 server 块改成按域名区分，并加上证书：

```nginx
server {
    listen 443 ssl;
    server_name staging-docs.raksmart.com;      # 另一块为 docs.raksmart.com
    root /var/www/staging;                      # 另一块为 /var/www/production
    ssl_certificate     /path/to/fullchain.pem; # 按实际证书路径填写
    ssl_certificate_key /path/to/privkey.pem;
    # 其余与 nginx-docs.conf 相同
}
```

`base` 为 `/`，staging 与 production 使用同一份构建产物，无需区分构建。

## 日常操作

```bash
promote.sh --list      # 查看 staging / production 当前版本及所有可用版本
promote.sh             # 验证 staging 无误后晋升到 production
promote.sh <版本名>     # 回滚：指向 releases/ 下任一旧版本（晋升时会打印上一个版本名）
journalctl -u pull-dist.service -n 20   # 查看拉取日志
```

回滚只是切换软链接，秒级生效，不需要重新构建。

## 可调参数（环境变量）

`REPO_URL`、`DIST_BRANCH`、`WWW_ROOT`（默认 `/var/www`）、`KEEP_RELEASES`（默认 5）。如需修改，在 `pull-dist.service` 的 `[Service]` 下加 `Environment=` 行。
