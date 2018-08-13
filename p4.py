# -*- coding:utf-8 -*-
# https://www.cnbeta.com/ 科技新闻网站
# 数据是静态的html

import requests
from bs4 import BeautifulSoup

cookie="__utmb=208385984; __utmc=208385984; __utma=208385984.15468271.1526976723.1526976723.1526976723.1; __utmz=208385984.1526976724.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); Hm_lvt_4216c57ef1855492a9281acd553f8a6e=1526976726; Hm_lpvt_4216c57ef1855492a9281acd553f8a6e=1526977226; trc_cookie_storage=taboola%2520global%253Auser-id%3D7eac83c3-0bf5-40d9-aa3f-99de4b62a565-tuct1f71a8f"
header={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection":"Keep-Alive",
    "Cookie":cookie,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

url = "https://www.cnbeta.com/"

webdata = requests.get(url, headers=header)
html = BeautifulSoup(webdata.content, 'lxml')

# 新闻块
news_list = html.select("div.item")
for news in news_list:
    # 主要新闻
    main_news_list = news.select("dt a")
    if(len(main_news_list)>0):
        print(main_news_list[0])
    else:
         continue
    # 相关新闻
    other_news_list = news.select("div.cnbeta-update-list-article li a")
    for other_news in other_news_list:
        print(other_news)
    print("")
