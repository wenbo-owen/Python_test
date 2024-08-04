import requests
url = 'https://search-operate.cdn.bcebos.com/e8cbce1d53432a6950071bf26b640e2b.gif'

resp = requests.get(url)

# 保存到本地
# 本地 二进制数据
with open('logo.png','wb') as file:
    file.write(resp.content)

