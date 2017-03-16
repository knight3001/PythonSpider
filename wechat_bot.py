#!/usr/bin/env python
# encoding=utf-8
import requests
from wxpy import *
import json


#图灵机器人
def talks_robot(info='你叫什么名字'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '60d96fc905fe4099813c9a18cd225caf'
    data = {'key': apikey, 'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    return replys

#微信自动回复
robot = Bot()
# 回复来自其他好友、群聊和公众号的消息
@robot.register()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talks_robot(info=message)
    return replys

# 开始监听和自动处理消息
robot.start()
