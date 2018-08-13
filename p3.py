# -*- coding:utf-8 -*-
# http://www.beshan.com/api/trips/private?page=1 碧山 私人定制旅游网站
# http://www.beshan.com/api/trips/private?page=2 第二页
# 数据是动态的json

import requests
import json

cookie="_gat=1; Hm_lvt_ce3c557b15c1910f44be04196c6841dd=1526083100; Hm_lpvt_ce3c557b15c1910f44be04196c6841dd=1526092772; _ga=GA1.2.16321554.1526083100; _gid=GA1.2.877020239.1526083100; laravel_sessioneyJpdiI6ImV1b1NSYlVDbkFYYnRyeFlLM3lGbWc9PSIsInZhbHVlIjoieTFrUXI5dkY4Nmp1SWZMU3RFd21xcVN0aGhhRE1SS200UDUzS1VNVncwcUVvOHU1aWhWbjA4aHF5MTlwbjF4TGZienFoUWR2QkpiaVlUbGFUbFN6XC9RPT0iLCJtYWMiOiI1OTFkNjhkODJiZjkyMDhjMjFiYWEyMDNlODQ3M2NkYjE3ZDg0YzNhOTU2NTFhZjcyNWUxZjM2ZGQ4OWFmYzAwIn0%3D"
header={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Connection":"Keep-Alive",
    "Content-Type":"application/json",
    "Cookie":cookie,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

# 加入循环 1-10页
for i in range(1, 11):
    # 第一页
    url = "http://www.beshan.com/api/trips/private?page="+str(i)
    webdata = requests.get(url, headers=header)
    json_data = json.loads(webdata.text)
    data_list = json_data["data"]
    for data in data_list:
        print(data["title"])
        print(data["price"])
        print(data["imageUrl"])
        print(data["url"])
        print(data["description"][3:-4])
        print("-------------------")