// 把已构建好的 VitePress 站点（docs/.vitepress/dist/）按 sidebar 顺序
// 拼成整书 PDF。只处理"产品手册"类的 4 本书，OPS 知识库（126 篇散文章）不做整书导出。
//
// 前置条件：先跑过 `npm run docs:build`，dist/ 目录必须存在。
// 用法：node scripts/export-pdf.mjs

import { createServer } from "node:http";
import { readFile, mkdir, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import puppeteer from "puppeteer";

const ROOT_DIR = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST_DIR = path.join(ROOT_DIR, "docs/.vitepress/dist");
const SIDEBAR_DIR = path.join(ROOT_DIR, "docs/.vitepress/sidebar");
const BASE = "/rakcloud-docs";
const PORT = 4173;

const BOOKS = [
  { slug: "vps", title: "VPS 用户手册" },
  { slug: "dedicatedserver", title: "独立服务器用户手册" },
  { slug: "baremetal", title: "裸机云用户手册" },
  { slug: "beginners-guide", title: "新手指南" },
];

const MIME_TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css",
  ".js": "text/javascript",
  ".json": "application/json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".woff2": "font/woff2",
  ".woff": "font/woff",
  ".ico": "image/x-icon",
};

function startStaticServer() {
  const server = createServer(async (req, res) => {
    let urlPath = decodeURIComponent(req.url.split("?")[0]);
    if (!urlPath.startsWith(BASE)) {
      res.writeHead(404);
      res.end();
      return;
    }
    let relPath = urlPath.slice(BASE.length);
    if (relPath === "" || relPath === "/") relPath = "/index.html";
    let filePath = path.join(DIST_DIR, relPath);
    if (existsSync(filePath) && (await stat(filePath)).isDirectory()) {
      filePath = path.join(filePath, "index.html");
    }
    if (!existsSync(filePath) && !path.extname(filePath)) {
      filePath = `${filePath}.html`;
    }
    try {
      const data = await readFile(filePath);
      const ext = path.extname(filePath);
      res.writeHead(200, { "Content-Type": MIME_TYPES[ext] || "application/octet-stream" });
      res.end(data);
    } catch {
      res.writeHead(404);
      res.end();
    }
  });
  return new Promise((resolve) => {
    server.listen(PORT, () => resolve(server));
  });
}

async function loadSidebar(bookSlug) {
  const raw = await readFile(path.join(SIDEBAR_DIR, `${bookSlug}.json`), "utf-8");
  return JSON.parse(raw);
}

async function buildBookPdf(browser, book, headHtml) {
  const groups = await loadSidebar(book.slug);
  const page = await browser.newPage();

  const sections = [];
  for (const group of groups) {
    const groupSections = [];
    for (const item of group.items) {
      const url = `http://localhost:${PORT}${BASE}${item.link}`;
      await page.goto(url, { waitUntil: "networkidle0" });
      await page.waitForSelector(".vp-doc", { timeout: 15000 });
      const contentHtml = await page.evaluate(() => document.querySelector(".vp-doc").innerHTML);
      groupSections.push(`
        <section class="pdf-doc">
          <h1>${item.text}</h1>
          ${contentHtml}
        </section>
      `);
    }
    sections.push(`
      <section class="pdf-chapter">
        <h2>${group.text}</h2>
      </section>
      ${groupSections.join("\n")}
    `);
  }

  const today = new Date().toISOString().slice(0, 10);
  const combinedHtml = `
    <!doctype html>
    <html lang="zh-CN">
      <head>
        <meta charset="utf-8">
        ${headHtml}
        <style>
          body { max-width: 800px; margin: 0 auto; padding: 0 32px; }
          .pdf-cover { height: 90vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
          .pdf-cover h1 { font-size: 40px; margin-bottom: 16px; }
          .pdf-chapter { page-break-before: always; display: flex; align-items: center; min-height: 30vh; }
          .pdf-chapter h2 { font-size: 28px; border-left: 6px solid #ff8f32; padding-left: 16px; }
          .pdf-doc { page-break-before: always; }
          .pdf-doc h1 { font-size: 22px; border-bottom: 1px solid #e2e2e2; padding-bottom: 8px; }
          img { max-width: 100%; }
        </style>
      </head>
      <body>
        <section class="pdf-cover">
          <h1>${book.title}</h1>
          <p>RakCloud 文档中心 · 生成日期 ${today}</p>
        </section>
        ${sections.join("\n")}
      </body>
    </html>
  `;

  await page.goto(`http://localhost:${PORT}${BASE}/`, { waitUntil: "networkidle0" });
  await page.setContent(combinedHtml, { waitUntil: "domcontentloaded", timeout: 60000 });
  // 图片是拼接进 DOM 后才开始加载的，等它们都 load/error 完再生成 PDF，
  // 避免用 networkidle0 在一整本几十张图的大页面上不稳定超时。
  await page.evaluate(() =>
    Promise.all(
      Array.from(document.images)
        .filter((img) => !img.complete)
        .map((img) => new Promise((resolve) => {
          img.addEventListener("load", resolve, { once: true });
          img.addEventListener("error", resolve, { once: true });
        }))
    )
  );

  const outDir = path.join(DIST_DIR, "pdf");
  await mkdir(outDir, { recursive: true });
  const outPath = path.join(outDir, `${book.slug}.pdf`);
  await page.pdf({
    path: outPath,
    format: "A4",
    printBackground: true,
    margin: { top: "20mm", bottom: "20mm", left: "16mm", right: "16mm" },
  });
  await page.close();
  console.log(`已生成 ${outPath}`);
}

async function main() {
  if (!existsSync(DIST_DIR)) {
    console.error("docs/.vitepress/dist 不存在，请先运行 npm run docs:build");
    process.exit(1);
  }

  const server = await startStaticServer();
  const browser = await puppeteer.launch({ headless: true });

  try {
    const firstPage = await browser.newPage();
    await firstPage.goto(`http://localhost:${PORT}${BASE}/`, { waitUntil: "networkidle0" });
    const headHtml = await firstPage.evaluate(() => {
      const links = [...document.querySelectorAll('link[rel="stylesheet"], link[rel="preload stylesheet"]')];
      return links.map((el) => el.outerHTML).join("\n");
    });
    await firstPage.close();

    for (const book of BOOKS) {
      await buildBookPdf(browser, book, headHtml);
    }
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
