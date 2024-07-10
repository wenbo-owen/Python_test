lst = [88,89,90,0,99]
lst1 =[]
lst2 =[]
print('原列表',lst)

for item in lst:
    if item >9 and item<100 :
        lst1.append('19'+str(item))
    elif item >=0 and item<10 :
        lst1.append('200'+str(item))

print(lst1)

print('-'*40)

for num,item in enumerate(lst):
    if str(item) != '0':
        lst2.append('19'+str(item))
    else:
        lst2.append('200'+str(item))


print(lst2)