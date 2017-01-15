# coding:utf-8

import random
guess_list = ["石头", "剪刀", "布"]
win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

while True:
    computer = random.choice(guess_list)
    people = input('请输入：石头,剪刀,布\n').strip()
    if people not in guess_list:
        continue
    elif computer == people:
        print("平手，再玩一次！")
    elif [computer, people] in win_combination:
        print("电脑获胜，再玩，人获胜才能退出！")
    else:
        print("人获胜！")
        break
