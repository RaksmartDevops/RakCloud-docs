# 文档部署与更新流程（简版）

面向需要了解 RakCloud 文档站如何更新、如何上线的团队。完整操作细节见 [deploy.md](deploy.md)，服务器部署见 [deploy/README.md](deploy/README.md)。

## 1. 一句话概括

文档源文件放在 GitHub 仓库，合并到 `main` 后由 GitHub Actions 自动构建；文档服务器**自己定时来拉取**构建产物，先更新到 staging 验收，确认无误后再由人工晋升到 production。

## 2. 整体流程

```text
编辑 materials/ → 转换生成 docs/ → 提交 PR → 合并 main
                                              │
                                  GitHub Actions 构建网站
                                              │ 推送到 dist 分支
                                              ▼
                       文档服务器每 2 分钟拉取 dist
                          ├─ staging     自动更新（验收用）
                          └─ production  人工晋升（对外）
```

| 环境 | 地址 | 更新方式 |
|---|---|---|
| staging | `https://staging-docs.raksmart.com/` | 自动，合并后约 2～5 分钟 |
| production | `https://docs.raksmart.com/` | 人工晋升（目前尚未切换，仍为旧文档系统） |

## 3. GitHub 端

仓库：`RaksmartDevops/RakCloud-docs`

| 内容 | 说明 |
|---|---|
| `materials/` | 文档源文件（唯一需要手工编辑的内容），按「书 → 章节 → md」组织 |
| `docs/` | 由脚本从 `materials/` 生成，**不要手改** |
| `main` 分支 | 受 PR 流程管理，不直接提交 |
| PR 检查 | 只构建校验，不发布；变绿才能合并 |
| `dist` 分支 | Actions 自动生成的构建产物，每次覆盖，**不要手改**；`BUILD_INFO` 文件记录对应的源 commit 和构建时间 |

**更新文档的步骤（贡献者）：**
1. 从最新 `main` 建分支：`git checkout main && git pull && git checkout -b docs/<主题>`
2. 只修改 `materials/` 下的文档
3. 运行 `python3 scripts/convert_material_to_vitepress.py` 生成 `docs/`，再 `npm run docs:build` 本地校验
4. 提交并推送，在 GitHub 上开 PR
5. PR 的 `build` 检查通过后，由负责人合并

**写作约定：**
- 图片引用写成 `./images/文件名.png`，不要只写文件名
- 页内锚点使用 `#标题-小写连字符` 格式，不要用 `%20`

## 4. 文档服务器端

服务器 `199.180.101.100`，网站由 Docker 中的 Nginx 提供。**GitHub 不连接服务器**，由服务器主动拉取，因此服务器不需要对外开放推送入口。

目录结构（`/opt/nginx/html/rakcloud-docs/`）：

```text
releases/<sha>/    每个版本一份，不可变，保留最近 5 个
staging    → releases/<sha>    定时器自动指向最新版本
production → releases/<sha>    仅人工晋升时改变
```

- **自动拉取**：`pull-dist.timer` 每 2 分钟检查 `dist` 分支，有新版本就下载并切换 staging。
- **晋升**：staging 验收通过后，由运维在服务器上执行 `promote.sh`，production 指向 staging 当前版本，**秒级生效，无需重启 Nginx**。
- **回滚**：`promote.sh <版本名>` 指回旧版本，同样秒级生效。

## 5. 验收与排查

**验收（任何人都可以做）：**

```bash
curl -s https://staging-docs.raksmart.com/BUILD_INFO
```

返回的 `commit=` 应等于刚合并到 `main` 的 commit，再在浏览器检查被改动的页面。

**常见情况：**

| 现象 | 处理 |
|---|---|
| PR 的 `build` 变红 | 看 Actions 日志，多为图片路径或标题与映射表不一致 |
| 合并后 staging 长时间未更新 | 请运维检查服务器上的 `pull-dist.service` 日志与 `WWW_ROOT` 配置 |
| 需要紧急撤回 | 请运维执行 `promote.sh <旧版本名>` 回滚 |

## 6. 角色分工

| 角色 | 负责 |
|---|---|
| 文档编辑 | 修改 `materials/`，提交 PR |
| 评审/合并人 | 检查 PR，合并到 `main` |
| 运维 | 服务器端定时器、Nginx、`promote.sh` 晋升与回滚 |
