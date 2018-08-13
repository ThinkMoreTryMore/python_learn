# coding:utf-8
# 获取今日头条 返回json数据

import requests
import urllib
import chardet
from bs4 import BeautifulSoup
import json

url = "https://www.toutiao.com/api/pc/focus/"
code = chardet.detect(urllib.urlopen(url).read() )
print(code["encoding"])

cookie = ''


headers = {

}
html = requests.get(url, headers=headers)
# soup = BeautifulSoup(html.text, 'lxml')
data = json.loads(html.content)
news = data['data']['pc_feed_focus']

# print(html)
# print(data)
# print(news)
urls = []
for n in news:
    title = n['title']
    img_url = n['image_url']
    url = n['media_url']
    urls.append(url)
    # print(url)
    print(url, title, img_url)

print(urls)