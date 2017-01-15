#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib
import re
import random
import sys
from bs4 import BeautifulSoup
from time import sleep

def main(): 
    baseurl = "http://bbs.hupu.com/16932807.html"
    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6,gl;q=0.4,ja;q=0.2,zh-CN;q=0.2,zh-TW;q=0.2',
        'Connection':'keep-alive',
        'Content-Length':'17',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'q_c1=47ca86fd1132445280850f1d9e10c45f|1469704271000|1469704271000; l_cap_id="Y2I4M2NhMWQ0MTFlNGJkYzk0OGEzZTI3ZjE5MWQ0NWY=|1469704271|4333db6a0ed3a498c2df3cbaa7041c0c484534eb"; cap_id="YjZiYzQ0YzEyNmE4NDQ0NDlkNGE0NWNiNDIwYmE0YzU=|1469704271|0a4f04b51d827be7be6e6aeeae4c37d509ae9eea"; d_c0="ADBA_I5gTAqPToWeinoOq67gh7YvciRxMOc=|1469704277"; _za=3a0a54a4-822c-405f-b753-a8bcf4dfb6ed; _zap=f7862ed3-c394-4d5b-8941-dc82e5b1c624; z_c0=Mi4wQUFCQTVzWWFBQUFBTUVEOGptQk1DaGNBQUFCaEFsVk5ZblhCVndCbExOZ0JGaGlDZUZ3LTIwSUpqMGg4RVNiN29n|1469704290|95d8bfd59c7a1712544deabd1f65990b9477bb96; a_t="2.0AABA5sYaAAAXAAAAZnXBVwAAQObGGgAAADBA_I5gTAoXAAAAYQJVTWJ1wVcAZSzYARYYgnhcPttCCY9IfBEm-6KjE6XDFj0VD4jo1Q54ukI1B_g8HQ=="; _xsrf=c43a28c8523b1822adcecdf1547f7061; __utmt=1; __utma=51854390.2122209620.1469765569.1470051916.1470053488.6; __utmb=51854390.9.9.1470053519054; __utmc=51854390; __utmz=51854390.1470053488.6.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20130410=1^3=entry_date=20130410=1',
        'Host':'www.zhihu.com',
        'Origin':'https://www.zhihu.com',
        'Referer':'https://www.zhihu.com/question/22591304/followers',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'X-Xsrftoken':'c43a28c8523b1822adcecdf1547f7061'
    }
    i = 1
    for x in range(1,91):
        data={'start':'0',
              'offset':str(x)}
        url = "http://bbs.hupu.com/16932807-"+str(x)+".html"
        content=requests.get(url,timeout=10).text
        soup = BeautifulSoup(content, "html.parser")
        imgs = soup.find_all(class_="headpic")
        #print(imgs)
        
        #imgs=re.findall('<img src=\"(.*?)_m.jpg',content)
        for img in imgs:
            try:
                pic=img.find("img").get("src")
                #img=img.replace('\\','')
                #去掉\字符这个干扰成分
                #pic=img+'.jpg'
                print(pic)
                path='C:\\Users\\Terry\\Downloads\\jpgs\\'+str(i)+'.jpg'
                #声明存储地址及图片名称
                urllib.request.urlretrieve(pic,path)
                #下载图片
                print(u'下载了第'+str(i)+u'张图片')
                
                i+=1
                sleep(random.uniform(0.5,1))
            #睡眠函数用于防止爬取过快被封IP
            except:
                print(u'抓漏1张')
                pass
                sleep(random.uniform(0.5,1))
    

if __name__=='__main__':
    main()

