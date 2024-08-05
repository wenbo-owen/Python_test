'''
    re.search(pattern, string,flags=re.IGNORECASE)
    用于在整个字符串中搜索第一个匹配的值，如果起始位置匹配成功，结果为Match对象，否则结果为None
    在Python的re模块中，re.findall(pattern, string, flags=0)函数用于在字符串中查找所有（非重叠）匹配正则表达式的子串，
    并返回一个列表。这个列表包含了所有匹配的子串。

    当你看到lst = re.findall(pattern, s, re.I)这样的代码时，它的含义如下：

    pattern：是一个字符串，表示要搜索的正则表达式模式。
    s：是一个字符串，表示要在其中搜索匹配项的文本。
    re.I：是一个标志（flag），指定搜索时忽略大小写。
    lst将是一个列表，包含了字符串s中所有与正则表达式pattern匹配（忽略大小写）的子串。

'''

import re

pattern = '\d\.\d+'                 # +限定符， \d 0-9数字出现1次或多次
s = 'I study Python 3.11 everyday Python2.7 I love you '  #待匹配字符串
lst = re.findall(pattern, s,re.I)
print(lst)    #None
#print('匹配值的起始位置', lst.start())
# print('匹配值的终止位置', match.end())
# print('匹配区间的位置元素', match.span())   #元组
# print('待匹配的字符串', match.string)
# print('匹配的数据', match.group())

print('-'*50)


s2 = '4.10 I study Python everyday'
lst2 = re.findall(pattern, s2, re.I)

print(lst2)   #<re.Match object; span=(0, 4), match='3.11'>


print('-'*50)

s3 = 'I study Python everyday'
match3 = re.findall(pattern, s3, re.I)
print(match3)