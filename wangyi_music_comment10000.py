# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re,time
import os,json
import base64
from Crypto.Cipher import AES
from pprint import pprint

Default_Header = {
                'Referer':'http://music.163.com/',
                'Host':'music.163.com',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                'Accept-Encoding':'gzip, deflate'
                }

BASE_URL = 'http://music.163.com'

_session = requests.session()
_session.headers.update(Default_Header)

def getPage(pageIndex):
    pageUrl = "http://music.163.com/#/discover/playlist/?order=hot&cat=全部&limit=35&offset=" + pageIndex
    soup = BeautifulSoup(_session.get(pageUrl).content,"html.parser")
    songList = soup.findAll('a',attrs={'class':'tit f-thide s-fc0'})
    for i in songList:
        print(i['href'])
        getPlayList(i['href'])

def getPlayList(playListId):
    playListUrl = BASE_URL + playListId
    soup = BeautifulSoup(_session.get(playListUrl).content,"html.parser")
    songList = soup.find('ul',attrs={'class':'f-hide'})
    for i in songList.findAll('li'):
        startIndex = (i.find('a'))['href']
        songId = startIndex.split('=')[1]
        readEver(songId)

def getSongInfo(songID):
    pass

def aesEncrypt(text,secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext

def rsaEncrypt(text,pubKey,modulus):
    text = text[::-1]
    rs = int(text.encode('hex'),16) ** int(pubKey, 16) % int(modulus,16)
    return format(rs,'x').zfill(256)

def createSecretKey(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:0]), os.urandom(size))))[0:16]

def readEver(songId):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'+str(songId)+'/?csrf_token='
    headers = {'Cookie':'appver=1.5.0.75771;','Referer':'http://music.163.com/'}
    text = {'username':'','password':'','rememberLogin':'true'}
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    nonce = '0CoJUm6Qyw8W8jud'
    pubKey = '010001'
    text = json.dump(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text,nonce),secKey)
    encSecKey = rsaEncrypt(secKey,pubKey,modulus)
    data = {'params':encText,'encSecKey':encSecKey}
    req = requests.post(url,headers=headers,data=data)
    total = req.json()['total']
    if int(total) > 10000:
        print(songId,total)    
    else:
        pass 


if __name__== '__main__':
    for i in range(1,43):
        getPage(str(i*35))
