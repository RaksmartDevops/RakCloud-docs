import { defineConfig } from 'vitepress'

import vpsSidebar from './sidebar/vps.json'
import dedicatedserverSidebar from './sidebar/dedicatedserver.json'
import baremetalSidebar from './sidebar/baremetal.json'
import beginnersGuideSidebar from './sidebar/beginners-guide.json'
import opsKnowledgeBaseSidebar from './sidebar/ops-knowledge-base.json'

function withPdfDownload(sidebar: any[], pdfPath: string) {
  return [
    {
      text: '资源下载',
      items: [{ text: '⬇ 下载 PDF 手册', link: pdfPath }],
    },
    ...sidebar,
  ]
}

export default defineConfig({
  base: '/rakcloud-docs/',
  lang: 'zh-CN',
  title: 'RakCloud 文档中心',
  description: 'RakCloud 产品文档',

  // 素材里有一批跨书/跨章节的文件名式相对链接（如 "购买%20RakSmart%20产品.md"），
  // 这类链接不是纯锚点，转换脚本的 rewrite_links() 只能靠显式的 LINK_FIXES 表逐条
  // 修复已知案例（见 scripts/convert_material_to_vitepress.py）。已核实并修复了当前
  // 五本书素材里全部这类案例，但不排除未来新增/编辑素材时再引入同类问题，这条规则
  // 作为兜底继续保留，避免个别遗漏直接导致构建失败。
  ignoreDeadLinks: [/%/],

  // 产品手册类的 4 本书支持整书 PDF 下载（scripts/export-pdf.mjs 在构建后生成到
  // dist/pdf/<book-slug>.pdf）。这个入口加在 sidebar 顶部而不是写进某篇 docs/*.md
  // 正文里，是因为 docs/ 是转换脚本生成的产物，手改正文下次跑脚本会被覆盖掉；
  // config.ts 是手工维护的文件，不受脚本重跑影响。
  themeConfig: {
    logo: { light: '/logo-new.png', dark: '/logo-new-white.png' },

    search: {
      provider: 'local',
    },

    nav: [
      { text: '首页', link: '/' },
      { text: 'VPS', link: '/vps/product-intro/overview' },
      { text: '独服', link: '/dedicatedserver/product-intro/overview' },
      { text: '裸机云', link: '/baremetal/product-intro/overview' },
      { text: '新手指南', link: '/beginners-guide/about-raksmart/products-and-services' },
      { text: 'OPS 知识库', link: '/ops-knowledge-base/' },
    ],

    sidebar: {
      '/vps/': withPdfDownload(vpsSidebar, '/pdf/vps.pdf'),
      '/dedicatedserver/': withPdfDownload(dedicatedserverSidebar, '/pdf/dedicatedserver.pdf'),
      '/baremetal/': withPdfDownload(baremetalSidebar, '/pdf/baremetal.pdf'),
      '/beginners-guide/': withPdfDownload(beginnersGuideSidebar, '/pdf/beginners-guide.pdf'),
      '/ops-knowledge-base/': opsKnowledgeBaseSidebar,
    },
  },
})
