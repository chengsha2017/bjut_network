# -*- coding:utf-8 -*-
#!/mport HTMLParser 
import urlparse 
import urllib 
import urllib2 
import cookielib 
import string 
import re 
  
#登录的主页面 
hosturl = 'https://lgn.bjut.edu.cn/' #自己填写 
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据） 
posturl = 'https://lgn.bjut.edu.cn/' #从数据包中分析出，处理post请求的url 
  
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie 
cj = cookielib.LWPCookieJar() 
cookie_support = urllib2.HTTPCookieProcessor(cj) 
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
urllib2.install_opener(opener) 
  
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功） 
h = urllib2.urlopen(hosturl) 

headers = {
	"Host": "lgn.bjut.edu.cn",
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/x-www-form-urlencoded",
	"Referer": "https://lgn.bjut.edu.cn/",
	"Connection": "close",
	"Content-Length": "71",
	"Upgrade-Insecure-Requests": "1",
}
postData = {
	"DDDDD": "", # your account 
	"upass": "", # your password
	"v46s": "1",
	"v6ip": "",	
	"f4serip": "172.30.201.2",
	"0MKKey": "",
}

#需要给Post数据编码 
postData = urllib.urlencode(postData) 
  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程 
request = urllib2.Request(posturl, postData, headers) 
print request 
response = urllib2.urlopen(request) 
text = response.read() 
print text
