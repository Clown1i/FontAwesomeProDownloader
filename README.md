# FontAwesomeProDownloader

著名的字体图标 [Font Awesome](https://fontawesome.com/) Pro版本的下载脚本。

**事实上使用官方CDN也可以用，只是下载下来免得哪一天被屏蔽了就比较麻烦了**

`https://kit-pro.fontawesome.com/releases/v5.14.0/css/pro.min.css`

Pro本身是付费的，请不要用于商业用途，下载仅供个人研究和学习使用。

（不用英语是因为怕被举报2333）

因个人使用不当产生的侵权需要自行承担后果。

# 使用第三方库

aiohttp

# 使用方法

运行脚本，会自动下载css文件以及依赖的字体文件。

会自动生成以下结构，请勿改变结构。

```
css
-- pro.min.css

webfonts
-- 各种字体
```

然后在HTML标签中引入 `css/pro.min.css` 就可以正常使用了，具体用法请去看官方文档。
