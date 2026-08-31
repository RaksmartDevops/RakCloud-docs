#!/usr/bin/env python3
"""将 materials/<书名>/ 下的 Format C 素材转换成 docs/<slug>/ 下的 VitePress 页面。

本轮只处理 VPS 一本书（试点），BOOKS 字典里 slug 映射直接复用自
rs-docs-v2/scripts/import_material_books.py 里已经人工确认过的 BOOKS["vps"]。
后续处理其余书时，把对应书的映射表加进 BOOKS 字典、在 main() 里加一行调用即可复用本脚本。

设计上和 Hugo 那边的转换脚本（import_material_books.py）不同：
- 正文（表格/加粗/斜体/引用块/代码围栏）直接透传保留原始 Markdown 语法，不重新拼 HTML
- H3/H4 页内锚点不用手写 slugify，VitePress/markdown-it 自动生成
- 图片相对路径（./images/xxx.png）不需要重写，只需要把 images/ 目录整份复制过去
"""

import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote

MATERIALS_DIR = Path(__file__).resolve().parent.parent / "materials"
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

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
        if not url.startswith("#"):
            # 非纯锚点链接（外部链接、跨书 .md 链接）本轮不处理，原样保留
            return m.group(0)
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

    return LINK_RE.sub(replace, body)


def convert_book(book_key: str) -> None:
    book = BOOKS[book_key]
    book_slug = book["slug"]
    doc_map = build_global_doc_map(book)

    src_book_dir = MATERIALS_DIR / book["material_dir"]
    dst_book_dir = DOCS_DIR / book_slug

    unresolved_links: list[str] = []

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

    if unresolved_links:
        print("以下链接指向本轮转换范围之外的内容（跨书链接等），保留原样，未重写：", file=sys.stderr)
        for line in unresolved_links:
            print(f"  - {line}", file=sys.stderr)


if __name__ == "__main__":
    convert_book("vps")
    print("VPS 手册转换完成 -> docs/vps/")
