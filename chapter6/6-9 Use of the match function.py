'''
    re.match(pattern, string,flags=re.IGNORECASE)
    用于从字符串的开始位置进行匹配，如果起始位置匹配成功，结果为Match对象，否则结果为None
例如"^"和"$"分别表示匹配的开始和结束
元字符         描述说明                 举例                   结果
.             匹配任意字符（除\n）         'p\nytho\tn '            p、 y、 t、 h、 o、 \t、 n
\w          匹配字母、数字、下划线       'python\n123'          p、y、 t、 h、 o、 n、 1、2、3
\W          匹配非字母、数字、下划线     'python\n123'          \n
\s            匹配任意空白字符             'python\t123'         \t
\S           匹配任意非空白字符         'python\t123'         p、y、 t、 h、 o、 n、 1、2、 3
\d            匹配任意十进制数             'pythont123'           1、2、3

限定符        描述说明                    举例                  结果
？         匹配前面的字符0次或1次        colou?r        可以匹配color或colour
+        匹配前面的字符1次或多次         colou+r        可以匹配colour或colouu…..r
*        匹配前面的字符0次或多次        colou*r        可以匹配color或colouu....r
{n}        匹配前面的字符n次                colou{2}r        可以匹配colouur
{n,}        匹配前面的字符最少n次            colou{2,}r        可以匹配colouur或colouuu…..r
{n,m}    匹配前面的字符最小n次，最多m次 colou{2,4}r      可以匹配colouur或colouuur或colouuuur

其它字符             描述说明                 举例              结果
区间字符[]    匹配[]中所指定的字符            [.?!]          匹配标点符号点、问号，感叹号
                                        [0-9]                 匹配0、1、2、3、4、5、6、7、8、9

排除字符^    匹配不在[]中指定的字符        [^0-9]        匹配除0、1、2、3、4、5、6、7、8、9的字符
选择字符|    用于匹配|左右的任意字符    \d{18}\d{15}    匹配15位身份证或18位身份证
转义字符\        同Python中的转义字符        \.            将.作为普通字符使用
[\u4e00-\u9fa5]    匹配任意一个汉字
分组（)            改变限定符的作用        six|fourth          匹配six或fourth
                                        (six|four)th        匹配sixth或fourth


'''

import re

pattern = '\d\.\d+'                 # +限定符， \d 0-9数字出现1次或多次
s = 'I study Python 3.11 everyday'  # 待匹配字符串
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

