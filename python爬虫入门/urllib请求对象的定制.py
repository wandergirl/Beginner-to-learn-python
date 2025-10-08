"""
            url的组成:
                        http/https  www.baidu.com      80/443      s      wd=周杰伦        #
                          协议           主机            端口号     路径       参数          锚点
            UA介绍:  UserAgent 用户代理 简称UA 它是一个特殊字符串头使得服务器识别用户的操作系及版本


"""
import urllib
url = 'https://www.youtube.com'
header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}
request =urllib.request.Request(url=url,hearders=header)
response = urllib.request.urlopen(request)
content =response.read().decode('utf-8')
print(content)