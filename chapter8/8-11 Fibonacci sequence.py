#斐波那契数列
def fac(n):
    if n==1 or n==2:
        return 1
    else:
        return fac(n-1) + fac(n-2)

print(fac(9))

for i in range(1,10):
    print(fac(i),end='\t')
print()