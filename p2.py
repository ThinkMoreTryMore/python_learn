# -*- coding:utf-8 -*-
# 爬取https://www.192tt.com/gc/toutiao/index.html    头条女神 第一页
# 爬取https://www.192tt.com/gc/toutiao/index_2.html    头条女神 第二页
# 获取的是首页的图片网址和图片介绍
# 用循环 遍历第1页到第10页
# time。sleep(1) 每获取一次就休眠一秒

import requests
from bs4 import BeautifulSoup
import time
import urllib3
import logging

urllib3.disable_warnings()
logging.captureWarnings(True)
# url = "https://www.192tt.com/gc/toutiao/index.html"

cookie = "vihwnecookieclassrecord=%2C39%2C57%2C"
header = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Cookie":cookie,
	"user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

j=""
for i in range(1,10) :
    if i==1:
        j=""
    else:
        j="_"+str(i)
    url = "https://www.192tt.com/gc/toutiao/index"+j+".html"
    j=""
    webdata = requests.get(url, verify=False, headers=header,  stream=True)
    html = BeautifulSoup(webdata.content, 'lxml')
    img_list = html.select(".mainer .piclist ul.clearfix img")
# img_des = html.select(".mainer .piclist ul.clearfix")
# print(img_list[0]["lazysrc"])
# print(img_list[0]["alt"])

    for img in img_list:
        print(img["alt"]+"\t"+img["lazysrc"])
    # print("111")
    time.sleep(1)