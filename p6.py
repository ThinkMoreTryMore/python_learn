# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import os
import urllib
import urllib2

# 创建文件夹
directory_url = "E:/python"
new_dir = time.strftime("%Y-%m-%d", time.localtime())
dirs = directory_url + '/' + str(new_dir) + '/' + (u'bt之家')
is_exist2 = os.path.exists(dirs)
# 如果文件夹不存在 将创建 文件夹路径
if not is_exist2:
    # 创建路径所有文件夹
    os.makedirs(dirs)

# 分析网页 获取 1- 5页 网站的地址
a_list_all = []

for i in range(2, 5):
    url = "http://www.btbtt33.com/forum-index-fid-8-page-"+str(i)+".htm"

    # 解析网页
    webdata = requests.get(url)
    html = BeautifulSoup(webdata.content, 'lxml')
    # 获取 当前页面所有文章的a链接
    a_list = html.select("td.subject a.subject_link")
    # 将a链接保存
    a_list_all += a_list

print(len(a_list_all))

# 进入网页
for html_a in a_list_all:
# html_a = a_list_all[5]
    print(html_a)
    dirs1= dirs +'/' + (u'' + (html_a.text))
    is_exist3 = os.path.exists(dirs1)
    if not is_exist3:
        os.makedirs(dirs1)

    url = str(html_a["href"])
    # 解析网页
    webdata = requests.get(url)
    html = BeautifulSoup(webdata.content, 'lxml')
    img_htmls = html.select(".message img")
    i =  1
    for img_html in img_htmls:
        # print(img_html)
        # 下载图片
        try:
            req = urllib2.Request(img_html["src"])
            req.add_header('referer', url)
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36")
            response = urllib2.urlopen(req, timeout=5)
            img = response.read()
            fileName = dirs1+"/"+ str(i) +".jpg"
            is_exist = os.path.exists(fileName)
            if is_exist:
                continue
            with open(fileName, 'wb') as f:
                f.write(img)
                f.close()
            i+=1
        except Exception, e:
            print(repr(e))
        time.sleep(0.5)
    time.sleep(1)