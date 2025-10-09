import urllib.request
import json
url = "https://fanyi.baidu.com/sug"
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}
data ={
    'kw':'legend'


}

# post请求的参数，必须进行编码
data = urllib.parse.urlencode(data).encode("utf-8")

request = urllib.request.Request(url,data=data,headers=headers)
response =urllib.request.urlopen(request)
content =response.read()
# json数据转换成字符串
obj = json.loads(content)
print(obj)
obj = json.dumps(obj)
print(obj)


