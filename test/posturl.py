# -*- coding:utf-8 -*-
# @Time   :2019/5/27 20:04
# @File   :posturl.py
# @Author :Vsonli


import requests
from bs4 import BeautifulSoup #注释1
from PIL import Image #注释2
import os,re
from io import BytesIO #注释3
import time

url = "https://www.zcool.com.cn/work/ZMzU1NTUzOTY=/1.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

'''通过向目标服务器进行请求后获得的响应对象，它作为一个对象，包含了服务器的响应的全部内容'''
response = requests.get(url, headers=headers)

'''
BeautifulSoup：网页抓取数据的驱动
    第一个参数是HTML代码对象，比如这里content存储了URL为” http://www.yestone.com/gallery/1501754333627“的这张网页的HTML代码，它是个字符串或者是一个文件句柄
    二个参数是HTML解析器可以使用内置标准的html.parser，也可以使用第三方的，比如lxml和html5lib'''
soup = BeautifulSoup(response.content, 'html.parser')

'''
传入两个参数，第一个是HTML文档的节点名，也可以理解为HTML的标签名；第二个则是该节点的class类名
比如上面代码中，我要找出该网页上所有的img节点，且我需要的img节点的类名为”no-right-key”
如果没有class类名的HTML元素：img_list = soup.find_all(name=‘img’, attrs={‘class’: ‘height_min’})
'''
items = soup.find_all('img', class_='no-right-key') #注释7
#定义一个相对路径，定义了一个和运行代码同一个文件夹下的名为photo的文件夹
folder_path = './photo'#注释8
if os.path.exists(folder_path) == False:
   os.makedirs(folder_path)
for index, item in enumerate(items):
    if item:
        url = item.get('data-src')
        if url != None:
            '''截取到@之前的链接，为高清版'''
            url = url[:-22]
            html = requests.get(url)
            img_name = folder_path + str(index+1) + '.png' #定义了一个文件名
            '''读取并将数据写入指定文件夹下的函数'''
            image = Image.open(BytesIO(html.content))
            image.save('D:\photo'+img_name)

            print('第%d张图片下载完成' % (index + 1))
            time.sleep(1)  # 自定义延时
            print('抓取完成')
