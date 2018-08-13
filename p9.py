# -*- coding:utf-8 -*-
# 爬取https://www.nvshens.com/rank/  排行榜首页

import requests
from bs4 import BeautifulSoup

name="https://www.nvshens.com"
url = "https://www.nvshens.com/rank/"

webdata = requests.get(url)
html = BeautifulSoup(webdata.content, 'lxml')

entry_box_rank_list = html.select("div#post_rank div.entry_box_rank") # 获取所有的排行榜
for entry_box_rank in entry_box_rank_list:
    title = entry_box_rank.select("div.hot_tag") # 排行榜的名称
    print(title[0].text)
    modelInfo_list = entry_box_rank.select("ul li")
    for i in range(0, len(modelInfo_list)):
        modelLink = "" # 模特的网址
        modelName = "" # 模特的名称
        modelLink = modelInfo_list[i].select("a")[0]["href"]
        model_a = modelLink.split("/")
        if (i == 0):
            modelName = modelInfo_list[i].select("div.first_girlli_div_rank h3")[0]
        else:
            modelName = modelInfo_list[i].select("a")[0]
        print(modelName.text+"\t\t"+str(name)+str(modelLink))
        print(str("https://img.onvshen.com:85")+str(modelLink)+model_a[2]+".jpg")
    print("")
