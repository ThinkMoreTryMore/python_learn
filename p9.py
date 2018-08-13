# -*- coding:utf-8 -*-
# 查询 http://zhongguose.com 中国色的各种色号
# json 格式数据获取
import requests
import json
url = "http://zhongguose.com/colors.json"
print(url)
webdata = requests.get(url)
# print( webdata.content)
data = json.loads(webdata.content)

for color in data:
    print(color["RGB"])
    print(color["name"])
    print("**************")
