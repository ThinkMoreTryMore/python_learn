# -*- coding:utf-8 -*-
# 爬取 http://www.jiemian.com/   界面新闻网站 因为页面复杂 样式虽然统一 但是不是结构单一的页面 分析难度加大

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

url = "http://www.jiemian.com/"
webdata = requests.get(url, headers=header)
html = BeautifulSoup(webdata.content, 'lxml')
news_view_content = html.select("div.news-view")

for news_view in news_view_content:
    # print(news_view[0])
    print("html:\t"+news_view.select("div.news-img a")[0]["href"])
    print("img_src:\t http:"+news_view.select("div.news-img a img")[0]["src"])
    print("header:\t"+news_view.select("div.news-header h3 a")[0].text)
    # print("content:\t"+news_view.select("div.news-main p")[0].text)
    print("")

