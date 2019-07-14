# -*- coding:utf-8 -*-
# @Time   :2019/4/25 14:32
# @File   :newchat.py
# @Author :Vsonli
import itchat
from itchat.content import *
import os
import re
import time
# 文件临时存储页
#rec_tmp_dir = os.path.join(os.getcwd(), 'D:\\Vson\\data')
rec_tmp_dir =  'C:\\itchatData\\'
# 存储数据的字典
rec_msg_dict = {}

# 好友信息监听
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True)
def handle_friend_msg(msg):
    msg_id = msg['MsgId']
    msg_from_user = ''
    try:
        msg_from_user = msg['User']['NickName']
    except :
        msg_from_user = msg['User']
        print(msg_from_user)
    msg_content = ''
    # 收到信息的时间
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M%S", time.localtime())
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']
    if msg['Type'] == 'Text':
        msg_content = msg['Content']
    elif msg['Type'] == 'Picture'\
        or msg['Type'] == 'Recording' \
        or msg['Type'] == 'Video' \
        or msg['Type'] == 'Attachment':
        msg_content = r"" + msg['FileName']
        msg['Text'](rec_tmp_dir + msg['FileName'])
    rec_msg_dict.update({ msg_id: { 'msg_from_user': msg_from_user, 'msg_time_rec': msg_time_rec, 'msg_create_time': msg_create_time, 'msg_type': msg_type, 'msg_content': msg_content } })

    #print(msg)




# 群聊信息监听
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def information(msg):
    msg_id = msg['MsgId']
    msg_from_user = msg['ActualNickName']
    msg_content = ''
    # 收到信息的时间
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M%S", time.localtime())
    msg_create_time = msg['CreateTime']
    msg_type = msg['Type']
    if msg['Type'] == 'Text': msg_content = msg['Content']
    elif msg['Type'] == 'Picture' \
            or msg['Type'] == 'Recording' \
            or msg['Type'] == 'Video' \
            or msg['Type'] == 'Attachment':
        msg_content = r"" + msg['FileName']
        msg['Text'](rec_tmp_dir + msg['FileName'])
    rec_msg_dict.update({ msg_id: { 'msg_from_user': msg_from_user, 'msg_time_rec': msg_time_rec, 'msg_create_time': msg_create_time, 'msg_type': msg_type, 'msg_content': msg_content } })
    if msg_from_user == '体育彩票':
        users = itchat.search_friends(name='Vson')
        userName = users[0]['UserName']
        frined = itchat.search_friends(name='林进新')
        friendName = frined[0]['UserName']
        itchat.send(msg_time_rec + '\n你有新的消息来自用户:' + msg_from_user, toUserName=userName)
        itchat.send(msg_from_user + ':' + msg_content, toUserName=userName)
        itchat.send(msg_time_rec + '\n你有新的消息来自用户:' + msg_from_user, toUserName=friendName)
        itchat.send(msg_from_user + ':' + msg_content, toUserName=friendName)
        #print(msg)


@itchat.msg_register([NOTE], isFriendChat=True, isGroupChat=True)
def revoke_msg(msg):
    users = itchat.search_friends(name='Vson')
    userName = users[0]['UserName']
    if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content']) is not None:
        old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
        old_msg = rec_msg_dict.get(old_msg_id, {})
        print('有人撤回了一条信息：'+ str(old_msg.get('msg_from_user')) + '：' + str(old_msg.get('msg_content')))

        #发送给自己的账号
        string1 = str(old_msg.get('msg_from_user')) + '：' + str(old_msg.get('msg_content'))
        itchat.send(string1, toUserName=userName)

        # 判断文msg_content是否存在，不存在说明可能是
        if os.path.exists( os.path.join(rec_tmp_dir, str( old_msg.get('msg_content'))) ):
            if old_msg.get('msg_type') == 'Picture':
                itchat.send_image(os.path.join(rec_tmp_dir, old_msg.get('msg_content')),
                                    toUserName="filehelper")
                string1 = str(old_msg.get('msg_from_user')) + '：' + str(old_msg.get('msg_content'))
                itchat.send(string1, toUserName=userName)
            elif old_msg.get('msg_type') == 'Video': itchat.send_video(os.path.join(rec_tmp_dir, old_msg.get('msg_content')),
                                  toUserName="filehelper")
            elif old_msg.get('msg_type') == 'Attachment' \
                    or old_msg.get('msg_type') == 'Recording': itchat.send_file(os.path.join(rec_tmp_dir, old_msg.get('msg_content')),
                                 toUserName="filehelper")



if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()