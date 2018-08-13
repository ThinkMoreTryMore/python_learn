#-*- coding:utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def get_content(url):

    html = urllib.urlopen(url)
    content = html.read()
    html.close()

    return content

def get_images(content):

    oSoup = BeautifulSoup(content)

    all_images = oSoup.find_all('img', class_="BDE_Image")

    x = 1
    for img in all_images:
        print img['src']
        image_name = "%s.jpg" % x

        urllib.urlretrieve(img['src'], image_name)
        x+=1


url = "http://tieba.baidu.com/p/2772656630"

content = get_content(url)

get_images(content)