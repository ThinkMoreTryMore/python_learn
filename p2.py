# coding:utf-8

import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/note/665900598/'

webdata = requests.get(url)
webdata.encoding = 'utf-8'
text = webdata.text

print(text)