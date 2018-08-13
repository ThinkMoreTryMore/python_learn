# -*- coding:utf-8 -*-
# 爬取https://www.nvshens.com/meet/  巧遇女神

import requests
import urllib2
from bs4 import BeautifulSoup

name="https://www.nvshens.com/"
url = "https://www.nvshens.com/meet/ "

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Cookie":"gallery_25948=1; gallery_21771=1; records=%5B%7B%22id%22%3A%2223106%22%2C%22name%22%3A%22%u5218%u5B50%u7457%22%7D%2C%7B%22id%22%3A%2220483%22%2C%22name%22%3A%22%u767D%u6615%22%7D%2C%7B%22id%22%3A%2220677%22%2C%22name%22%3A%22%u30B5%u30D8%u30EB%u30FB%u30ED%u30FC%u30BA%22%7D%2C%7B%22id%22%3A%2216157%22%2C%22name%22%3A%22%u502A%u59AE%22%7D%2C%7B%22id%22%3A%2222494%22%2C%22name%22%3A%22%uC190%uC724%uC8FC%22%7D%5D; gallery_24923=1; Hm_lvt_f378865b660846b55ba91d29e1c4c04d=1525779765,1525790887,1525876994; Hm_lpvt_f378865b660846b55ba91d29e1c4c04d=1525880304",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}
response  = urllib2.urlopen(url)
# html = BeautifulSoup(webdata.content, 'lxml')
print(response.geturl()) # 获取重定向的网址

# entry_box_rank_list = html.select("div#post_rank div.entry_box_rank") # 获取所有的排行榜
# for entry_box_rank in entry_box_rank_list:
#     title = entry_box_rank.select("div.hot_tag") # 排行榜的名称
#     print(title[0].text)
#     modelInfo_list = entry_box_rank.select("ul li")
#     for i in range(0, len(modelInfo_list)):
#         modelLink = "" # 模特的网址
#         modelName = "" # 模特的名称
#         modelLink = modelInfo_list[i].select("a")[0]["href"]
#         if (i == 0):
#             modelName = modelInfo_list[i].select("div.first_girlli_div_rank h3")[0]
#         else:
#             modelName = modelInfo_list[i].select("a")[0]
#         print(modelName.text+"\t\t"+str(name)+str(modelLink))
#     print("")
