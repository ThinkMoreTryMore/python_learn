# -*- coding:utf-8 -*-
# 获取今日头条的文章

import requests
import urllib
import chardet

url = "https://www.toutiao.com/a6546514256588702215/"
code = chardet.detect(urllib.urlopen(url).read() )
print(code["encoding"])

cookies = 'tt_webid=6547133348094494215; sso_login_status=0; tt_webid=6547133348094494215; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=kw2tx5pxj1524379477306; tt_webid=6547133348094494215'

headers = {

    # "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # "referer":"https://www.toutiao.com/",
    # "cookie": cookies,
    "user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
}
html = requests.get(url, headers=headers)
# soup = BeautifulSoup(html.text, 'lxml')
# data = json.loads(html.content)
# news = data['data']['pc_feed_focus']

print(html.content)
# print(soup)
# print(data)
# print(news)
# urls = []
# for n in news:
#     title = n['title']
#     img_url = n['image_url']
#     url = n['media_url']
#     urls.append(url)
#     # print(url)
#     print(url, title, img_url)
#
# print(urls)