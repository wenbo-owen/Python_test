import requests
import re

# 定义函数

def get_html():
    url = 'http://www.weather.com.cn/weather1d/101010100.shtml'  # 爬虫打开的浏览器网页
    resp = requests.get(url)
    # 设置一下编码格式
    resp.encoding = 'utf-8'
    #print(resp.text)  # resp响应对象，对象名.属性名
    return resp.text

# 对数据进行解析
def parse_html(html_str):
    city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str)
    weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str)
    wd = re.findall('<span class="wd">(.*)</span>',html_str)
    zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html_str)

    lst = []
    for a, b, c, d in zip(city, weather, wd, zs):
        lst.append([a, b, c, d])

    return lst

