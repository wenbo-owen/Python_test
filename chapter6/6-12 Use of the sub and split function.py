'''
re.sub(pattern,rep|string,count,flags=0)
'''

import re

pattern = '黑客|破解|反爬'
s = '我想学习python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
match = re.sub(pattern,'xxx',s)
print(match)


pattern = '[?|&]'
s2 = 'https://www.bilibili.com/video?BV1wD4y1o7AS?p=72&spm_id_from'
lst = re.split(pattern,s2)
print(lst)

print('-'*50)

pattern = r'13[4-9]\d{8}'  # 前两位13，第2位4-9之间的数, 后面是8位十进制的数  这个r 好像加不加都可以的
lst=['13809876543','15109876543','13278965439','15912345665','13198765432']

for item in lst:
    match = re.match(pattern,item)
    if match is not None:
        print(match.group())
    else:
        print(None)

print('-'*50)
pattern  = r'wrs_\w+'
s = 'wrs_python wrs_home'
match = re.search(pattern,s)
print(match.group())

lst = re.findall(pattern,s)
print(lst)

print('-'*50)

pattern = r'\s*@'                #r 原始字符串
s = ' @温博 @王倩 @温如水'         # \s 表示匹配任何空白字符   * 表示匹配前面的字符（这里是 \s）零次或多次
lst = re.split(pattern,s)
print(lst)