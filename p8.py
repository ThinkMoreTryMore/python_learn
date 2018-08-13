# -*- coding:utf-8 -*-
# 爬取https://www.nvshens.com/gallery/ 首页
# 女神写真
# 每个关键字的第一个

import requests
from bs4 import BeautifulSoup

name = "https://www.nvshens.com/"
url = "https://www.nvshens.com/gallery/"
webdata = requests.get(url)
html = BeautifulSoup(webdata.content, 'lxml')

# 获取 关键字导引搜索
a_link_list = html.select(".tag_div li a")
for a_link in a_link_list:
    url = "https://www.nvshens.com" + str(a_link["href"])
    # print("https://www.nvshens.com"+str(a_link["href"]))
    # 1页
    j = url
    for i in range(1, 2):
        if (i != 1):
            j = url + str(i) + ".html"
        print(j)
        webdata2 = requests.get(j)
        html2 = BeautifulSoup(webdata2.content, 'lxml')
        a_link_list = html2.select("div#listdiv ul li.galleryli a.galleryli_link")
        # 第一个
        img_list = a_link_list[0].select("img")
        print(img_list[0]["alt"] + "\t\t" + name + a_link_list[0]["href"] + "\t\t" + img_list[0]["data-original"])
        print("")
# a_link_list = html.select("div#listdiv ul li.galleryli a.galleryli_link")
# for a_link in a_link_list:
#     print(a_link)
