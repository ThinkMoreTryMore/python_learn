# -*- coding:utf-8 -*-
# 查询 1-4的 智联招聘的职位招聘信息 （jl是城市, kw是职位名称, p是页码）

import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def getJobInfo(page):
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B9%96%E5%8D%97&kw=php&p={0}&isadv=0".format(page)
    # print(url)
    webdata = requests.get(url)
    html = BeautifulSoup(webdata.content, 'lxml')

    jobNames = html.select("table.newlist .zwmc a")  # name ( get_text() ) 工作名称
    companyNames = html.select("table.newlist .gsmc a")  # companyName ( get_text() ) 公司名称
    feedbacks = html.select("table.newlist .fk_lv span")  # feedback ( get_text() )  反馈率
    slarys = html.select("table.newlist .zwyx")  # slary ( get_text() )  薪资
    locations = html.select("table.newlist .gzdd")  # location ( get_text() )  公司位置
    job_dutys = html.select("table.newlist .newlist_deatil_last") # job_duty  ( get_text() ) 岗位要求

    jobinfo = []
    for jobName, slary,companyName, location, feedback in zip(jobNames, slarys, companyNames, locations, feedbacks):
        data={
            'jobName': jobName.get_text(),
            'slary': slary.get_text(),
            'companyName': companyName.get_text(),
            'location': location.get_text(),
            'feedback': feedback.get_text()
        }
        print("["+data["jobName"]+"\t"+data["companyName"]+"\t"+data["location"]+"\t"+data["slary"]+"\t"+data["feedback"]+"]")
        jobinfo.append(data)
    return jobinfo

if __name__=='__main__':
    pool = Pool(processes=2)
    pool.map_async(getJobInfo,[1,2,3,4])
    pool.close()
    pool.join()
