#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib
import re
import random
import sys
import json
from bs4 import BeautifulSoup
from time import sleep

def main(): 
    url = "https://www.zhihu.com/question/22591304/followers"
    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6,gl;q=0.4,ja;q=0.2,zh-CN;q=0.2,zh-TW;q=0.2',
        'Connection':'keep-alive',
        'Content-Length':'18',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'_za=a5ea7e6d-889c-4c57-bade-d05a25e380e4; _ga=GA1.2.287944439.1450050121; udid="AFAAA7r2lAmPThVqPlTf6QlA5W4j1o3AZIA=|1457500058"; _zap=a6fc3482-7b55-41b6-8415-b6906f09a9c6; d_c0="AEAATnTDoQmPTsxuBBmVxBN4qDbNm3dHzeE=|1461278623"; _xsrf=ba7d52f9b67d8e16f76f83f25faba525; q_c1=a04d6659b09c4daca12a3576bba9bbe5|1468190777000|1439269559000; l_cap_id="ZDE0MDMxNTBhNTIwNDJjZmFlY2Q3NmYwZGQ4M2M0NWE=|1470187099|fe9af7880f66217bcaec37a9a02fd16c55a4a204"; login="MzJhZGU3OTdkZTI4NDQwOTgxZWVhN2ZiM2QyZWNmZWU=|1470187106|81994752bf4631ca2d0c5d514972f76e0d7cd19b"; z_c0=Mi4wQUFCQTVzWWFBQUFBUUFCT2RNT2hDUmNBQUFCaEFsVk5ZdFBJVndDY0RORWJKWXN6dTE2WC1SR1BWN2xkSFdTNkJR|1470187106|248142ebfddfd44c4a0d655024c9a61573ed9b92; n_c=1; s-q=zhouyuan; s-i=2; sid=1b724nno; s-t=autocomplete; cap_id="Y2Y5NTJlZjFmNmRkNGNmZGIzNWEwZGViZjM1ZjEwZTg=|1470291332|a5e9df8c89da73dc59ac673044d65bd02161551b"; a_t="2.0AABA5sYaAAAXAAAAF2_KVwAAQObGGgAAAEAATnTDoQkXAAAAYQJVTWLTyFcAnAzRGyWLM7tel_kRj1e5XR1kugX-sQS9zPiXcjiZlVgJa4JSDNzF3w=="; __utmt=1; __utma=51854390.287944439.1450050121.1470292441.1470291768.3; __utmb=51854390.11.8.1470351045174; __utmc=51854390; __utmz=51854390.1470292441.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20130410=1^3=entry_date=20130410=1',
        'Host':'www.zhihu.com',
        'Origin':'https://www.zhihu.com',
        'Referer':'https://www.zhihu.com/question/22591304/followers',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'X-Xsrftoken':'ba7d52f9b67d8e16f76f83f25faba525'
    }
    i = 1
    for x in range(20,3600,20):
        data={'start':'0',
              'offset':str(x)}
        content=requests.post(url,headers=headers,data=data,timeout=10)
        html = json.loads(content.text)['msg'][1]
        #soup = BeautifulSoup(content.text,'html.parser')
        #imgs = html.find_all("img", class_="zm-item-img-avatar")
        imgs=re.findall('<img src=\"(.*?)_m.jpg',html)
        for img in imgs:
            try:
                img=img.replace('\\','')
                img=img.replace('_m.jpg','.jpg')
                #去掉\字符这个干扰成分
                pic=img+'.jpg'
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

