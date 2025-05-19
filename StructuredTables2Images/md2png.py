import markdown
import imgkit
import os

# 读取 markdown 文件
with open('table.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

# 将 markdown 转换为 HTML
html_content = markdown.markdown(md_content, extensions=['tables'])

style = """
<style>
    html, body {
        margin: 0;
        padding: 0;
        height: 100%;  /* 设置 html 和 body 的高度 */
    }
    body {
        display: flex;
        justify-content: center;  /* 水平居中 */
        align-items: center;      /* 垂直居中 */
        min-height: 100%;         /* 保证 body 高度至少为 100% */
        overflow: hidden;         /* 禁止溢出内容产生的滚动条 */
    }
    table {
        width: 100%;  /* 表格宽度设置为页面的 80% */
        height: 100%;
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }
</style>
"""

html_with_style = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Table</title>
    {style}
</head>
<body>
{html_content}
</body>
</html>
"""

# 将生成的 HTML 写入文件
with open('output.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_with_style)

options = {
    'encoding': "UTF-8",  # 确保使用 UTF-8 编码
}
config = imgkit.config(wkhtmltoimage=r'D:\wkhtmltox\wkhtmltopdf\bin\wkhtmltoimage.exe')
# 将HTML文件转换为图片
imgkit.from_file('output.html', 'output.png', config=config, options=options)
os.remove('output.html')

print('表格已成功转换为图片。')
