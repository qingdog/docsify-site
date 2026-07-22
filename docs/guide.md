# 技术指南

本页面介绍核心技术概念与基础用法。

## 快速开始

只需三个步骤即可上手：

1. 创建 `index.html` 入口文件
2. 编写 Markdown 文档
3. 启动本地服务器预览

## 核心配置

Docsify 通过 `window.$docsify` 对象进行配置：

```javascript
window.$docsify = {
  name: 'My Docs',
  loadSidebar: true,
  subMaxLevel: 3
}
```

## 页面切换

你可以随时跳转到其他页面：

- [返回首页](/)
- [高级进阶](/advanced)

> 提示：侧边栏也提供了导航功能，点击即可切换页面。
