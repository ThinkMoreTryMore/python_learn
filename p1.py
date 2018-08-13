# -*- coding:utf-8 -*-
# 爬取http://www.freebuf.com/articles
import requests
from bs4 import BeautifulSoup
url= "http://www.freebuf.com/articles"

cookie="3cb185a485c81b23211eb80b75a406fd=1524361666; PHPSESSID=q6rhlk34ssd6nt7jveje2cr617"
headers = {
    "Cookie": cookie,
    "Host": "www.freebuf.com",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

webdata = requests.get(url, headers=headers)
html = BeautifulSoup(webdata.content, 'lxml')

title_h = html.select(".news-info .article-title")
introduce_h = html.select(".news-info .text")
look_h = html.select(".new-info .look")


# print(title_h[0]["href"])
# print(title_h[0]["title"])

for title in title_h:
    print(title["href"])