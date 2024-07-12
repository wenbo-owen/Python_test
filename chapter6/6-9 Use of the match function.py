'''
    re.match(pattern, string,flags=re.IGNORECASE)
    用于从字符串的开始位置进行匹配，如果起始位置匹配成功，结果为Match对象，否则结果为None

'''

import re

pattern = '\d\.\d+'                 # +限定符， \d 0-9数字出现1次或多次
s = 'I study Python 3.11 everyday'  #待匹配字符串
match = re.match(pattern, s,re.I)
print(match)    #None

print('-'*50)
s2 = '3.11 I study Python everyday'
match2 = re.match(pattern, s2, re.I)
print(match2)   #<re.Match object; span=(0, 4), match='3.11'>

print('匹配值的起始位置', match2.start())
print('匹配值的终止位置', match2.end())
print('匹配区间的位置元素', match2.span())   #元组
print('待匹配的字符串', match2.string)
print('匹配的数据', match2.group())

