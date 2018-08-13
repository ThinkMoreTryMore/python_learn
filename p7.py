# -*- coding:utf-8 -*-
# https://www.192tt.com

import requests
from bs4 import BeautifulSoup
import time
import os
import urllib
import urllib2

# 创建文件夹
directory_url = "E:/python"
new_dir = time.strftime("%Y-%m-%d", time.localtime())
dirs = directory_url + '/' + str(new_dir) + '/' + (u'美女屋')+ '/' + (u'尤物特')
is_exist2 = os.path.exists(dirs)
# 如果文件夹不存在 将创建 文件夹路径
if not is_exist2:
    # 创建路径所有文件夹
    os.makedirs(dirs)

# 分析网页 获取 1- 5页 网站的地址
img_list_all = []

for i in range(1, 5):
    if i==1:
        url = "https://www.192tt.com/new/ugirlapp/"
    else:
        url="https://www.192tt.com/new/ugirlapp/index_"+str(i)+".html"
    # 解析网页
    webdata = requests.get(url)
    html = BeautifulSoup(webdata.content, 'lxml')
    img_list = html.select(".piclist a img")
    # 将img链接保存
    img_list_all += img_list

print(len(img_list_all))

i=1
for img_html in img_list_all:
    # print(img_html)
    # 下载图片
    try:
        req = urllib2.Request(img_html["lazysrc"])
        # req.add_header('referer', url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36")
        response = urllib2.urlopen(req, timeout=5)
        img = response.read()
        fileName = dirs+"/"+ img_html["alt"] +".jpg"
        is_exist = os.path.exists(fileName)
        if is_exist:
            continue
        with open(fileName, 'wb') as f:
            f.write(img)
            f.close()
        i+=1
    except Exception, e:
        print(repr(e))
    time.sleep(0.2)
time.sleep(1)
print("下载结束")