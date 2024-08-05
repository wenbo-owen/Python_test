'''
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

import requests
import re

url = 'http://www.weather.com.cn/weather1d/101010100.shtml'  #爬虫打开的浏览器网页

resp = requests.get(url)
#设置一下编码格式
resp.encoding = 'utf-8'
print(resp.text)   #resp响应对象，对象名.属性名

city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
wd = re.findall('<span class="wd">(.*)</span>',resp.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)

print('city is :',city)
print('weather is :',weather)
print('wd is :',wd)
print('zs is :',zs)

print('-'*50)

for aaa in zip(city,weather,wd,zs):
    print(aaa)

print('-'*50)



lst = []
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])

print(lst)
for item in lst:
    print(item)







'''
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">34/26℃</span>
<span class="zs">较适宜</span>
'''
