# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib2
import os
import time

# 创建文件夹
directory_url = "E:/python"
new_dir = time.strftime("%Y-%m-%d", time.localtime())
dirs = directory_url + '/' + (new_dir.encode('utf-8')) + '/' + (u'星海镖师漫画')
is_exist2 = os.path.exists(dirs)
# 如果文件夹不存在 将创建 文件夹路径
if not is_exist2:
    # 创建路径所有文件夹
    os.makedirs(dirs)

url = "http://www.omanhua.com/comic/3824/"
webdata = requests.get(url)
html = BeautifulSoup(webdata.content, 'lxml')
a_list = html.select("div.subBookList  a")

# s = 124
# while True:
#     if s == 128:
#         break
#     s = s + 1

# a_list = [u'番外篇']
for a in a_list:
    # 创建文件夹
    dir_comic = dirs + '/' + (a["title"])
    # 特殊情况
    # a = str(s) + u'话'
    # dir_comic = dirs + '/' + a
    is_exist2 = os.path.exists(dir_comic)
    # 如果文件夹不存在 将创建 文件夹路径
    if not is_exist2:
        # 创建路径所有文件夹
        os.makedirs(dir_comic)

    i = 0
    # 循环下载直到下一张图片无法访问或被下载
    while True:
        i = i + 1
        if i < 10:
            b = "00" + str(i)
        elif i < 100 and i >= 10:
            b = "0" + str(i)
        # 下载图片
        img_src = (a["title"]).encode("utf-8") + "/" + str(i) + ".jpg"
        # b = str(i)
        # 特殊情况
        # img_src = "/" + b + ".jpg"
        # 此处下载图片
        try:
            content = "http://pic.fxdm.cc/tu/3824/" + urllib2.quote(img_src.encode("utf-8"))  # 将网址中的中文字符转码
            # content = 'http://pic.fxdm.cc/tu/3824/%E7%95%AA%E5%A4%96%E7%AF%87' + img_src
            print(content)
            req = urllib2.Request(content)
            req.add_header("User-Agent",
                           "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36")
            req.add_header("Host", "pic.fxdm.cc")
            req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
            try:
                response = urllib2.urlopen(req, timeout=10)
            except urllib2.URLError, err:
                print(err)
                break
            img = response.read()
            fileName = dir_comic + "/" + str(i) + ".jpg"
            is_exist = os.path.exists(fileName)
            if is_exist:
                continue
            with open(fileName, 'wb') as f:
                f.write(img)
                f.close()
            print(1)
        except Exception, e:
            continue
        time.sleep(0.2)
    print('完成一集')




# 写在最后：因为网站管理员的 文件夹分配或者管理不当 导致某几章无法下载或者 访问失败，
#有几章还是自己 手动到漫画网站中下载，实在毫无规律