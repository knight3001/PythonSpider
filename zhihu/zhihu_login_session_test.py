#!/usr/bin/env python
# encoding=utf-8
# pylint: disable=C0103

import time
import requests
from bs4 import BeautifulSoup

baseURl = 'https://www.zhihu.com/#signin'
loginURL = 'http://www.zhihu.com/login/email'
sampleURL = "https://www.zhihu.com/people/wang-mie-mie-sirius/answers"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Host': 'www.zhihu.com',
}

def kill_captcha(s):
    captchaURL = 'http://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
    with open('captcha.gif', 'wb') as fp:
        captchaREQ = s.get(captchaURL, headers=headers)
        fp.write(captchaREQ.content)
    loginCaptcha = input('input captcha:\n').strip()
    return loginCaptcha

def login(username, password):
    s = requests.session()
    req = s.get(baseURl, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    _xsrf = soup.find('input', attrs={'name': '_xsrf'}).get('value')
    captcha = kill_captcha(s)
    data = {
        '_xsrf': _xsrf,
        'email': username,
        'password': password,
        'captcha': captcha
    }
    resp = s.post(loginURL, headers=headers, data=data).content
    #assert '\u767b\u9646\u6210\u529f' in resp
    return s

if __name__ == '__main__':
    session = login('terry@bneing.com', 'CMJpAGdh01dtryCaDewq')
    soup = BeautifulSoup(session.get(sampleURL, headers=headers).text, "html.parser")
    print(soup)
 