s1 = "Hello World!"
new_s2 =s1.lower()
print(new_s2)

new_s3 = s1.upper()
print(new_s3)

# 字符串的分隔
e_mails = '313864336@qq.com'
lst = e_mails.split('@')
print('邮箱名:',lst[0],'邮件服务器域名',lst[1])

print(s1.count('o'))  # o 在字符串中出现了2次

print(s1.find('o'))
print(s1.find('p')) #-1 没有找到

print(s1.index('o'))
#print(s1.index('p')) #-1 没有找到