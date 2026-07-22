# 快速开始

## 安装 Docsify

Docsify 的安装非常简单，你只需要创建一个 `index.html` 文件并引入 Docsify 的 JavaScript 即可。

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>My Docs</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
</body>
</html>
```

## 初始化项目

### 方法一：手动创建

1. 创建一个项目目录
2. 新建 `index.html` 文件，写入上面的代码
3. 创建 `README.md` 文件作为首页内容
4. 启动本地服务器预览

### 方法二：使用 CLI 工具

```bash
npm i docsify-cli -g
docsify init ./docs
```

## 本地预览

使用 docsify-cli 启动开发服务器：

```bash
docsify serve ./docs
```

然后访问 `http://localhost:3000` 即可看到你的文档站点。

## 添加更多页面

### 创建新文件

在项目目录下创建新的 Markdown 文件，例如 `guide.md`，然后在侧边栏配置中添加链接即可。

### 页面间导航

在 Markdown 中，你可以使用相对链接在不同页面间切换：

```markdown
[前往功能特性页](features.md)
```

渲染后会变成：[前往功能特性页](features.md)

---

## 下一步

- 了解更多高级功能，请查看 [功能特性](features.md)
- 返回 [首页](/)

