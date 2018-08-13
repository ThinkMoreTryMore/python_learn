# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import os
import urllib
import urllib2

url = "https://www.nvshens.com/rank/"
# 分析网页 获取图片地址
webdata = requests.get(url)
html = BeautifulSoup(webdata.content, 'lxml')

# 创建文件夹
directory_url = "E:/python"
new_dir = time.strftime("%Y-%m-%d", time.localtime())
dirs = directory_url+'/'+str(new_dir)+'/'+(u'排行榜')
is_exist2 = os.path.exists(dirs)
# 如果文件夹不存在 将创建 文件夹路径
if not is_exist2:
    # 创建路径所有文件夹
    os.makedirs(dirs)

# 该项目p4 可以使用pro2 项目的p9 直接使用 许诺Sabrina		https://www.nvshens.com//girl/18879/ 需要将 18879 取出
name="https://www.nvshens.com"
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
        model_img = str("https://img.onvshen.com:85")+str(modelLink)+model_a[2]+".jpg"
        if (i == 0):
            modelName = modelInfo_list[i].select("div.first_girlli_div_rank h3")[0]
        else:
            modelName = modelInfo_list[i].select("a")[0]
        print(modelName.text+"\t\t"+str(name)+str(modelLink))

        # 下载图片
        try:
            req = urllib2.Request(model_img)
            req.add_header('Host', "img.onvshen.com:85")
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36")
            req.add_header("Referer", str(name)+str(modelLink))
            response = urllib2.urlopen(req, timeout=5)
            img = response.read()
            file = dirs+"/"+modelName.text+".jpg"
            # 假如已经下载有 那么进入下一个下载
            is_exist = os.path.exists(file)
            if is_exist:
                continue
            with open(dirs+"/"+modelName.text+".jpg", 'wb') as f:
                f.write(img)
                f.close()
        except Exception,e:
            print(repr(e))
        time.sleep(1)
