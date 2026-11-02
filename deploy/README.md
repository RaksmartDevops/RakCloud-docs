# 文档服务器部署（拉取模式）

GitHub Actions 构建后把产物发布到 `dist` 分支；文档服务器**主动拉取**，先落到 staging 验证，再人工晋升到 production。服务器不需要对外开放 SSH，也不需要任何密钥（仓库公开，HTTPS 拉取）。

```text
push main → Actions 构建 → dist 分支
                              ↓ pull-dist.timer 每 2 分钟
              <WWW_ROOT>/releases/<sha>/   ← 每个版本一份，不可变
              <WWW_ROOT>/staging    → releases/<sha>   （自动更新）
              <WWW_ROOT>/production → releases/<sha>   （仅 promote.sh 改变）
```

软链接是**相对路径**，所以 Nginx 无论跑在宿主机还是容器里，只要整个 `WWW_ROOT` 被挂载就能解析。切换版本只改软链接，**不需要 reload Nginx**。

## 文件

| 文件 | 作用 |
|---|---|
| `pull-dist.sh` | 发现 `dist` 有新版本就下载校验，切换 staging；保留最近 5 个版本，不删在用版本；git 操作有超时保护 |
| `promote.sh` | 把 production 指向 staging 当前版本；也用于回滚 |
| `pull-dist.service` / `.timer` | systemd 定时拉取（每 2 分钟，单次最长 300 秒） |
| `nginx-docker/*.conf` | 正式服务器（Nginx 跑在 Docker 里）的两个站点配置 |
| `nginx-docs.conf` | 测试机（无域名、宿主机 Nginx）配置，按端口区分 |

## 正式服务器上线手册（199.180.101.100，Nginx 在 Docker 中）

现状：容器 `nginx`（host 网络），宿主机 `/opt/nginx/html` 挂载为容器内 `/usr/share/nginx/html`，`/opt/nginx/conf.d` 挂载为 `/etc/nginx/conf.d`，均由 `/opt/nginx/docker-compose.yaml` 管理。**不需要重建容器，也不需要改 compose**：我们的目录放在已挂载的 `/opt/nginx/html/rakcloud-docs/` 下即可。

宿主机路径与容器内路径对应关系：

| 宿主机 | 容器内 |
|---|---|
| `/opt/nginx/html/rakcloud-docs/staging` | `/usr/share/nginx/html/rakcloud-docs/staging` |
| `/opt/nginx/html/rakcloud-docs/production` | `/usr/share/nginx/html/rakcloud-docs/production` |

### 阶段 A：安装拉取脚本（不影响任何现有站点）

在仓库的 `deploy/` 目录下（先 `git clone` 本仓库或把该目录拷到服务器）：

```bash
sudo mkdir -p /opt/rakcloud-docs-deploy /opt/nginx/html/rakcloud-docs
sudo install -m 755 pull-dist.sh promote.sh /opt/rakcloud-docs-deploy/
sudo install -m 644 pull-dist.service pull-dist.timer /etc/systemd/system/

# 指向容器挂载目录下的专用子目录
sudo mkdir -p /etc/systemd/system/pull-dist.service.d
printf '[Service]\nEnvironment=WWW_ROOT=/opt/nginx/html/rakcloud-docs\n' | sudo tee /etc/systemd/system/pull-dist.service.d/env.conf

# 首次手动拉取，确认无报错（此时只会创建 releases/ 和 staging 链接）
sudo WWW_ROOT=/opt/nginx/html/rakcloud-docs /opt/rakcloud-docs-deploy/pull-dist.sh
ls -la /opt/nginx/html/rakcloud-docs        # 应看到 releases/ 和 staging -> releases/<sha>
sudo systemctl daemon-reload
sudo systemctl enable --now pull-dist.timer
```

### 阶段 B：上线 staging（`https://staging-docs.raksmart.com/`）

旧 staging 站点**归档，不删除**。归档目录放在 Web 根之外，不会被对外访问：

```bash
TS=$(date +%F-%H%M)
sudo mkdir -p /opt/nginx/archive/$TS

# 1. 备份旧 staging 的配置和内容
sudo cp -a /opt/nginx/conf.d/staging-docs.raksmart.com.conf /opt/nginx/archive/$TS/
sudo mv /opt/nginx/html/staging-docs.raksmart.com /opt/nginx/archive/$TS/

# 2. 换上新配置（deploy/nginx-docker/staging-docs.raksmart.com.conf）
sudo install -m 644 nginx-docker/staging-docs.raksmart.com.conf /opt/nginx/conf.d/staging-docs.raksmart.com.conf

# 3. 校验配置，通过后再 reload；校验失败不要 reload，直接按回退处理
docker exec nginx nginx -t && docker exec nginx nginx -s reload
```

验证：浏览器打开 `https://staging-docs.raksmart.com/`，检查首页、各书侧边栏、搜索、图片；命令行：

```bash
curl -sI https://staging-docs.raksmart.com/ | head -3
curl -s https://staging-docs.raksmart.com/BUILD_INFO
```

**staging 回退**（把旧站点放回去）：

```bash
sudo cp -a /opt/nginx/archive/$TS/staging-docs.raksmart.com.conf /opt/nginx/conf.d/
sudo mv /opt/nginx/archive/$TS/staging-docs.raksmart.com /opt/nginx/html/
docker exec nginx nginx -t && docker exec nginx nginx -s reload
```

### 阶段 C：上线 production（`https://docs.raksmart.com/`）

**staging 验证通过后再做。** 此步骤会替换对外的旧文档系统。

```bash
TS=$(date +%F-%H%M)
sudo mkdir -p /opt/nginx/archive/$TS

# 1. 晋升：production 链接指向 staging 验证过的同一个版本
sudo WWW_ROOT=/opt/nginx/html/rakcloud-docs /opt/rakcloud-docs-deploy/promote.sh

# 2. 归档旧站点的配置和内容
sudo cp -a /opt/nginx/conf.d/docs.raksmart.com.conf /opt/nginx/archive/$TS/
sudo mv /opt/nginx/html/docs.raksmart.com /opt/nginx/archive/$TS/

# 3. 换上新配置并 reload
sudo install -m 644 nginx-docker/docs.raksmart.com.conf /opt/nginx/conf.d/docs.raksmart.com.conf
docker exec nginx nginx -t && docker exec nginx nginx -s reload
```

**production 回退**同上，把 `docs.raksmart.com` 的配置和目录放回去并 reload，几秒内恢复旧站点。

> **旧链接**：旧站点的路径（如 `/raksmart/zh/...`、`/marketplace/zh/...`）与新站点结构不同，切换后这些旧 URL 会返回 404。上线 production 前需要决定是否做旧→新路径的 301 跳转（影响外部引用和搜索引擎收录）。

### 注意

- 其他域名（`documents.petacloud.ai`、`test-docs.raksmart.com`、`default.conf`）的配置本手册均不触碰。
- 日常的版本更新**只**走 `pull-dist.sh`（自动）和 `promote.sh`（人工），不再需要碰 Nginx。只有改站点配置时才需要 `nginx -t` 与 reload。

## 日常操作

```bash
# 服务器上若设置了环境变量 WWW_ROOT，脚本会自动使用；未设置则默认 /var/www
export WWW_ROOT=/opt/nginx/html/rakcloud-docs

promote.sh --list      # 查看 staging / production 当前版本及所有可用版本
promote.sh             # 验证 staging 无误后晋升到 production
promote.sh <版本名>     # 回滚：指向 releases/ 下任一旧版本（晋升时会打印上一个版本名）
journalctl -u pull-dist.service -n 20   # 查看拉取日志
```

回滚只是切换软链接，秒级生效，不需要重新构建，也不需要 reload。

## 可调参数（环境变量）

`REPO_URL`、`DIST_BRANCH`、`WWW_ROOT`（默认 `/var/www`）、`KEEP_RELEASES`（默认 5）、`GIT_TIMEOUT_SECS`（默认 120）。通过 `pull-dist.service.d/env.conf` 里的 `Environment=` 行设置。

## 测试机（47.103.103.48）

无域名、宿主机 Nginx：`nginx-docs.conf` 里 production 监听 80，staging 监听 8080。脚本装在 `/opt/rakcloud-docs-deploy/`，`WWW_ROOT` 用默认的 `/var/www`。
