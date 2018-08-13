#-*- coding:utf-8 -*-

# 创建以日期为文件夹
# 下载 NASA 每日图片
import os
import time
import urllib
import requests
from bs4 import BeautifulSoup

directory_url = "E:/python"

new_dir = time.strftime("%Y-%m-%d", time.localtime())
dirs = directory_url+'/'+new_dir
is_exist = os.path.exists(directory_url)
is_exist2 = os.path.exists(dirs)
# 如果文件夹不存在 将创建 文件夹路径
if not is_exist2:
    os.makedirs(dirs)

#NASA 每日图片
nasa_url = "https://apod.nasa.gov/apod/astropix.html"
webdata = requests.get(nasa_url)
html = BeautifulSoup(webdata.content, 'lxml')

img_url = html.select("a")[1]["href"]
img_url = "https://apod.nasa.gov/apod/"+img_url
# img_url="https://apod.nasa.gov/apod/image/1806/ViaLacteaconMarte_c0.jpg"
urllib.urlretrieve(img_url, dirs+"/NASA_universe_Img.jpg")
print("下载完成")

