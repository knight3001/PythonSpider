#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103
import random
guess_list = [u"石头", u"剪刀", u"布"]
win_combination = [[u"布", u"石头"], [u"石头", u"剪刀"], [u"剪刀", u"布"]]

while True:
    computer = random.choice(guess_list)
    people = input(u'请输入：石头,剪刀,布\n').strip()
    if people not in guess_list:
        continue
    elif computer == people:
        print(u"平手，再玩一次！")
    elif [computer, people] in win_combination:
        print(u"电脑获胜，再玩，人获胜才能退出！")
    else:
        print(u"人获胜！")
        break
