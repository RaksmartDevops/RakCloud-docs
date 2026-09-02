# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

RakCloud（RakSmart）云产品官方文档站：VPS、独服（dedicatedserver）、裸机云（baremetal）、新手指南（beginners-guide）、OPS 知识库（ops-knowledge-base）共五本书，用 VitePress 构建成静态站点，发布在 `http://47.103.103.48/rakcloud-docs/`。

## 常用命令

```bash
npm install                                   # 安装依赖（devDependencies：vitepress、puppeteer）
npm run docs:dev                              # 本地预览（vitepress dev docs）
npm run docs:build                            # 构建产物到 docs/.vitepress/dist（vitepress build docs）
npm run docs:preview                          # 预览构建产物
npm run docs:pdf                              # 构建后运行，把 4 本产品手册导出成整书 PDF（需要先 docs:build）

python3 scripts/convert_material_to_vitepress.py   # 从 materials/ 重新生成 docs/ 内容 + sidebar json
```

## 内容流水线：materials/ → docs/

这是本仓库最关键的架构点，不了解会踩坑：

- **`materials/`** 是产品文档的唯一源头（Format C 素材，按“书 → 章节目录 → .md 文件”组织，如 `materials/VPS/03、管理 VPS/管理 VPS.md`）。**改文档内容一律改这里**，改完需要重新跑一次转换脚本。后续所有内容编辑都直接在 GitHub 上进行，不需要在本地维护一份常驻 clone——需要跑脚本/构建校验时，临时 clone 一份到本地即可，用完不必保留。
- **`docs/`** 不是手写的，是 `scripts/convert_material_to_vitepress.py` 从 `materials/` 生成后**提交进仓库的产物**（和一般“运行时生成、gitignore 掉”的 build 产物不同）。同时生成的还有 `docs/.vitepress/sidebar/<slug>.json`（`config.ts` 里 import 这些 JSON 拼进 `themeConfig.sidebar`，避免手写大量 sidebar 条目）。
- 转换脚本区分两种素材结构：
  - “一章节一文件”（VPS/独服/裸机云/新手指南）：`convert_book()`，按 H2 拆成多个独立页面
  - “分类目录多文件”（OPS 知识库）：`convert_ops_kb()`，一个 `.md` 就是一篇独立文章，H1 只作标题不进正文
- 脚本里的 `BOOKS` / `OPS_KB_CATEGORIES` 章节-slug 映射表照搬自姊妹项目 `rs-docs-v2/scripts/import_material_books.py`（Hugo 版本的同款转换脚本），已人工核对过，不要重新 derive。
- 跨书/跨章节的相对链接（如 `[账单管理](账单管理.md#账单管理)`）转换脚本没法自动解析，只能靠脚本里的 `LINK_FIXES` 表逐条修复已知案例。
- **页内锚点（`#标题`）转换脚本不做任何 slugify**：`rewrite_links()` 只处理映射表里能查到的"引用另一整篇文档标题"式锚点（对应 H2），对页内 H3/H4 级锚点一律原样保留，默认假设 materials/ 原文写的就是 VitePress 会自动生成的标准格式（小写 + 空格转连字符）。**如果 materials/ 原文用了 Obsidian 导出习惯的 `#标题%20带空格` 写法，这个假设就不成立，会产生实际跳转失效但构建不报错的死锚点**（`docs/.vitepress/config.ts` 的 `ignoreDeadLinks: [/%/]` 会把这类链接从死链检查里豁免掉，所以构建绿灯不代表锚点都能跳转）。

### 隐患修复记录（2026-09-02）

以下 2 处已经在 `materials/` 源头修复，`LINK_FIXES` 表也已同步补上，重新跑转换脚本会持续生成正确结果：
- `materials/新手指南/04、购买 RakSmart 产品/购买 RakSmart 产品.md`：`[账单管理](新手指南/08、账单管理/账单管理)` 这个残留的旧式路径改成了 `[账单管理](账单管理.md#账单管理)`，并在 `LINK_FIXES` 里新增 `"账单管理.md#账单管理": "/beginners-guide/billing/billing-management.md"`。
- `materials/VPS/03、管理 VPS/管理 VPS.md`：`[购买弹性 IP](#购买弹性%20IP)` 改成了 `[购买弹性 IP](#购买弹性-ip)`。

**以下 5 处同类 `#标题%20带空格` 锚点问题仍未修复**（用户明确决定本轮只处理上面 2 处已知案例，暂不做脚本层的通用 slugify 规则，也不逐一手改剩余案例）：
- `materials/VPS/03、管理 VPS/管理 VPS.md:73` — `[查看 VPS 详情信息](#查看%20VPS%20详情信息)`
- `materials/VPS/03、管理 VPS/管理 VPS.md:74` — `[执行 VPS 操作](#执行%20VPS%20操作)`
- `materials/VPS/03、管理 VPS/管理 VPS.md:142` — `[弹性 IP](#弹性%20IP)`
- `materials/VPS/02、快速入门/快速入门.md:83` — `[通过官网 VPS 入口购买](#通过官网%20VPS%20入口购买)`
- `materials/VPS/02、快速入门/快速入门.md:214` 和 `:224` — `[登录 VPS](#登录%20VPS)`、`[购买 VPS](#购买%20VPS)`

这些链接目前点击后跳转不到目标位置（非阻断性问题，不影响构建/发布）。如果以后要处理，做法是把 `#标题%20带空格` 改成 `#标题-带空格对应部分转小写连字符`（例如 `#购买弹性-ip` 这个已验证过的写法：原标题空格转 `-`，英文字母转小写，中文字符不变）。**新增文档时如果沿用 Obsidian 导出的 `%20` 锚点写法，会持续产生同类问题**，写作时应直接使用 VitePress 标准锚点格式。

## 站点功能（2026-09-02 新增）

- **站内搜索**：`docs/.vitepress/config.ts` 里 `themeConfig.search: { provider: 'local' }`，用 VitePress 内置 minisearch，构建时自动为全站建索引，没有引入任何外部依赖/第三方服务。
- **首页样式**：只改了 `docs/.vitepress/theme/custom.css`（Hero 区域品牌橙渐变背景、Feature 卡片 hover 上浮+阴影），没有改 `docs/index.md` 的内容结构，也没有加任何具体数字类宣传文案（如 SLA、开通时长）——这类需要真实业务数据支撑的文案本轮刻意没加，避免不实宣传。
- **产品手册 PDF 导出**：`scripts/export-pdf.mjs`，新增 `puppeteer` devDependency（无头 Chromium 渲染，只在生成 PDF 这一步用到）。
  - 只覆盖 VPS / 独服 / 裸机云 / 新手指南 4 本"产品手册"类书；OPS 知识库（126 篇散文章）不做整书合并，判断是合并成一份大 PDF 对这类知识库文章集合意义不大。
  - 原理：起本地静态服务器 serve 已构建的 `docs/.vitepress/dist/`，puppeteer 按 `docs/.vitepress/sidebar/<book>.json` 的章节/页面顺序依次打开每一页，提取 `.vp-doc` 正文 HTML 拼成一份大 HTML（章节分隔页 + 扉页），再整体 `page.pdf()` 一次性输出，比逐页转 PDF 再合并更简单。
  - 输出到 `docs/.vitepress/dist/pdf/<book-slug>.pdf`（写进已构建的 dist 里，dist 本来就不进 git、每次部署整份 rsync 过去，不需要额外拷贝逻辑）。
  - PDF 下载入口**没有**写进 `docs/*.md`（那是转换脚本生成的产物，手改了下次重新转换会被覆盖），而是在 `config.ts` 里用 `withPdfDownload()` 给对应书的 sidebar 数组顶部插入一条"⬇ 下载 PDF 手册"链接——`config.ts` 是手工维护文件，不受脚本重跑影响。
  - **CI 中文字体风险**：`ubuntu-latest` runner 默认没有中文字体，无头 Chromium 渲染中文转 PDF 会变方块，`deploy.yml` 里在跑 `docs:pdf` 之前加了 `apt-get install -y fonts-noto-cjk`。本机 macOS 有中文字体，本地验证不出这个问题，第一次在 CI 上跑 `docs:pdf` 时需要重点看生成的 PDF 是否正常。

## 部署

- `.github/workflows/deploy.yml`：**仅 `workflow_dispatch` 手动触发**（不会因为 push 到 main 自动部署）。
- **如何在 GitHub 上查看**：仓库页面 → **Actions** 标签 → 左侧 "Deploy RakCloud Docs" workflow → 点进具体一次 run，可以看到 build、rsync、curl 校验每一步的日志。
  - 命令行等效操作：
    ```bash
    gh run list -R RaksmartDevops/RakCloud-docs -w deploy.yml   # 列出历史运行记录
    gh run view <run-id> -R RaksmartDevops/RakCloud-docs --log  # 查看某次运行的完整日志
    gh workflow run deploy.yml -R RaksmartDevops/RakCloud-docs  # 手动触发一次部署
    gh run watch -R RaksmartDevops/RakCloud-docs                # 触发后跟踪运行状态
    ```
- 部署链路：checkout → setup-node@20 → `npm ci` → `npm run docs:build` → 校验 `docs/.vitepress/dist/index.html` 存在 → 安装中文字体（`fonts-noto-cjk`）→ `npm run docs:pdf` 生成 4 本产品手册 PDF → 用 GitHub secret `SERVER_SSH_KEY_B64`（base64 编码的 SSH 私钥）准备好 `~/.ssh/deploy_key` → `rsync -az --delete` 到 `root@47.103.103.48:/var/www/rakcloud-docs/` → curl 校验 `http://47.103.103.48/rakcloud-docs/` 返回 200。
- 服务器上的 Nginx 配置（`/etc/nginx/sites-available/docs-raksmart`，不在本仓库里）已有 `/rakcloud-docs/` 的 location block（`alias /var/www/rakcloud-docs/`），不需要改动。
- 本地临时验证可参考：SSH 用 `~/ccp/key_aly.pem`（RSA 私钥，不是 TLS 证书）连接 `root@47.103.103.48`。
