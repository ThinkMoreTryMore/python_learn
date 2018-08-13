# -*- coding:utf-8 -*-
# https://apod.nasa.gov/apod/ap(xxx).html 分析
# xx代表的是今天 每日一图


import requests
from bs4 import BeautifulSoup
import time

url = "https://apod.nasa.gov/apod/ap" + str(time.strftime("%Y%m%d"))[2:] + ".html"
print(url)
# 单页面的解析
webdata = requests.get(url)
html = BeautifulSoup(webdata.content, 'lxml')
img_big = html.select("a")
title = html.select("title")
# for aContent in aContent_list:
# https://apod.nasa.gov/apod/image/1805/RedRectangle_HubbleSchmidt_1140.jpg 正确的
# image/1805/RedRectangle_HubbleSchmidt_1140.jpg 解析的
print("title:" + title[0].text)
print("bigImg: \thttps://apod.nasa.gov/apod/" + img_big[1]["href"])
print("smallImg: \thttps://apod.nasa.gov/apod/" + img_big[1].select("img")[0]["src"])
print("")
