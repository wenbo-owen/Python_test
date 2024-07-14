
'''

    字符串验证
'''


#isdigit()十进制的阿拉伯数字
print('123'.isdigit())
print('一二三'.isdigit())
print('0b1010'.isdigit())
print('ⅡⅡⅡ'.isdigit())
print('-'*50)
#所有字符都是数字
print('123'.isnumeric())
print('一二三'.isnumeric())
print('0b1010'.isnumeric())
print('ⅡⅡⅡ'.isnumeric())
print('壹贰叁'.isnumeric())

print('-'*50)
#所有的字符都是字母（包括中文字符）
print('hello你好'.isalpha())      #True
print('hello你好123'.isalpha())   #False
print('hello你好一二三'.isalpha())   #True
print('hello你好ⅡⅡⅡ'.isalpha())   #False
print('hello你好壹贰叁'.isalpha())   #True


print('-'*50)
#所有字符都是数字或字母
print('hello你好'.isalnum())      #True
print('hello你好123'.isalnum())   #False
print('hello你好一二三'.isalnum())   #True
print('hello你好ⅡⅡⅡ'.isalnum())   #False
print('hello你好壹贰叁'.isalnum())   #True

#判断字符的大小写

print('-'*50)
print('HelloWorld'.islower())       #False
print('helloworld'.islower())       #True
print('hello你好'.islower())          #True

print('-'*50)
print('HelloWorld'.isupper())   #False
print('HELLOWORLD'.isupper())   #True
print('hello你好'.isupper())  #True

#所有字符都是首字母大写
print('-'*50)
print('HelloWorld'.istitle())
print('Helloworld'.istitle())
print('Hello'.istitle())
print('Hello World'.istitle())
print('Hello world'.istitle())

#判断是否都是空白字符
print('-'*50)
print('\t'.isspace())       #True
print(' '.isspace())        #True
print('\n'.isspace())       #True



