'''
re.sub(pattern,rep|string,count,flags=0)
在Python的re模块中，re.sub(pattern, repl, string, count=0, flags=0)函数的含义是：在字符串中查找所有与正则表达式pattern匹配的子串，
并将它们替换为repl指定的字符串。这个替换操作可以指定发生的次数（通过count参数），以及是否使用特定的标志（通过flags参数）。
在Python的re模块中，\w是一个特殊的字符类，它匹配任何字母数字字符（等价于[a-zA-Z0-9_]）。这包括所有大写和小写字母、所有数字以及下划线（_）。
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
s = 'wrs_python wrs_home wrs_ok'
match = re.search(pattern,s)   #wrs_python    只取了第一个值
print(match.group())

lst = re.findall(pattern,s)
print(lst)

print('-'*50)

pattern = r'\s*@'                #r 原始字符串
s = ' @温博 @王倩 @温如水'         # \s 表示匹配任何空白字符   * 表示匹配前面的字符（这里是 \s）零次或多次
lst = re.split(pattern,s)
print(lst)