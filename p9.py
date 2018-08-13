# -*- coding:utf-8 -*-

# 爬取 没品小视频 up主的 所有视频 链接

import requests
import json

url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=4445596&page=1&pagesize=25"
webdata = requests.get(url)
jsondata =json.loads(webdata.text)
# print(jsondata["data"]["vlist"][1]["title"])
list = jsondata["data"]["vlist"]
for info in list:
    print(info["title"])
    print("https://www.bilibili.com/video/av"+str(info["aid"]))