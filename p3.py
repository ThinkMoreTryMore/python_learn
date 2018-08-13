# -*- coding:utf-8 -*-

# 下载 1-99页的 电影图片
import os
import urllib
import urllib2
import time
import requests
import datetime
from bs4 import BeautifulSoup

cookie="upv2=20180610%2C2"
header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "cookie": cookie,
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}


def header_build(referer):
    header2 = {
        "Accept":"image/webp,image/*,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "DNT":"1",
        "Host":"img1.xmspc.com",
        "Referer":referer,
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
    }
    return header2

def downImg(movies, url):
    i = 1
    for movie in movies:
        try:
            header2 = header_build(url)
            req = urllib.request.Request(movie["data-original"], headers=header2)
            response = urllib.request.urlopen(req, timeout=5)
            img = response.read()
            with open(dirs+"/"+(movie["alt"])+".jpg") as f:
                f.wrie(img)
            # 下载一次图片就休息一秒
            time.sleep(0.5)
            i+=1
            if i%40==0:
                time.sleep(10)
                print("--中场休息--")
        except Exception as e:
            print((repr(e))+"异常"+str(i/40))
            continue

# 图片存放位置
dirs = "E:/python/2018-06-10/movie_img"
is_exists = os.path.exists(dirs)
if not is_exists:
    os.makedirs(dirs)
    print("创建保存路径")

cout = 1
movies = []
for i in range(1, 30):
    # 电影推荐 第一页
    url = "http://www.id97.com/movie/?page="+str(i)
    webata = requests.get(url, headers=header)
    html = BeautifulSoup(webata.content, 'lxml')
    imgs = html.select("div.movie-item-in a img")
    for movie in imgs:
        movies.append(movie)
        # print(img["alt"])
        try:
            req = urllib2.Request(movie["data-original"])
            req.add_header('Referer', url)
            req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36")
            response = urllib2.urlopen(req, timeout=5)
            # response = urllib.request.urlopen(req, timeout=5)
            img = response.read()
            with open(dirs+"/"+(movie["alt"])+".jpg", 'wb') as f:
                f.write(img)
                f.close()
        except Exception,e:
            print(repr(e))
    time.sleep(0.5)
    cout+=1
    if(cout%5==0):
        time.sleep(0.5)
    if(cout%7==0):
        time.sleep(0.7)
    if(cout%9==0):
        time.sleep(0.9)

print(len(movies)) # 列表大小






