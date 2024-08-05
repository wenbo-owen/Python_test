import weather
import openpyxl

html = weather.get_html()  # 发请求，得响应结果
lst = weather.parse_html(html)

# 创建一个新的Excel 工作簿
workbook = openpyxl.Workbook()  # 创建对象
# 在Excel文件中创建工作表
sheet  = workbook.create_sheet('景区天气')
#向工作表中添加数据
for item in lst:
    sheet.append(item)  #一次添加一行

workbook.save('weather.xlsx')