# coding:utf-8
# 获取qq新闻 首页的标题和网址

# 引入相关模块
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "http://news.qq.com/"
# 请求腾讯新闻的URL，获取其text文本
webdata = requests.get(url)
# webdata.encoding = 'UTF-8'
text = webdata.text
# text = webdata.content.encode('utf-8')
# 对获取到的文本进行解析
soup = BeautifulSoup(text,'lxml')
# print(soup)
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.text > em.f14 > a.linkto")

# 对返回的列表进行遍历
for n in news_titles:
    # 提取出标题和链接信息
    title = n.get_text()
    link = n.get("href")
    data = [
        title,
        link
    ]
    print(data[0])
    print(data[1])
    print(data)