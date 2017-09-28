#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import json
import os
import sys
from selenium import webdriver

def main(): 
    driver=webdriver.Chrome()                #用chrome浏览器打开
    driver.get("http://www.zhihu.com")       #打开知乎我们要登录
    time.sleep(2)                            #让操作稍微停一下
    driver.find_element_by_link_text('登录').click() #找到‘登录’按钮并点击
    time.sleep(2)
    #找到输入账号的框，并自动输入账号 这里要替换为你的登录账号                              
    driver.find_element_by_name('account').send_keys('knight3001@sina.com') 
    time.sleep(2)
    #密码，这里要替换为你的密码
    driver.find_element_by_name('password').send_keys('sIK4ECPnOcDM1Iu')
    time.sleep(2)
    #输入浏览器中显示的验证码，这里如果知乎让你找烦人的倒立汉字，手动登录一下，再停止程序，退出#浏览器，然后重新启动程序，直到让你输入验证码
    yanzhengma=input('验证码:')
    driver.find_element_by_name('captcha').send_keys(yanzhengma)
    #找到登录按钮，并点击
    driver.find_element_by_css_selector('div.button-wrapper.command > button').click()

    cookie=driver.get_cookies()
    time.sleep(3)
    driver.get('https://www.zhihu.com/question/22591304/followers')
    time.sleep(5)

    execute_times(10)

    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    #print(content)
    imgs=re.findall('<img src=\"(.*?)_m.jpg',content)
    for img in imgs:
        try:
            img=img.replace('\\','')
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

def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


if __name__=='__main__':
    main()

