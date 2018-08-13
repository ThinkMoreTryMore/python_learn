# -*- coding:utf-8 -*-
# 查询 书格的最近更新的文化信息

# 放弃 原因1: 网页结构混乱 2. 选择难以定位

import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def getNewBook(page):
    url = "https://shuge.org/ebooks/renew/page/{0}/".format(page)
    print(url)
    webdata = requests.get(url)
    html = BeautifulSoup(webdata.content, 'lxml')
    # print(html)

    bookNames = html.select(".ebook .column-last h3 a")
    chats = html.select(".ebook .fulldetails p.smalldetails a")
    bookDetails = html.select(".ebook .column-last p")

    for bookName, bookDetail, chat in zip(bookNames, bookDetails, chats):
        print(bookName.get_text()+"\t"+bookDetail.get_text())
        print("************")
        # print(bookDetail.get_text())

if __name__=='__main__':
    pool = Pool(processes=2)
    pool.map_async(getNewBook,[2,3,4])
    pool.close()
    pool.join()
