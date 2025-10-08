# 需求获取https：//
import urllib

url = "https://www.google.com/search?q="
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',}
# 将早濑优香四个子变成unicode编码
name = urllib.parse.quote("早濑优香")
request =urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)