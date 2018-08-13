# -*- coding:utf-8 -*-
# 爬取 http://www.lesmao.me/
# 获取一到四页的图片名称和图片网址

import requests
from bs4 import BeautifulSoup
import time
import urllib3
import logging

urllib3.disable_warnings()
logging.captureWarnings(True)
cookie = ""
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Cookie":cookie,
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

for i in range(1,4):
    if(i==1):
        j=""
    else:
        j="plugin.php?id=group&page="+str(i)
    print(j)
    url = "http://www.lesmao.me/"+j
    webdata = requests.get(url, headers=header)
    html = BeautifulSoup(webdata.content, 'lxml')

    contents= html.select("div#index-pic div.group")
    for content in contents:
        img = content.select("div.photo a")
        bution = content.select("div.bution div.data")
        print("http://www.lesmao.me/"+img[0]["href"])
        print(img[0].select("img")[0]["alt"])
        print(img[0].select("img")[0]["src"])
        # print(bution[0].text)
        print("")
