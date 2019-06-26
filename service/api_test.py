# -*- coding:utf-8 -*-
# @Time   :2019/6/3 15:10
# @File   :api_test.py
# @Author :Vsonli
import requests
url = 'https://www.xuegean.com/xyxb/userCenter/login'
data1={
    "deviceCode": "481D3629d2d7978388365460dC5F91D2",
    "loginType": 1,
    "networkType":0,
    "smsCode":"081588",
    "userName":"8826"
}
response=requests.post(url,data1)
print(response.text)
r = response.json()['data']['token']



# url='https://www.xuegean.com/xyxb/groupCenter/userGroupList'
# headers = {
#         "Accept-Encoding": 'gzip',
#         "Accept-Language":"zh-CN,zh;q=0.8",
#         "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; JKM-AL00 Build/HUAWEIJKM-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
#         "Cookie":"AUTH-TOKEN=" + r,
#         "Content-Length":16,
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Connection": "Keep-Alive",
#         "Host": "xuegean.com"
#         }
#
# data = {"ts": "1558671736028"}
# resp = requests.post(url,data,headers)
# print(resp.text)
