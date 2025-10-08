"""
        使用rullib获取百度首页的源码

"""
import urllib

# 1.定义一个url
url = "http://www.baidu.com"
# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 3.获取响应中的页面的源码
#返回的是字节形式的二进制数据
#我们要将二进制数据转换成字符串
#二进制--->字符串 解码 decode("解码的格式")
content =response.read().decode("utf-8")
# response 的一个类型 六个方法
print(type(response))  #查看respons 的类型  HTTPResponse
# 1.以一个字节一个字节的去读
response.read()
# 2.读取一行
response.readline()
# 3。一行一行的读取
response.readline()
# 4.读取状态码
response.getcode()
# 5.读取url
response.geturl()
# 6.读取状态信息
response.getheaders()



print(response.getcode())

# 返回的是url地址



