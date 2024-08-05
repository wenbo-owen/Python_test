import pdfplumber
import re

#打开PDF文件
with pdfplumber.open('FIFO_FPGA.pdf') as pdf:
    for i in pdf.pages:   #遍历页
        test = i.extract_text()
        print(test)         #extract_text() 提取内容
        print(f'------------第{i.page_number}页结束')

print('-'*50)

print('test的数据类型是',type(test))

pattern = r'[a-zA-Z_]+\b'

match = re.findall(pattern,test,re.I)
print(match)