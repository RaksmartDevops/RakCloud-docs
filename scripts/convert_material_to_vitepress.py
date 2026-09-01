#!/usr/bin/env python3
"""将 materials/<书名>/ 下的 Format C 素材转换成 docs/<slug>/ 下的 VitePress 页面。

BOOKS 字典里的章节/H2/slug 映射，以及 OPS_KB_CATEGORIES 里的分类/文件/slug 映射，
均照搬自 rs-docs-v2/scripts/import_material_books.py 里已经人工确认过的同名数据
（BOOKS 第 18-266 行、OPS_KB_CATEGORIES 第 330-474 行），素材目录结构已核实与
rs-docs-v2 完全一致，不重新核对内容。

设计上和 Hugo 那边的转换脚本（import_material_books.py）不同：
- 正文（表格/加粗/斜体/引用块/代码围栏）直接透传保留原始 Markdown 语法，不重新拼 HTML
- H3/H4 页内锚点不用手写 slugify，VitePress/markdown-it 自动生成
- 图片相对路径（./images/xxx.png）不需要重写，只需要把 images/ 目录整份复制过去

本脚本处理两种素材结构：
- "一章节一文件"（标准 Format C）：convert_book()，一个 .md 按 H2 拆成多个独立页面
- "分类目录多文件"（OPS 知识库变体）：convert_ops_kb()，一个 .md 本身就是一篇独立文章，
  不按 H2 拆分，H1 只作为文章标题（不进正文），H2/H3/H4 保留在正文里作为文章内小节

同时生成 docs/.vitepress/sidebar/<slug>.json，作为脚本生成后提交进仓库的产物
（和 docs/vps/*.md 同类，不是运行时生成），config.ts 里 import 这些 JSON 拼进 sidebar，
避免手写大量 sidebar 条目。
"""

import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote

MATERIALS_DIR = Path(__file__).resolve().parent.parent / "materials"
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
SIDEBAR_DIR = DOCS_DIR / ".vitepress" / "sidebar"

BOOKS = {
    "vps": {
        "slug": "vps",
        "title": "VPS",
        "material_dir": "VPS",
        "chapters": [
            {
                "dir": "01、产品介绍",
                "file": "产品介绍.md",
                "slug": "product-intro",
                "weight": 10,
                "docs": {
                    "产品概述": "overview",
                    "产品优势": "advantages",
                    "产品类型": "product-types",
                    "区域和可用区": "regions-and-zones",
                },
            },
            {
                "dir": "02、快速入门",
                "file": "快速入门.md",
                "slug": "quickstart",
                "weight": 20,
                "docs": {
                    "购买 VPS": "purchase",
                    "登录 VPS": "login",
                },
            },
            {
                "dir": "03、管理 VPS",
                "file": "管理 VPS.md",
                "slug": "manage-vps",
                "weight": 30,
                "docs": {
                    "查看已购的 VPS": "view-instances",
                    "查看 VPS 详情信息": "instance-details",
                    "执行 VPS 操作": "vps-operations",
                    "弹性 IP": "elastic-ip",
                    "独立云盘": "cloud-disk",
                    "安全组": "security-groups",
                    "VPS 升降级": "upgrade-downgrade",
                    "VPS 取消": "cancellation",
                    "账单与续费管理": "billing",
                    "新开工单": "new-ticket",
                },
            },
        ],
    },
    "dedicatedserver": {
        "slug": "dedicatedserver",
        "title": "物理服务器",
        "material_dir": "独服",
        "chapters": [
            {
                "dir": "01、产品介绍",
                "file": "产品介绍.md",
                "slug": "product-intro",
                "weight": 10,
                "docs": {
                    "产品简介": "overview",
                    "产品优势": "advantages",
                    "产品类型": "product-types",
                    "区域和可用区": "regions-and-zones",
                },
            },
            {
                "dir": "02、快速入门",
                "file": "快速入门.md",
                "slug": "quickstart",
                "weight": 20,
                "docs": {
                    "购买物理服务器": "purchase",
                    "登录物理服务器": "login",
                },
            },
            {
                "dir": "03、管理物理服务器",
                "file": "管理物理服务器.md",
                "slug": "manage-servers",
                "weight": 30,
                "docs": {
                    "查看已购的物理服务器": "view-servers",
                    "查看服务器详细信息": "server-details",
                    "执行服务器操作": "server-operations",
                    "物理服务器取消": "cancellation",
                    "账单与续费管理": "billing",
                    "新开工单": "new-ticket",
                },
            },
        ],
    },
    "baremetal": {
        "slug": "baremetal",
        "title": "裸机云",
        "material_dir": "裸机云",
        "chapters": [
            {
                "dir": "01、产品介绍",
                "file": "产品介绍.md",
                "slug": "product-intro",
                "weight": 10,
                "docs": {
                    "产品简介": "overview",
                    "产品优势": "advantages",
                    "产品类型": "product-types",
                    "区域和可用区": "regions-and-zones",
                },
            },
            {
                "dir": "02、快速入门",
                "file": "快速入门.md",
                "slug": "quickstart",
                "weight": 20,
                "docs": {
                    "购买裸机云": "purchase",
                    "登录裸机云": "login",
                },
            },
            {
                "dir": "03、管理裸机云",
                "file": "管理裸机云.md",
                "slug": "manage-baremetal",
                "weight": 30,
                "docs": {
                    "查看已购的裸机云": "view-instances",
                    "查看裸机云详细信息": "instance-details",
                    "执行服务器操作": "server-operations",
                    "管理安全组": "security-groups",
                    "裸机云升降级": "upgrade-downgrade",
                    "裸机云取消": "cancellation",
                    "账单与续费管理": "billing",
                    "新开工单": "new-ticket",
                },
            },
        ],
    },
    "beginners-guide": {
        "slug": "beginners-guide",
        "title": "新手指南",
        "material_dir": "新手指南",
        "chapters": [
            {
                "dir": "01、了解 RakSmart",
                "file": "了解 RakSmart.md",
                "slug": "about-raksmart",
                "weight": 10,
                "docs": {
                    "产品和服务": "products-and-services",
                    "区域和可用区": "regions-and-zones",
                },
            },
            {
                "dir": "02、注册 RakSmart 账号",
                "file": "注册 RakSmart 账号.md",
                "slug": "register-account",
                "weight": 20,
                "docs": {
                    "通过官网首页注册": "register-via-website",
                    "使用 QQ 账号快捷注册": "qq-register",
                },
            },
            {
                "dir": "03、了解 RakSmart 控制台",
                "file": "了解 RakSmart 控制台.md",
                "slug": "console-overview",
                "weight": 30,
                "docs": {
                    "控制台简介": "console-intro",
                    "登录控制台": "login-console",
                    "控制台总览": "console-dashboard",
                    "技术支持": "tech-support-overview",
                },
            },
            {
                "dir": "04、购买 RakSmart 产品",
                "file": "购买 RakSmart 产品.md",
                "slug": "buy-products",
                "weight": 40,
                "docs": {
                    "了解 RakSmart 产品购买方式": "purchase-methods",
                    "购买 RakSmart 产品": "purchase",
                },
            },
            {
                "dir": "05、管理已购买的产品",
                "file": "管理已购买的产品.md",
                "slug": "manage-products",
                "weight": 50,
                "docs": {
                    "产品管理": "product-management",
                    "升降级": "upgrade-downgrade",
                    "产品取消和退订": "cancellation",
                },
            },
            {
                "dir": "06、钱包管理",
                "file": "钱包管理.md",
                "slug": "wallet",
                "weight": 60,
                "docs": {
                    "账户余额管理": "balance",
                    "代金券管理": "vouchers",
                    "优惠券管理": "coupons",
                },
            },
            {
                "dir": "07、账户管理",
                "file": "账户管理.md",
                "slug": "account",
                "weight": 70,
                "docs": {
                    "查看账户余额": "view-balance",
                    "查看账户资料": "profile",
                    "用户身份与权限": "user-roles",
                    "为普通用户授权": "user-permissions",
                    "配置联系人和邮件通知": "contacts",
                    "配置付款方式": "payment-methods",
                    "账号安全设置": "security",
                    "其他设置": "other-settings",
                },
            },
            {
                "dir": "08、账单管理",
                "file": "账单管理.md",
                "slug": "billing",
                "weight": 80,
                "docs": {
                    "操作入口": "billing-entry",
                    "账单管理": "billing-management",
                },
            },
            {
                "dir": "09、技术支持",
                "file": "技术支持.md",
                "slug": "technical-support",
                "weight": 90,
                "docs": {
                    "公告信息": "announcements",
                    "文档中心": "documentation-center",
                    "我的工单": "my-tickets",
                    "服务面板密码重置": "panel-password-reset",
                    "设置 SSH 公钥": "ssh-keys",
                    "查看投诉封停": "abuse-list",
                    "联系我们": "contact-us",
                },
            },
        ],
    },
}


# 跨书 / 跨章节的文件名式相对链接修复表。这批链接不是纯锚点（不以 # 开头），现有
# rewrite_links() 的锚点改写逻辑处理不了，会原样保留、构建时被 ignoreDeadLinks
# 兜底跳过（不报错但点不到目标页）。这里显式列出四本新书 + 已发布 VPS 书素材里
# 全部这类残留链接（已用 grep 全量核实，不是猜测），统一改写成正确的 VitePress
# 绝对路径。key 是 unquote() 之后的原始链接文本（无论源文件里写的是 %20 编码还是
# 直接的中文空格，unquote 后都归一化成同一个 key）。
#
# 部分链接（如"购买 RakSmart 产品.md"整篇引用）没有严格对应的单一目标页，参考
# rs-docs-v2/scripts/import_material_books.py 里 GUIDE_LOCAL_FILE_LINKS /
# GUIDE_LOCAL_SECTION_LINKS 已经做过的取舍（引用整篇 -> 章节首页或代表性文章，
# 引用具体小节 -> 对应文章 + 锚点）。这批链接在 rs-docs-v2（Hugo 版）里其实也
# 从未修复过、目前仍是线上死链，本轮借这次转换一并修掉。
LINK_FIXES: dict[str, str] = {
    "购买 RakSmart 产品.md": "/beginners-guide/buy-products/purchase.md",
    "购买 RakSmart 产品.md#了解 RakSmart 产品购买方式": "/beginners-guide/buy-products/purchase-methods.md",
    "购买 RakSmart 产品.md#官网优惠活动入口": "/beginners-guide/buy-products/purchase-methods.md#官网优惠活动入口",
    "购买 RakSmart 产品.md#官网推荐产品入口": "/beginners-guide/buy-products/purchase-methods.md#官网推荐产品入口",
    "购买 RakSmart 产品.md#控制台购买中心入口": "/beginners-guide/buy-products/purchase-methods.md#控制台购买中心入口",
    "购买 RakSmart 产品.md#购买 RakSmart 产品": "/beginners-guide/buy-products/purchase.md",
    "注册 RakSmart 账号.md": "/beginners-guide/register-account/index.md",
    "钱包管理.md": "/beginners-guide/wallet/index.md",
    "钱包管理.md#为 RakSmart 账号充值": "/beginners-guide/wallet/balance.md#为-raksmart-账号充值",
    "管理已购买的产品.md#产品管理": "/beginners-guide/manage-products/product-management.md",
    "管理已购买的产品.md#升降级": "/beginners-guide/manage-products/upgrade-downgrade.md",
    "管理已购买的产品.md#产品取消和退订": "/beginners-guide/manage-products/cancellation.md",
    "账户管理.md#账号安全设置": "/beginners-guide/account/security.md",
    "账户管理.md#用户身份与权限": "/beginners-guide/account/user-roles.md",
    # 源素材里这条链接本身格式有误（多写了一层路径前缀和多余的 ##），照原样匹配后改写
    "新手指南/07、账户管理/账户管理.md#账户管理##为普通用户授权": "/beginners-guide/account/user-permissions.md",
    "账单管理.md": "/beginners-guide/billing/index.md",
    "技术支持.md": "/beginners-guide/technical-support/index.md",
    "独服/01、产品介绍/产品介绍.md": "/dedicatedserver/product-intro/overview.md",
    "裸机云/01、产品介绍/产品介绍.md": "/baremetal/product-intro/overview.md",
    "VPS/01、产品介绍/产品介绍.md": "/vps/product-intro/overview.md",
    "独服/02、快速入门/快速入门.md#登录物理服务器": "/dedicatedserver/quickstart/login.md",
}

# [text](#anchor)]？ 形式的站内锚点链接；末尾可选的 "]" 是素材里的既有笔误，一并吃掉
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)(\])?")


def strip_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return text
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def split_format_c(text: str):
    """按 H1/H2 拆分：返回 (h1_title, intro_lines, [(h2_title, h2_lines), ...])"""
    lines = text.split("\n")
    h1_title = None
    intro_lines: list[str] = []
    docs: list[tuple[str, list[str]]] = []
    current_title = None
    current_lines: list[str] = []
    state = "before_h1"

    for line in lines:
        if h1_title is None and line.startswith("# "):
            h1_title = line[2:].strip()
            state = "intro"
            continue
        if line.startswith("## "):
            if current_title is not None:
                docs.append((current_title, current_lines))
            current_title = line[3:].strip()
            current_lines = []
            state = "doc"
            continue
        if state == "intro":
            intro_lines.append(line)
        elif state == "doc":
            current_lines.append(line)

    if current_title is not None:
        docs.append((current_title, current_lines))

    return h1_title, intro_lines, docs


def build_global_doc_map(book: dict) -> dict:
    """中文 H2 标题 -> (chapter_slug, doc_slug)，覆盖全书所有章节，用于跨章节链接重写"""
    mapping = {}
    for chapter in book["chapters"]:
        for zh_title, doc_slug in chapter["docs"].items():
            mapping[zh_title.strip()] = (chapter["slug"], doc_slug)
    return mapping


def rewrite_links(body: str, doc_map: dict, current_chapter_slug: str) -> str:
    def replace(m: re.Match) -> str:
        text, url, stray_bracket = m.group(1), m.group(2), m.group(3)
        if url.startswith("#"):
            fragment = unquote(url[1:]).strip()
            target = doc_map.get(fragment)
            if target is None:
                return m.group(0)
            target_chapter_slug, target_doc_slug = target
            if target_chapter_slug == current_chapter_slug:
                new_url = f"./{target_doc_slug}.md"
            else:
                new_url = f"../{target_chapter_slug}/{target_doc_slug}.md"
            return f"[{text}]({new_url})"
        # 非纯锚点链接（跨书/跨章节的文件名式相对链接）：查已知修复表
        fixed = LINK_FIXES.get(unquote(url).strip())
        if fixed is not None:
            return f"[{text}]({fixed})"
        return m.group(0)

    return LINK_RE.sub(replace, body)


def write_sidebar_json(book_slug: str, groups: list[dict]) -> None:
    SIDEBAR_DIR.mkdir(parents=True, exist_ok=True)
    (SIDEBAR_DIR / f"{book_slug}.json").write_text(
        json.dumps(groups, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def convert_book(book_key: str) -> None:
    book = BOOKS[book_key]
    book_slug = book["slug"]
    doc_map = build_global_doc_map(book)

    src_book_dir = MATERIALS_DIR / book["material_dir"]
    dst_book_dir = DOCS_DIR / book_slug

    unresolved_links: list[str] = []
    sidebar_groups: list[dict] = []

    for chapter in book["chapters"]:
        src_chapter_dir = src_book_dir / chapter["dir"]
        src_file = src_chapter_dir / chapter["file"]
        dst_chapter_dir = dst_book_dir / chapter["slug"]
        dst_chapter_dir.mkdir(parents=True, exist_ok=True)

        raw = src_file.read_text(encoding="utf-8")
        body = strip_front_matter(raw)
        h1_title, intro_lines, docs = split_format_c(body)

        expected_titles = set(chapter["docs"].keys())
        actual_titles = {t for t, _ in docs}
        missing = expected_titles - actual_titles
        extra = actual_titles - expected_titles
        if missing or extra:
            raise ValueError(
                f"{src_file} 里的 H2 标题和映射表对不上：缺失 {missing}，多余 {extra}"
            )

        # 章节 index.md：H1 标题 + 简介 + 子文章列表
        intro_text = "\n".join(intro_lines).strip()
        index_lines = [
            "---",
            f"title: {h1_title}",
            "---",
            "",
            f"# {h1_title}",
            "",
        ]
        if intro_text:
            index_lines += [intro_text, ""]
        index_lines.append("## 本章内容")
        index_lines.append("")
        for zh_title, doc_slug in chapter["docs"].items():
            index_lines.append(f"- [{zh_title}](./{doc_slug}.md)")
        (dst_chapter_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

        # 每个 H2 -> 独立 .md 页面
        for zh_title, doc_lines in docs:
            doc_slug = chapter["docs"][zh_title]
            doc_body = "\n".join(doc_lines).strip("\n")
            doc_body = rewrite_links(doc_body, doc_map, chapter["slug"])
            for m in LINK_RE.finditer(doc_body):
                if m.group(2).startswith("#") and unquote(m.group(2)[1:]).strip() not in doc_map:
                    unresolved_links.append(
                        f"{chapter['slug']}/{doc_slug}.md: 未解析的站内锚点链接 {m.group(0)!r}"
                    )
            out = f"---\ntitle: {zh_title}\n---\n\n{doc_body}\n"
            (dst_chapter_dir / f"{doc_slug}.md").write_text(out, encoding="utf-8")

        # 图片整份复制（相对路径 ./images/xxx.png 保持不变，不需要重写）
        src_images = src_chapter_dir / "images"
        if src_images.is_dir():
            dst_images = dst_chapter_dir / "images"
            if dst_images.exists():
                shutil.rmtree(dst_images)
            shutil.copytree(src_images, dst_images)

        sidebar_groups.append(
            {
                "text": h1_title,
                "items": [
                    {"text": zh_title, "link": f"/{book_slug}/{chapter['slug']}/{doc_slug}"}
                    for zh_title, doc_slug in chapter["docs"].items()
                ],
            }
        )

    write_sidebar_json(book_slug, sidebar_groups)

    if unresolved_links:
        print("以下链接指向本轮转换范围之外的内容（跨书链接等），保留原样，未重写：", file=sys.stderr)
        for line in unresolved_links:
            print(f"  - {line}", file=sys.stderr)


# ---------------------------------------------------------------------------
# OPS 知识库(中文)："分类目录多文件"变体
# ---------------------------------------------------------------------------

OPS_KB_BOOK_SLUG = "ops-knowledge-base"
OPS_KB_TITLE = "OPS 知识库"
OPS_KB_MATERIAL_DIR = "OPS知识库(中文)"

# 照搬 rs-docs-v2/scripts/import_material_books.py 第 330-474 行，数据不做改动
OPS_KB_CATEGORIES: list[dict] = [
    {"dir": "网络", "slug": "network", "weight": 10, "docs": {
        "服务器无法ping通如何处理.md": "server-not-responding-to-ping",
        "MTR工具安装及使用.md": "mtr-installation-and-usage",
    }},
    {"dir": "SSL", "slug": "ssl", "weight": 20, "docs": {
        "SSL 证书 FAQ.md": "ssl-certificate-faq",
        "SSL证书验证方式指南.md": "ssl-certificate-verification-guide",
        "企业邮箱 FAQ.md": "enterprise-email-faq",
    }},
    {"dir": "云原生", "slug": "cloud-native", "weight": 30, "docs": {
        "云原生负载均衡.md": "load-balancer",
        "云原生安全组设置.md": "security-group-setup",
        "云原生备份使用操作.md": "backup-guide",
    }, "subcategories": [
        {"dir": "Cloud DB MySQL Plus", "slug": "cloud-db-mysql-plus", "weight": 10, "docs": {
            "数据库连接1.md": "database-connection-1",
            "数据库连接2.md": "database-connection-2",
            "无法连接数据库.md": "cannot-connect-database",
        }},
    ]},
    {"dir": "销售问题", "slug": "sales-issues", "weight": 40, "docs": {
        "域名注册信息要求.md": "domain-registration-requirements",
        "用户注册与登录.md": "user-registration-and-login",
        "如何注册账号.md": "how-to-register-account",
        "如何下单.md": "how-to-place-order",
        "如何购买裸机云.md": "how-to-purchase-baremetal",
    }},
    {"dir": "操作系统", "slug": "operating-system", "weight": 50, "docs": {}, "subcategories": [
        {"dir": "linux", "slug": "linux", "weight": 10, "docs": {
            "CentOS 7.X系统重置密码.md": "centos-7-reset-password",
            "Linux系统-etc-fstab 配置错误导致无法登录.md": "fstab-misconfiguration-login-failure",
            "CentOS7.x防火墙开-关和添加端口.md": "centos-7-firewall-and-ports",
            "CentOS 6 - 7修改语言及时区.md": "centos-6-7-change-language-timezone",
            "CentOS 8 EOL如何切换源.md": "centos-8-eol-switch-mirror",
            "linux系统yum报错没有足够的缓存安装.md": "yum-insufficient-cache-error",
            "Centos8 无法使用Yum及Dnf.md": "centos-8-yum-dnf-not-working",
            "Ubuntu18.04-22.04防火墙开-关和修改远程端口.md": "ubuntu-firewall-and-remote-port",
            "linux系统硬盘的挂载与扩容.md": "disk-mount-and-expand",
            "如何使用Putty工具远程linux系统.md": "remote-login-with-putty",
            "Centos7.x系统修改网卡名称.md": "centos-7-rename-network-interface",
            "Linux系统宝塔面板安装教程.md": "install-baota-panel",
            "Linux系统如何使用atop监控工具.md": "how-to-use-atop",
            "linux系统如何传输数据.md": "how-to-transfer-data",
            "SSH登录Linux时提示“Permission denied, please try again”错误如何处理.md": "ssh-permission-denied",
            "Linux系统扩容inode可用空间.md": "expand-inode-space",
            "Linux系统如何查看内存使用情况以及清理缓存.md": "check-memory-and-clear-cache",
            "CentOS 7.x系统升级到CentOS 7.9系统.md": "centos-7-upgrade-to-7-9",
            "CentOS系统修改主机名.md": "centos-change-hostname",
            "CentOS 操作系统如何配置多个IP.md": "centos-configure-multiple-ips",
            "Linux系统锐速安装教程.md": "install-serverspeeder",
            "linux系统如何设置开启-禁止ping.md": "enable-disable-ping",
            "ubuntu防火墙开启与关闭.md": "ubuntu-firewall-on-off",
        }},
        {"dir": "windows", "slug": "windows", "weight": 20, "docs": {
            "Windows系统安装使用宝塔面板.md": "install-baota-panel",
            "Windows系统磁盘空间的压缩-扩展.md": "shrink-extend-disk-space",
            "Windows 2012系统卸载某些软件后无法进入系统桌面怎么办.md": "windows-2012-desktop-not-loading-after-uninstall",
            "windows系统如何更改语言.md": "change-system-language",
            "Windows修改管理员密码.md": "change-administrator-password",
            "Windows 服务器一键部署幻兽帕鲁.md": "deploy-palworld-one-click",
            "Windows远程桌面出现CredSSP加密数据修正问题解决方案.md": "rdp-credssp-encryption-fix",
            "Windows关闭系统自动更新.md": "disable-automatic-updates",
            "Windows系统如何添加IP.md": "add-ip-address",
            "Windows系统使用IE浏览器打开网站提示“增强安全配置正在阻止来自下列网站内容”如何处理.md": "ie-enhanced-security-blocking-content",
            "windows远程连接提示“发生身份验证错误要求的安全包不存在” 解决方法.md": "rdp-authentication-error-security-package",
            "windows系统如何远程登录.md": "remote-desktop-login",
            "Windows修改远程端口号.md": "change-remote-desktop-port",
            "Windows系统无法启用远程协助.md": "remote-assistance-not-working",
            "Windows系统如何设置图标快捷方式.md": "create-desktop-shortcut",
            "通过远程桌面连接Windows实例提示“要远程登录，你需要具有通过远程桌面服务进行登录的权限。”信息如何解决.md": "rdp-permission-required-error",
            "Windows系统如何创建分区.md": "create-disk-partition",
            "Windows系统设置禁Ping.md": "disable-ping",
        }},
    ]},
    {"dir": "账单问题", "slug": "billing-issues", "weight": 60, "docs": {
        "财务管理 - 我的账单.md": "my-bills",
        "充值-支持虚拟货币转账.md": "recharge-via-crypto-transfer",
    }},
    {"dir": "VPS", "slug": "vps", "weight": 70, "docs": {
        "VPS 独立云盘使用指南.md": "cloud-disk-guide",
        "VPS 弹性 IP 使用指南.md": "elastic-ip-guide",
        "如何生成SSH密钥对.md": "generate-ssh-key-pair",
        "SSH 公钥管理指南.md": "ssh-key-management-guide",
        "VPS 安全组使用指南.md": "security-group-guide",
        "VPS 控制台操作指南.md": "console-guide",
        "VPS 监控功能说明.md": "monitoring-guide",
        "如何使用私钥进行远程登录.md": "remote-login-with-private-key",
        "VPS（小时计费）产品购买及注意事项.md": "hourly-billing-purchase-notes",
    }},
    {"dir": "托管云", "slug": "managed-cloud", "weight": 80, "docs": {
        "如何进行服务器托管.md": "how-to-host-server",
    }},
    {"dir": "账户和安全", "slug": "account-security", "weight": 90, "docs": {
        "启用登陆Raksmart动态验证.md": "enable-login-2fa",
    }},
    {"dir": "售前支持", "slug": "presales-support", "weight": 100, "docs": {
        "安全中心 - 安全设置.md": "security-settings",
        "我的钱包 - 代金券.md": "wallet-vouchers",
        "账户管理 - 付款方式.md": "payment-methods",
        "安全中心 - 修改密码.md": "change-password",
        "我的钱包 - 账户余额.md": "wallet-balance",
        "账户管理 - 我的资料.md": "my-profile",
        "如何查找已购买的产品.md": "find-purchased-products",
        "登录日志.md": "login-logs",
        "账户管理 - 用户管理.md": "user-management",
        "投诉封停使用指南.md": "complaint-suspension-guide",
        "我的钱包 - 优惠券.md": "wallet-coupons",
        "技术支持 - 我的工单.md": "my-tickets",
        "账户管理 - 联系人.md": "contacts",
    }},
    {"dir": "共享主机", "slug": "shared-hosting", "weight": 110, "docs": {
        "如何购买共享主机.md": "how-to-purchase",
    }},
    {"dir": "域名", "slug": "domain", "weight": 120, "docs": {
        "SSL购买认证指南.md": "ssl-purchase-verification-guide",
        "DNS 解析管理.md": "dns-management",
        "域名相关问题解答.md": "domain-faq",
    }},
    {"dir": "独服", "slug": "dedicated-server", "weight": 130, "docs": {
        "物理服务器BCM重置.md": "bmc-reset",
        "物理服务器BIOS说明介绍.md": "bios-overview",
        "物理服务器打开VNC窗口.md": "open-vnc-window",
        "物理服务器控制面板.md": "control-panel",
        "物理服务器控制面板管理介绍.md": "control-panel-management-overview",
        "物理服务器救援模式操作.md": "rescue-mode-operations",
        "物理服务器无法正常启动，检测是否为无法识别到硬盘.md": "boot-failure-disk-not-detected",
        "物理服务器格式化硬盘操作.md": "format-disk",
        "物理服务器检查磁盘健康状态.md": "check-disk-health",
        "物理服务器流量统计.md": "traffic-statistics",
        "物理服务器网络监控.md": "network-monitoring",
        "物理服务器进入救援模式无响应故障描述.md": "rescue-mode-no-response-issue",
        "物理服务机器破解密码.md": "password-recovery",
        "物理服务机器重装系统.md": "reinstall-os",
    }},
    {"dir": "裸机云", "slug": "baremetal", "weight": 140, "docs": {
        "裸机云 Rescue（救援系统）使用指南.md": "rescue-mode-guide",
        "裸机云 VNC 控制台使用指南.md": "vnc-console-guide",
        "裸机云升级-降级操作指南.md": "upgrade-downgrade-guide",
        "裸机云密码修改与重置指南.md": "password-change-reset-guide",
        "裸机云控制台操作指南.md": "console-guide",
        "裸机云监控功能说明.md": "monitoring-guide",
        "裸机云重装系统指南.md": "reinstall-os-guide",
    }},
]

_OPS_KB_H1_RE = re.compile(r"^#(?!#)\s+")


def extract_ops_kb_title_and_body(text: str) -> tuple[str, list[str]]:
    lines = text.replace("\xa0", " ").splitlines()
    title = ""
    body_lines: list[str] = []
    found_title = False
    for line in lines:
        stripped = line.rstrip()
        if not found_title and _OPS_KB_H1_RE.match(stripped):
            title = _OPS_KB_H1_RE.sub("", stripped).strip()
            found_title = True
            continue
        body_lines.append(stripped)
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    return title, body_lines


def validate_ops_kb_body(lines: list[str], doc_path: Path) -> None:
    """正文（已去掉首行文章标题）里不应再出现单个 # 标题或孤立的 # 符号行——
    这批素材约定：文章标题用一个 #，章内小节一律用 ## 及以上。不规范格式直接
    报错并指出文件，要求先在源 markdown 里改规范，而不是靠脚本猜测转换。"""
    for line in lines:
        stripped_line = line.strip()
        if re.fullmatch(r"#+", stripped_line):
            raise ValueError(f"{doc_path}: 存在孤立的 # 符号行，请在源 markdown 里删除")
        if _OPS_KB_H1_RE.match(line):
            raise ValueError(
                f"{doc_path}: 正文里出现单 # 标题 {stripped_line!r}，"
                "请在源 markdown 里改为 ## 及以上层级"
            )


def convert_ops_kb_node(*, src_dir: Path, dst_dir: Path, node: dict):
    """转换一个分类（或子分类）节点，返回 (本分类文章列表, 子分类结果列表) 供上层
    生成 index.md 和 sidebar 用：
    - 本分类文章列表: [(文章标题, doc_slug), ...]
    - 子分类结果列表: [(子分类节点 dict, 该子分类的完整返回值), ...]（递归结构）
    """
    dst_dir.mkdir(parents=True, exist_ok=True)
    src_images = src_dir / "images"

    doc_entries: list[tuple[str, str]] = []
    for filename, doc_slug in node.get("docs", {}).items():
        doc_path = src_dir / filename
        raw = strip_front_matter(doc_path.read_text(encoding="utf-8"))
        title, body_lines = extract_ops_kb_title_and_body(raw)
        validate_ops_kb_body(body_lines, doc_path)
        body = "\n".join(body_lines).strip("\n")
        out = f"---\ntitle: {title}\n---\n\n{body}\n"
        (dst_dir / f"{doc_slug}.md").write_text(out, encoding="utf-8")
        doc_entries.append((title, doc_slug))

    if src_images.is_dir():
        dst_images = dst_dir / "images"
        if dst_images.exists():
            shutil.rmtree(dst_images)
        shutil.copytree(src_images, dst_images)

    sub_results: list[tuple[str, list[tuple[str, str]]]] = []
    for sub in node.get("subcategories", []):
        sub_docs = convert_ops_kb_node(src_dir=src_dir / sub["dir"], dst_dir=dst_dir / sub["slug"], node=sub)
        sub_results.append((sub, sub_docs))

    index_lines = ["---", f"title: {node['dir']}", "---", "", f"# {node['dir']}", ""]
    if doc_entries:
        index_lines.append("## 本分类内容")
        index_lines += [f"- [{t}](./{s}.md)" for t, s in doc_entries]
        index_lines.append("")
    if sub_results:
        index_lines.append("## 子分类")
        index_lines += [f"- [{sub['dir']}](./{sub['slug']}/index.md)" for sub, _ in sub_results]
    (dst_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    return doc_entries, sub_results


def build_ops_kb_sidebar_item(node: dict, doc_entries: list[tuple[str, str]], sub_results, path_prefix: str) -> dict:
    items = [
        {"text": title, "link": f"{path_prefix}/{node['slug']}/{doc_slug}"}
        for title, doc_slug in doc_entries
    ]
    for sub, sub_docs_and_subs in sub_results:
        sub_doc_entries, sub_sub_results = sub_docs_and_subs
        items.append(
            build_ops_kb_sidebar_item(
                sub, sub_doc_entries, sub_sub_results, f"{path_prefix}/{node['slug']}"
            )
        )
    return {"text": node["dir"], "collapsed": True, "items": items}


def convert_ops_kb() -> None:
    src_root = MATERIALS_DIR / OPS_KB_MATERIAL_DIR
    dst_root = DOCS_DIR / OPS_KB_BOOK_SLUG

    sidebar_groups = []
    for category in OPS_KB_CATEGORIES:
        doc_entries, sub_results = convert_ops_kb_node(
            src_dir=src_root / category["dir"],
            dst_dir=dst_root / category["slug"],
            node=category,
        )
        sidebar_groups.append(
            build_ops_kb_sidebar_item(category, doc_entries, sub_results, f"/{OPS_KB_BOOK_SLUG}")
        )
    write_sidebar_json(OPS_KB_BOOK_SLUG, sidebar_groups)

    index_lines = ["---", f"title: {OPS_KB_TITLE}", "---", "", f"# {OPS_KB_TITLE}", "", "## 分类"]
    index_lines += [f"- [{c['dir']}](./{c['slug']}/index.md)" for c in OPS_KB_CATEGORIES]
    (dst_root / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    convert_book("vps")
    convert_book("dedicatedserver")
    convert_book("baremetal")
    convert_book("beginners-guide")
    convert_ops_kb()
    print("VPS / 独服 / 裸机云 / 新手指南 / OPS 知识库(中文) 转换完成")
