# -*- coding:utf-8 -*-
# 爬取http://www.haotudao.cc/    好图岛首页
# http://www.haotudao.cc/page/2  第二页

import requests
from bs4 import BeautifulSoup
import time
import urllib3
import logging

urllib3.disable_warnings()
logging.captureWarnings(True)

header = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}
for i in range(1,10,1):
    if(i==1):
        url = "http://www.haotudao.cc/"
    else:
        url="http://www.haotudao.cc/page/"+str(i)
    webdata = requests.get(url, headers=header)
    html = BeautifulSoup(webdata.content, 'lxml')

    a_content = html.select("div.thumbnail a.zoom")
    for a in a_content:
        print(a["href"])
        print(a.select("img")[0]["src"])
        print(a.select("img")[0]["alt"])
    print("第"+str(i)+"页")
    time.sleep(1)