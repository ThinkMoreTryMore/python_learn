# -*- coding:utf-8 -*-
# http://www.beshan.com/siren-dingzhi-lvxing#page/1  碧山 私人定制旅游网站
# http://www.beshan.com/siren-dingzhi-lvxing#page/2 第二页
# siren-dingzhi-lvxing 是私人定制旅行
# jingzhi-jiudian 是精致酒店
# 第一页的数据是静态的
# 第二页的数据开始是动态的json


import requests
from bs4 import BeautifulSoup
import time

# 加入循环 1-10页
url = "http://www.beshan.com/siren-dingzhi-lvxing#page/1"
# 单页面的解析
webdata = requests.get(url)
html = BeautifulSoup(webdata.content, 'lxml')
item_content = html.select("div#trips-content ul div.item")
for item in item_content:
    img = item.select("img")[0]["src"]
    city = item.select(".header .cities")[0].text
    title_link = item.select(".header .title a")[0]["href"]
    title = item.select(".header .title a")[0].text
    introduce = item.select("div.body div.description p")[0].text
    print(title)
    price_list = item.select("div.body div.price-display span")
    for price_content in price_list:
        print(price_content.text)
    print("")