import excel2img
import pandas as pd

# 读取CSV文件
def csv2excel(csv_file):
    data = pd.read_csv(csv_file, header=None)
    excel_file = csv_file.split('.')[0] + '.xlsx'  # 替换为你希望保存的Excel文件名
    data.to_excel(excel_file, index=False, header=False)
    print(f'已成功将{csv_file}转换为{excel_file}')
    return excel_file
 
def out_img(excel_file, sheet_list):
    try:
        print("开始截图，请耐心等待。。。")
        for i in range(len(sheet_list)):
            # sheet_list[i] + ".png" 为保存的图片名称（以sheet名称.png命名）
            excel2img.export_img(excel_file, sheet_list[i] + ".png", sheet_list[i], None)
    except Exception as e:
        print("截图失败！", e)
 
 
if __name__ == '__main__':
    file = r'C:\Users\Administrator\Desktop\1.csv'
    sheet_list = ['Sheet1']
    # 如果file是以csv结尾，将csv文件转换成Excel文件
    if file.endswith('.csv'):
        file = csv2excel(file)
    out_img(file, sheet_list)