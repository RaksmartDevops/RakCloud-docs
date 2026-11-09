# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

RakCloud（RakSmart）云产品官方文档站：VPS、独服（dedicatedserver）、裸机云（baremetal）、新手指南（beginners-guide）、IP 及网络服务（ip-network）、OPS 知识库（ops-knowledge-base）共六本书，用 VitePress 构建成静态站点。本仓库是 materials 素材和站点的**唯一源头**（此前并行的 Hugo 项目 `rs-docs-v2` 已归档到 `~/ccp/_archive/rs-docs-v2`，不再维护）。上线地址 `https://docs.raksmart.com/`（根路径）；发布采用"GitHub 构建产物 → `dist` 分支 → 文档服务器拉取到 staging → 人工晋升 production"，见"部署"一节。

## 常用命令

```bash
npm install                                   # 安装依赖（devDependencies：vitepress）
npm run docs:dev                              # 本地预览（vitepress dev docs）
npm run docs:build                            # 构建产物到 docs/.vitepress/dist（vitepress build docs）
npm run docs:preview                          # 预览构建产物

python3 scripts/convert_material_to_vitepress.py   # 从 materials/ 重新生成 docs/ 内容 + sidebar json
```

## 内容流水线：materials/ → docs/

这是本仓库最关键的架构点，不了解会踩坑：

- **`materials/`** 是产品文档的唯一源头（Format C 素材，按“书 → 章节目录 → .md 文件”组织，如 `materials/VPS/03、管理 VPS/管理 VPS.md`）。**改文档内容一律改这里**，改完需要重新跑一次转换脚本。日常编辑流程：本地用 Obsidian 打开本仓库的 `materials/` 目录（`materials/.obsidian` 已被 gitignore，不入库）编写 → 跑转换脚本重新生成 `docs/` → 本地 `npm run docs:build` 校验 → 提交并 push。
- **`docs/`** 不是手写的，是 `scripts/convert_material_to_vitepress.py` 从 `materials/` 生成后**提交进仓库的产物**（和一般“运行时生成、gitignore 掉”的 build 产物不同）。同时生成的还有 `docs/.vitepress/sidebar/<slug>.json`（`config.ts` 里 import 这些 JSON 拼进 `themeConfig.sidebar`，避免手写大量 sidebar 条目）。
- 转换脚本区分两种素材结构：
  - “一章节一文件”（VPS/独服/裸机云/新手指南）：`convert_book()`，按 H2 拆成多个独立页面
  - “分类目录多文件”（OPS 知识库）：`convert_ops_kb()`，一个 `.md` 就是一篇独立文章，H1 只作标题不进正文
- 脚本里的 `BOOKS` / `OPS_KB_CATEGORIES` 章节-slug 映射表最初照搬自已归档的 Hugo 项目（`~/ccp/_archive/rs-docs-v2/scripts/import_material_books.py`），已人工核对过，不要重新 derive；此后以本仓库的脚本为准，归档项目不再同步。
- 跨书/跨章节的相对链接（如 `[账单管理](账单管理.md#账单管理)`）转换脚本没法自动解析，只能靠脚本里的 `LINK_FIXES` 表逐条修复已知案例。
- **页内锚点（`#标题`）的处理（2026-11-09 起）**：`rewrite_links()` 对映射表里能查到的“引用另一整篇文档标题”式锚点（H2）改写为跨页链接；其余页内 H3/H4 锚点由 `slugify_anchor()` 按 VitePress 规则规范化（先 `unquote`，再小写、空白转 `-`，中文不变），所以 materials/ 里 Obsidian 风格的 `#标题%20带空格` 写法会被自动转成 `#标题-带空格`。注意 `docs/.vitepress/config.ts` 的 `ignoreDeadLinks: [/%/]` 仍会豁免含 `%` 的链接，构建绿灯不代表所有锚点都能跳转；新增文档时建议仍直接写标准格式。

### 新增手册与外部来稿的处理规则（2026-11-03）

- **新增一本书必须登记**：转换脚本是显式登记制，在 `materials/` 放新目录不会自动生成页面。需要同时改 `scripts/convert_material_to_vitepress.py`（`BOOKS` 增加书、章节、H2→slug 映射，`__main__` 增加 `convert_book(...)`）、`docs/.vitepress/config.ts`（import 侧边栏 JSON、`nav`、`sidebar`）、`docs/index.md`（首页卡片）。H2 标题与映射表对不上会直接抛 ValueError。例：`ip-network`（《IP及网络服务介绍》）。
- **图片引用必须写成 `./images/文件名.png`**：脚本只整份复制章节的 `images/` 目录，不改写路径。写成裸文件名（`xxx.png`）或错误的长路径，会让 `npm run docs:build` 报 `Could not resolve` 失败。2026-11-03 已修复注册、控制台手册中 4 处此类写法。
- **`docs/` 与 `materials/` 的不同步已消除**：2026-11-03 在 `docs/sync-colleague-edits` 分支按当前 `materials/` 重新生成过一次（24 个文件）。此前不同步的原因是 9 月 6 日同步 materials 后一直没重跑脚本，而重跑会被上述裸文件名图片路径挡住构建。
- **同事/外部提供整份手册副本时不要直接覆盖 `materials/`**：对方多半基于旧版修改。做法是以其所基于的旧版 commit 为基线，对每个有差异的文件做三方合并（`git merge-file <当前materials文件> <基线> <对方文件>`），只合入对方相对基线的增量，并核对其中是否有回退（如把 `#购买弹性-ip` 改回 `%20`）。
- 面向其他团队的简版发布流程见 [`deploy-overview.md`](deploy-overview.md)。

### 隐患修复记录（2026-09-02）

以下 2 处已经在 `materials/` 源头修复，`LINK_FIXES` 表也已同步补上，重新跑转换脚本会持续生成正确结果：
- `materials/新手指南/04、购买 RakSmart 产品/购买 RakSmart 产品.md`：`[账单管理](新手指南/08、账单管理/账单管理)` 这个残留的旧式路径改成了 `[账单管理](账单管理.md#账单管理)`，并在 `LINK_FIXES` 里新增 `"账单管理.md#账单管理": "/beginners-guide/billing/billing-management.md"`。
- `materials/VPS/03、管理 VPS/管理 VPS.md`：`[购买弹性 IP](#购买弹性%20IP)` 改成了 `[购买弹性 IP](#购买弹性-ip)`。

**原先记录的 5 处同类 `%20` 锚点问题，以及后来在 `elastic-ip.html` 发现的 `#购买弹性%20IP`，已于 2026-11-09 由脚本通用规范化一并解决**（无需再手改 materials/）。遗留的一处原文笔误：`materials/VPS/03、管理 VPS/管理 VPS.md:48` 链接末尾多了一个 `]`，尚未修改。

## 站点功能（2026-09-02 新增）

- **站内搜索**：`docs/.vitepress/config.ts` 里 `themeConfig.search: { provider: 'local' }`，用 VitePress 内置 minisearch，构建时自动为全站建索引，没有引入任何外部依赖/第三方服务。
- **首页样式**：只改了 `docs/.vitepress/theme/custom.css`（Hero 区域品牌橙渐变背景、Feature 卡片 hover 上浮+阴影），没有改 `docs/index.md` 的内容结构，也没有加任何具体数字类宣传文案（如 SLA、开通时长）——这类需要真实业务数据支撑的文案本轮刻意没加，避免不实宣传。
- PDF 导出功能已取消（`scripts/export-pdf.mjs`、puppeteer 依赖均已移除）。

## 部署

拉取模式：GitHub 只负责构建，不连任何服务器；文档服务器主动拉取，先到 staging 验证，再人工晋升到 production。生产服务器位于 JumpServer 之后，GitHub runner 无法 SSH 推送，所以不能用推送模式。

```text
push main → Actions 构建 → dist 分支（孤立提交，每次覆盖）
                              ↓ pull-dist.timer 每 2 分钟
              /var/www/releases/<sha>/    每个版本一份，不可变，保留最近 5 个
              /var/www/staging    → releases/<sha>    自动更新
              /var/www/production → releases/<sha>    仅 promote.sh 改变
```

- **`.github/workflows/build-dist.yml`**：PR 事件只构建校验，不发布；push `main` 或手动触发时构建并强制推送到 `dist` 分支。校验项：`index.html`/`404.html`/`sitemap.xml` 存在，产物中不含 `/rakcloud-docs/` 旧路径。`dist` 分支根目录就是站点根，附带 `BUILD_INFO`（源 commit SHA、构建时间）。Actions 均锁定到 commit SHA，由 Dependabot 提交升级 PR。
- **`deploy/`**：服务器端脚本与配置，详见 `deploy/README.md`。`pull-dist.sh` 拉取并切换 staging，`promote.sh` 晋升或回滚（秒级切软链接，无需重新构建），`nginx-docs.conf` 是测试机配置，`pull-dist.{service,timer}` 是 systemd 定时器。
- **`base` 为 `/`**，staging 与 production 使用同一份构建产物，不需要区分构建。
- **正式环境**：`https://docs.raksmart.com/`（production）与 `https://staging-docs.raksmart.com/`（staging），服务器 `199.180.101.100`。Nginx 按域名区分两个 server 块，证书需自行配置，写法见 `deploy/README.md`。
- **测试机** `47.103.103.48`（无域名）：production 在 `:80`，staging 在 `:8080`，脚本装在 `/opt/rakcloud-docs-deploy/`。SSH 用 `~/ccp/key_aly.pem`（RSA 私钥，不是 TLS 证书）连接 `root@47.103.103.48`。

常用操作（在服务器上执行）：

```bash
promote.sh --list      # 查看 staging / production 当前版本及可用版本
promote.sh             # 验证 staging 无误后晋升到 production
promote.sh <版本名>     # 回滚到 releases/ 下的旧版本
journalctl -u pull-dist.service -n 20   # 查看拉取日志
```

查看 Actions 运行情况：

```bash
gh run list -R RaksmartDevops/RakCloud-docs -w build-dist.yml
gh run view <run-id> -R RaksmartDevops/RakCloud-docs --log
```

旧的 `deploy.yml`（SSH + rsync 推送）和 GitHub secret `SERVER_SSH_KEY_B64` 已不再使用，secret 需在 GitHub 仓库设置中手动删除。
