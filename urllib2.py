# coding:utf8

import urllib2
import cookielib

url = 'http://www.baidu.com'

print '第一中方法'
# 直接请求
response = urllib2.urlopen(url)
print '获取状态码，如果是200表示获取成功'
print response.getcode()
print '读取内容长度' 
print  len(response.read())


print '第二种方法'
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
print '获取状态码，如果是200表示获取成功'
print response2.getcode();
print '读取内容长度' 
print len(response2.read())



print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print '打印cookie的数据'
print cj
print '获取状态码，如果是200表示获取成功'
print response3.getcode()
print '读取内容长度' 
print  len(response3.read())
