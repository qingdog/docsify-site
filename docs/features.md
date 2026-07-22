# 功能特性

## 侧边栏

Docsify 支持自定义侧边栏。你可以在项目根目录创建 `_sidebar.md` 文件来配置导航菜单。

```markdown
- [首页](/)
- [快速开始](guide.md)
- [功能特性](features.md)
```

启用侧边栏后，你可以在每个页面间快速切换。

## 搜索功能

Docsify 内置全文搜索插件，只需在 `index.html` 中添加以下配置：

```html
<script>
  window.$docsify = {
    search: {
      maxAge: 86400000,
      paths: 'auto',
      placeholder: '搜索...',
      noData: '没有找到结果',
    }
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
```

## 主题切换

Docsify 提供了多种官方主题：

| 主题名称 | CDN 链接 |
|---------|---------|
| Vue     | `themes/vue.css` |
| Buble   | `themes/buble.css` |
| Dark    | `themes/dark.css` |
| Pure    | `themes/pure.css` |

## 代码高亮

支持自动代码高亮，无需额外配置。支持多种编程语言：

```python
def hello():
    print("Hello, Docsify!")
```

```javascript
function hello() {
    console.log("Hello, Docsify!");
}
```

## Emoji 支持

Docsify 支持在 Markdown 中使用 Emoji :smile: :rocket: :tada:

## 表格

| 功能 | 是否支持 | 说明 |
|-----|---------|-----|
| Markdown | ✅ | 原生支持 |
| 搜索 | ✅ | 插件支持 |
| 主题 | ✅ | 多种可选 |
| Emoji | ✅ | 内置支持 |

---

> 想了解更多？返回 [首页](/) 或查看 [快速开始](guide.md)
