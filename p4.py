# -*- coding:utf-8 -*-
# 爬取http://www.haotudao.cc/    好图岛首页
# http://www.haotudao.cc/xingan 好图岛性感美女

import requests
from bs4 import BeautifulSoup
import time
import urllib3
import logging

urllib3.disable_warnings()
logging.captureWarnings(True)

header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

url = "http://www.haotudao.cc/"
webdata = requests.get(url, headers=header)
html = BeautifulSoup(webdata.content, 'lxml')

li_content = html.select("ul#menu-haofuli li.menu-item")

for li in li_content:
    url2 = li.select("a")[0]["href"]
    webdata2 = requests.get(url2, headers=header)
    html2 = BeautifulSoup(webdata2.content, 'lxml')
    current_name = html2.select("div.subsidiary span.current")
    print(current_name[0].text)

    for i in range(1, 3, 1):
        if (i == 1):
            url3 = url2
        else:
            url3 = url2 +"/page/"+ str(i)
        webdata3 = requests.get(url3, headers=header)
        html3 = BeautifulSoup(webdata3.content, 'lxml')
        a_content = html3.select("div.thumbnail a.zoom")
        # print(a_content[0])
        for a in a_content:
            print(a["href"])
            print(a.select("img")[0]["src"])
            print(a.select("img")[0]["alt"])
        print("第" + str(i) + "页")
        time.sleep(0.2)
    print(current_name[0].text)