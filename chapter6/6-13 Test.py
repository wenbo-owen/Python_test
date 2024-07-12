lst =['京A8888','黑A9999','陕A6666']

for item in lst:
    area = item[0:1]
    print('{0} 归属地 {1}'.format(item,area))

print('-'*50)

s = 'HelloPython,HelloJava,hellophp'
word = input('请输入要统计的字符')
print('{0}在{1}一共出现了{2}'.format(word,s,s.upper().count(word)))

