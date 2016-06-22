import time
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import sys
from pytesseract import image_to_string
import http.client
import threading
import urllib.parse
threshold = 140
table = []
for i in range(256) :
    if i < threshold :
        table.append(0)
    else :
        table.append(1)

def getVerify(name):
    im = Image.open(name)
    imgry = im.convert("L")
    imgry.save("g" + name)
    out = imgry.point(table, "1")
    out.save("b" + name)
    text = image_to_string(out)
    text = text.strip()
    text = text.upper()
    text = text.replace(" ", "")
    print (text) 
    return text
def fun() :
	conn = http.client.HTTPConnection("xk.tjut.edu.cn")
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		#"Connection" : "keep-alive",
		"Upgrade-Insecure-Requests" : "1"
		}
	conn.request("GET", "/xsxk/", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	cookie = r1.getheader("set-cookie").split(";")[0].strip()
	conn.close()
	print(cookie)
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "image/webp,image/*,*/*;q=0.8",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		#"Connection" : "keep-alive",
		"Cookie" : cookie
		}
	conn.request("GET", "/xsxk/main.xk", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	conn.close()
	#cookie = r1.getheader("set-cookie").split(";")[0].strip()
	print(cookie)
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/",
		#"Connection" : "keep-alive",
		"Upgrade-Insecure-Requests" : "1",
		"Cookie" : cookie
		}	
	conn.request("GET","/xsxk/servlet/ImageServlet", None, heads)
	r1 = conn.getresponse()
	data = r1.read()
	conn.close()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	file = open("a.jpg", "wb")
	file.write(data)
	file.close()
	verifyCode = getVerify("a.jpg")
	# heads = {
	# 	"Host" : "xk.tjut.edu.cn",
	# 	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
	# 	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	# 	"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	# 	"Accept-Encoding" : "gzip, deflate",
	# 	"Referer" : "http://xk.tjut.edu.cn/xsxk/logout.xk",
	# 	"Connection" : "keep-alive",
	# 	"Cookie" : cookie
	# 	}	
	# conn.request("GET","/xsxk/main.xk", None, heads)
	# r1 = conn.getresponse()
	# conn.close()
	# print(heads)
	# print(r1.status, r1.reason, r1.msg)
	params = urllib.parse.urlencode({
		"username" : "20145477",
		"password" : "5606595222",
		"verifyCode" : verifyCode
	        })
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/",
		"Connection" : "keep-alive",
		"Content-Type" : "application/x-www-form-urlencoded",
		"Origin" : "http://xk.tjut.edu.cn",
		"Upgrade-Insecure-Requests" : "1",
		"Cookie" : cookie
		}
	conn.request("POST", "/xsxk/login.xk", params, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding" : "gzip, deflate",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/logout.xk",
		#"Connection" : "keep-alive",
		"Cookie" : cookie
	}
	conn.request("GET", "/xsxk/index.xk", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/",
		#"Connection" : "keep-alive",
		"Upgrade-Insecure-Requests" : "1",
		"Cookie" : cookie
		}	
	conn.request("GET","/xsxk/servlet/ImageServlet", None, heads)
	r1 = conn.getresponse()
	data = r1.read()
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "image/webp,image/*,*/*;q=0.8",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		#"Connection" : "keep-alive",
		"Cookie" : cookie
		}
	conn.request("GET", "/xsxk/main.xk", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg, r1.read().decode())
	conn.close()
	# heads = {
	# 	"Host" : "xk.tjut.edu.cn",
	# 	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
	# 	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	# 	"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	# 	"Accept-Encoding" : "gzip, deflate",
	# 	"Referer" : "http://xk.tjut.edu.cn/xsxk/index.xk",
	# 	"Connection" : "keep-alive",
	# 	"Cookie" : cookie
	# }
	# conn.request("GET", "/xsxk/loadData.xk?method=cacheIsOpen", None, heads)
	# r1 = conn.getresponse()
	# print(heads)
	# print(r1.status, r1.reason, r1.msg)
	# conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "/*/",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/main.xk",
		"Connection" : "keep-alive",
		"Cookie" : cookie,
		"X-Requested-With" : "XMLHttpRequest"
	}
	conn.request("GET", "/xsxk/loadData.xk?method=getXsLoginCnt", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg, r1.read().decode())
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "*/*",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/main.xk",
		#"Connection" : "keep-alive",
		"Cookie" : cookie,
		"X-Requested-With" : "XMLHttpRequest"
	}
	conn.request("GET", "/xsxk/loadData.xk?method=getXksj", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg, r1.read().decode())
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "*/*",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/index.xk",
		#"Connection" : "keep-alive",
		"X-Requested-With" : "XMLHttpRequest",
		"Cookie" : cookie
	}
	conn.request("GET", "/xsxk/loadData.xk?method=loginCheck", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg, r1.read().decode())
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/index.xk",
		"Upgrade-Insecure-Requests" : "1",
		#"Connection" : "keep-alive",
		"Cookie" : cookie
	}
	conn.request("GET", "/xsxk/xkjs.xk?pyfaid=01482&jxqdm=1&data-frameid=main&data-timer=2000&data-proxy=proxy.xk", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg, r1.read().decode())
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "*/*",
		"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
		"Accept-Encoding" : "gzip, deflate, sdch",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/xkjs.xk?pyfaid=01482&jxqdm=1&data-frameid=main&data-timer=2000&data-proxy=proxy.xk",
		"Upgrade-Insecure-Requests" : "1",
		#"Connection" : "keep-alive",
		"Cookie" : cookie
	}
	conn.request("GET", "/xsxk/tjxk.xk", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	conn.close()
	# heads = {
	# 	"Host" : "xk.tjut.edu.cn",
	# 	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
	# 	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	# 	"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	# 	"Accept-Encoding" : "gzip, deflate",
	# 	"Referer" : "http://xk.tjut.edu.cn/xsxk/index.xk",
	# 	"Connection" : "keep-alive",
	# 	"Cookie" : cookie
	# }
	# conn.request("GET", "/xsxk/loadData.xk?method=getCurTime", None, heads)
	# r1 = conn.getresponse()
	# print(heads)
	# print(r1.status, r1.reason, r1.msg, r1.read().decode())
	# conn.close()
	# heads = {
	# 	"Host" : "xk.tjut.edu.cn",
	# 	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
	# 	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	# 	"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	# 	"Accept-Encoding" : "gzip, deflate",
	# 	"Referer" : "http://xk.tjut.edu.cn/xsxk/xkjs.xk?pyfaid=01482&jxqdm=1&data-frameid=main&data-timer=2000&data-proxy=proxy.xk",
	# 	"Connection" : "keep-alive",
	# 	"Cookie" : cookie
	# }
	# conn.request("GET", "/xsxk/loadData.xk?method=gerPyfaCurTime&timeOne=", None, heads)
	# r1 = conn.getresponse()
	# print(heads)
	# print(r1.status, r1.reason, r1.msg, r1.read().decode())
	# conn.close()

	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding" : "gzip, deflate",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/index.xk",
		"Connection" : "keep-alive",
		"Cookie" : cookie,
		"X-Requested-With" : "XMLHttpRequest"
	}
	conn.request("GET", "/xsxk/loadData.xk?method=gerJxbXkrs", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.msg)
	conn.close()
	heads = {
		"Host" : "xk.tjut.edu.cn",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding" : "gzip, deflate",
		"Referer" : "http://xk.tjut.edu.cn/xsxk/qxgxk.xk",
		"Connection" : "keep-alive",
		"Cookie" : cookie,
		"X-Requested-With" : "XMLHttpRequest"
	}
	conn.request("GET", "/xsxk/xkOper.xk?method=handleTjxk&jxbid=201620171066245601&glJxbid=", None, heads)
	r1 = conn.getresponse()
	print(heads)
	print(r1.status, r1.reason, r1.read().decode(), r1.msg)
	conn.close()
#while(True) :
#    fun()
#    time.sleep(0.1)
fun()
