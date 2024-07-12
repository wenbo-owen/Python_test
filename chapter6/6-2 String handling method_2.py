s='Hello World'
# 默认参数替换所有
new_s = s.replace('o','你好')
print(new_s)

# 最后一个参数是替换次数，默认是全部替换
new_s1 = s.replace('o','你好',1)
print(new_s1)

#字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))


#去掉字符串左右的空格
s = '    Hello    MG    '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# 去除指定的字符
s3 = 'dl-helloworld'
print(s3.strip('ld'))  # 与顺序无关
print(s3.lstrip('ld'))
print(s3.rstrip('ld'))

