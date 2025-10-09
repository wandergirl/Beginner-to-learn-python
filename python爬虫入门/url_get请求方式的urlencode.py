# urlencode应用场景：多个参数的时候
# https：//www.baidu.com/s?wd=早濑优香&sex=女
import urllib.request,urllib.parse
# data = {
#     'wd':"早濑优香",
#     'sex':'女'
# }
# a =urllib.parse.urlencode(data)
#
# print(a)



# 定制请求头仅仅UA会被百度反爬
import time, random
time.sleep(random.uniform(1, 3))
# 爬取的url地址
url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=utf8&sa=vs_ala_img&fr=ala&ala=1&alatpl=normal&pos=3&dyTabStr=MCwzLDEsMiwxMyw3LDYsNSwxMiw5&word=%E6%97%A9%E6%BF%91%E4%BC%98%E9%A6%99&lid=c72082a100001507&topic=%E6%97%A9%E6%BF%91%E4%BC%98%E9%A6%99?'
# 定制请求头
# base_url={
#     'wd':"早濑优香",
#      'sex':'女',
#     'location':'千禧年科技学院'
#
# }
# new_data =urllib.parse.urlencode(base_url)
# print(new_data)
# url1 = url + new_data
# print(url1)
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.baidu.com/",
    "Connection": "keep-alive"
}
# 模拟浏览器向服务器发送请求
request = urllib.request.Request(url,headers=headers)
# 接受响应
response = urllib.request.urlopen(request)
# 将读取到的源码赋值给content
content = response.read().decode('utf-8')
# 打印conten文本
print(content)
