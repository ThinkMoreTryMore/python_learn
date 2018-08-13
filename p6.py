# -*- coding:utf-8 -*-
# 爬取 http://jandan.net/   爬取有趣动态、无聊图、妹子图、段子 
# 因为图片是通过js加载的 所以只做了段子

import requests
from bs4 import BeautifulSoup
import time
import urllib3
import logging

urllib3.disable_warnings()
logging.captureWarnings(True)
cookie = "voted_comment_3801940=1; voted_comment_3801914=1; voted_comment_3801899=1; voted_comment_3800174=1; voted_comment_3801677=1; voted_comment_3800157=1; voted_comment_3800094=1; voted_comment_3801381=1; voted_comment_3800478=1; voted_comment_3800832=1; voted_comment_3801162=1; voted_comment_3800453=1; voted_comment_3800491=1; voted_comment_3800816=1; _ga=GA1.2.1788229895.1524358214; _gid=GA1.2.841366163.1525516486; voted_comment_3802432=1; voted_comment_3802214=1; voted_comment_3802077=1; voted_comment_3802054=1; voted_comment_3801279=1; voted_comment_3802330=1; voted_comment_3801204=1"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Cookie":cookie,
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}

url = "http://jandan.net/"
webdata = requests.get(url, headers=header)
html = BeautifulSoup(webdata.content, 'lxml')

hot_tabs_content = html.select("ul.hot-tabs li")
hot_list_item_content = html.select("div.hot-list-item")

cout = len(hot_tabs_content)
# for i in range(0,1):
#     print(hot_tabs_content[i].text)
#     imgs = hot_list_item_content[0].select(".acv_comment img")
#     # for img in imgs:
#     #     print("http:"+img["src"])
#     print(hot_list_item_content[0])

duanzi_list = hot_list_item_content[2].select(".acv_comment p")
for duanzi in duanzi_list:
    print(duanzi.text)
    print("------------")


# 煎蛋网的加密
# var c=jdKfQaglpwNzNExuUXvK3miqEwtKC1zfrj(e,"sys3G6gNtRmtykzBgHlGJmHotQWdRUlj");
# var k="DECODE";var x=x?x:"";var f=f?f:0;var g=4;x=md5(x);var w=md5(x.substr(0,16));var u=md5(x.substr(16,16));
# if(g){if(k=="DECODE"){var b=md5(microtime());var d=b.length-g;var t=b.substr(d,g)}}
# else{var t=""}var r=w+md5(w+t);var m;if(k=="DECODE"){f=f?f+time():0;tmpstr=f.toString();if(tmpstr.length>=10)
# {n=tmpstr.substr(0,10)+md5(n+u).substr(0,16)+n}else{var e=10-tmpstr.length;for(var p=0;p<e;p++)
# {tmpstr="0"+tmpstr}n=tmpstr+md5(n+u).substr(0,16)+n}m=n}var h=new Array(256);for(var p=0;p<256;p++){h[p]=p}va

