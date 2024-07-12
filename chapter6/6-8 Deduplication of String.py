s='helloworldhelloworldfffsfggasdasdasdasdasd'

#(1)字符串拼接及not in

new_s=''

for item in s:
    if item not in new_s:
        new_s+=item

print(new_s)

print('-'*50)
#(2) 使用所引+not in
new_s2=''

for item in range(len(s)):
    if s[item] not in new_s2:
        new_s2+=s[item]

print(new_s2)

print('-'*50)
#(3) 通过集合去重
new_s3 = set(s)
lst = list(new_s3)
lst.sort(key=s.index)
print(''.join(lst))



