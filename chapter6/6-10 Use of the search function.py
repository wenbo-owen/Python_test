'''
    re.search(pattern, string,flags=re.IGNORECASE)
    用于在整个字符串中搜索第一个匹配的值，如果起始位置匹配成功，结果为Match对象，否则结果为None

在Python的re模块中，re.search(pattern, string, flags=0)函数用于在字符串中搜索第一个匹配正则表达式的子串。其中，pattern是正则表达式的模式，string是待搜索的字符串，而flags是一个可选参数，用于指定搜索时的额外选项。

re.I是flags参数的一个选项，它代表“忽略大小写”（IGNORECASE）的搜索。当你设置re.I作为flags参数时，搜索过程将不会区分大小写字母，即大写字母和小写字母被视为等同。
'''



import re

pattern = '\d\.\d+'                 # +限定符， \d 0-9数字出现1次或多次
s = 'I study Python 3.11 everyday Python2.7 I love you '  #待匹配字符串
match = re.search(pattern, s,re.I)
print(match)    #None
print('匹配值的起始位置', match.start())
print('匹配值的终止位置', match.end())
print('匹配区间的位置元素', match.span())   #元组
print('待匹配的字符串', match.string)
print('匹配的数据', match.group())

print('-'*50)


s2 = '4.10 I study Python everyday'
match2 = re.search(pattern, s2, re.I)

print(match2)   #<re.Match object; span=(0, 4), match='3.11'>
print('匹配值的起始位置', match2.start())
print('匹配值的终止位置', match2.end())
print('匹配区间的位置元素', match2.span())   #元组
print('待匹配的字符串', match2.string)
print('匹配的数据', match2.group())

print('-'*50)

s3 = 'I study Python everyday'
match3 = re.search(pattern, s3, re.I)
print(match3)