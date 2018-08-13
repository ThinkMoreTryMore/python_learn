# coding:utf-8
# 获取 网页的编码格式

import requests
import urllib
import chardet
from bs4 import BeautifulSoup


url = "http://how2j.cn"
code = chardet.detect(urllib.urlopen(url).read() )
print(code["encoding"])

html = requests.get(url)
# html.encoding = 'gbk'

print(html.text)