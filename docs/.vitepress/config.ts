import { defineConfig } from 'vitepress'

import vpsSidebar from './sidebar/vps.json'
import dedicatedserverSidebar from './sidebar/dedicatedserver.json'
import baremetalSidebar from './sidebar/baremetal.json'
import beginnersGuideSidebar from './sidebar/beginners-guide.json'
import opsKnowledgeBaseSidebar from './sidebar/ops-knowledge-base.json'

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

  themeConfig: {
    logo: { light: '/logo-new.png', dark: '/logo-new-white.png' },

    nav: [
      { text: '首页', link: '/' },
      { text: 'VPS', link: '/vps/product-intro/overview' },
      { text: '独服', link: '/dedicatedserver/product-intro/overview' },
      { text: '裸机云', link: '/baremetal/product-intro/overview' },
      { text: '新手指南', link: '/beginners-guide/about-raksmart/products-and-services' },
      { text: 'OPS 知识库', link: '/ops-knowledge-base/' },
    ],

    sidebar: {
      '/vps/': vpsSidebar,
      '/dedicatedserver/': dedicatedserverSidebar,
      '/baremetal/': baremetalSidebar,
      '/beginners-guide/': beginnersGuideSidebar,
      '/ops-knowledge-base/': opsKnowledgeBaseSidebar,
    },
  },
})
