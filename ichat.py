# -*- coding:utf-8 -*-
# @Time   :2019/4/24 16:48
# @File   :ichat.py
# @Author :Vsonli

import itchat
import time

#登陆二维码
itchat.auto_login(True)
#获取微信好友列表，[1:]代表获取除自己之外的好友
friendList = itchat.get_friends(update=True)[1:]
#对列表的好友发送微信消息
for friend in friendList:
    itchat.send(friend['DisplayName'] or friend['NickName'], friend['UserName'])

    time.sleep(3)  # 隔3s发送一条消息