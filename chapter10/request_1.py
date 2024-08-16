import requests
import re

url = 'https://item.jd.com/10107746069194.html'

resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)

