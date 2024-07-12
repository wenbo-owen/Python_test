s = '伟大的中国梦'
#编码 str ->bytes

scode = s.encode(errors='replace')  #默认utf-8,因为utf-8中文占3个字节，英文占1个字节
print(scode)

scode_gbk = s.encode('gbk',errors='replace')
print(scode_gbk)

#编码中的出错问题
s2='耶✌'
scode_error = s2.encode('gbk',errors='ignore')
print(scode_error)

# s2='耶✌'
# scode = s2.encode('gbk',errors='strict')
# print(scode)

s2='耶✌'
scode_error = s2.encode('gbk',errors='replace')
print(scode_error)

#解码过程 bytes ->str
print(bytes.decode(scode_gbk,'gbk'))

print(bytes.decode(scode,'utf-8',errors='replace'))