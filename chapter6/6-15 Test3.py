import re

'''
注意 这里的? 要加/ 
'''

s = 'https://image0.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3&step_word=&hs=0&pn=11&spn=0&di=46137345https://image2.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3&step_word=&hs=0&pn=11&spn=0&di=46154551212https://image0.baidu.com/search/detail?ct=5223230&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3&step_word=&hs=0&pn=11&spn=0&di=662323232'

pattern = 'https://image\d{1}.baidu.com/search/detail\?ct=\d*&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3&step_word=&hs=0&pn=11&spn=0&di=\d*'

lst =re.findall(pattern, s)
for i in lst:
    print(i)

