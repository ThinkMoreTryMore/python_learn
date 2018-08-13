# coding:utf-8
# how2j.cn 的 cookies 登录验证
import requests
import urllib
import chardet
from bs4 import BeautifulSoup


url = "http://how2j.cn/frontconfigPage#nowhere"
code = chardet.detect(urllib.urlopen(url).read() )
print(code["encoding"])

cookie = 'JSESSIONID=A8A58F4D81C38A68BCEB86459946DE29;user.uuid=9bd7c3da-6388-489f-98ce-343b0d0727ea'


headers = {
    'Host':'how2j.cn',
    'Referer':'http://how2j.cn/frontloginPage?act=login',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'cookie':cookie,
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection':'keep-alive'
}
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'lxml')
# html.encoding = 'gbk'
alipayName = soup.select("#alipayName")
userCount = soup.select("#alipayCount")
userName = soup.select("#username")

print(userName[0]['value'])
print(alipayName[0]['value'])
print(userCount[0]['value'])