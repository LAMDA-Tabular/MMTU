import os
from subprocess import run
from PIL import Image
from pdf2image import convert_from_path
import excel2img
import pandas as pd

def latex_to_pdf(latex_table_code, output_pdf):
    """
    将 LaTeX 表格代码字符串封装为完整的 LaTeX 文档，并编译为 PDF。
    """
    # 包装 LaTeX 表格代码为完整的 LaTeX 文档
    full_latex_code = r"""
    \documentclass{standalone}
    \usepackage{booktabs}
    \begin{document}
    """ + latex_table_code + r"""
    \end{document}
    """

    # 将完整的 LaTeX 文档写入文件
    with open("table.tex", "w") as f:
        f.write(full_latex_code)

    # 使用 pdflatex 将 LaTeX 文件编译为 PDF
    run([r"D:\LaTex\miktex\bin\x64\pdflatex.exe", "table.tex"], check=True)

    # 清理辅助文件
    os.remove("table.aux")
    os.remove("table.log")
    
    # 重命名生成的 PDF 文件
    os.rename("table.pdf", output_pdf)


def pdf_to_image(pdf_file, output_image):
    """
    将 PDF 文件转换为图片。
    """
    # img = Image.open(pdf_file)
    # img.save(output_image)
    images = convert_from_path(pdf_file, poppler_path=r"D:\poppler\poppler-24.07.0\Library\bin")
    
    # 保存图片
    for i, image in enumerate(images):
        image.save(f"{output_image[:-4]}_{i+1}.png", "PNG")


# 示例 LaTeX 表格代码字符串，从 \begin{tabular} 开始，到 \end{tabular} 结束
latex_table_code = """
\\begin{tabular}{lllll}\\hline\n& \\multicolumn{4}{c}{\\textbf{Image size $224\\times224$}} \\\\\n \\hline\n\\multicolumn{1}{c}{\\textbf{Types of N treatments}} & Control     & Low       & Medium     & High     \\\\\n \\hline\n\\textbf{Precision}                                 & 0.949       & 0.992     & 0.985      & 0.923    \\\\\n\\textbf{Recall}                                    & 0.936       & 0.992     & 0.98       & 0.941    \\\\\n\\textbf{F1-score}                                  & 0.943       & 0.992     & 0.982      & 0.932    \\\\\n\\textbf{Accuracy}                                  & \\multicolumn{4}{c}{0.962}                       \\\\\n \\hline\n& \\multicolumn{4}{c}{\\textbf{Image size $384\\times384$}} \\\\\n \\hline\n\\textbf{Precision}                                 & 0.973       & 0.991     & 0.982      & 0.917    \\\\\n\\textbf{Recall}                                    & 0.924       & 0.989     & 0.981      & 0.964    \\\\\n\\textbf{F1-score}                                  & 0.948       & 0.99      & 0.982      & 0.94     \\\\\n\\textbf{Accuracy}                                  & \\multicolumn{4}{c}{0.965}                       \\\\\n \\hline\n\\end{tabular}
"""

# 步骤1：将 LaTeX 表格代码字符串封装为完整的 LaTeX 文档并转换为 PDF
latex_to_pdf(latex_table_code, "table.pdf")

# 步骤2：将 PDF 转换为图片
pdf_to_image("table.pdf", "table_image.png")

print("图片已生成：table_image.png")
