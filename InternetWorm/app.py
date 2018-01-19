import urllib.request as urllib2, http.cookiejar as cookielib
from bs4 import BeautifulSoup
#下载链接
url = 'https://baike.baidu.com/item/Python/407313'

#模拟浏览器请求
request = urllib2.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib2.urlopen(request)
print ('response2:',response2.read())

#cookie请求方法
#创建cookie容器
cj = cookielib.CookieJar()
#创建opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#给urllib2安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
response = urllib2.urlopen(url)
#如果情请求成功

#创建解析器对象
soup = BeautifulSoup(
    response.read(),#文档字符串
    'html.parser',#HTML解析器
    from_encoding = 'utf-8'#HTML文档的编码
)
#搜索节点find_all(name, attrs, string)
node = soup.find_all('div')#,class_='abc',string='Python')
#查找节点的标签名称：node.name
#获取查找到的a节点的href属性：node['href']
#获取查找到的a节点的链接文字：node.get_text()
if response.getcode()==200 :
    print ('response:',node)
