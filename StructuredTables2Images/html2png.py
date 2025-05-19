import imgkit

# HTML代码
html_content = '''
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>表格示例</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h2>示例表格</h2>
<table>
    <thead>
        <tr>
            <th>姓名</th>
            <th>年龄</th>
            <th>城市</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>25</td>
            <td>北京</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>30</td>
            <td>上海</td>
        </tr>
        <tr>
            <td>王五</td>
            <td>28</td>
            <td>广州</td>
        </tr>
    </tbody>
</table>

</body>
</html>
'''

# 将HTML保存为文件
with open('table.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
options = {
    'encoding': "UTF-8",  # 确保使用 UTF-8 编码
}

config = imgkit.config(wkhtmltoimage=r'D:\wkhtmltox\wkhtmltopdf\bin\wkhtmltoimage.exe')

# 将HTML文件转换为图片
imgkit.from_file('0.html', '0.png', config=config, options=options)

print('表格已成功转换为图片。')