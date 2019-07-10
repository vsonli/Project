# -*- coding:utf-8 -*-
# @Time   :2019/6/27 18:55
# @File   :qiantu.py
# @Author :Vsonli
import urllib.request
import re

for i in range(0,20):
    print('------------go---------------')
    url = 'https://www.58pic.com/piccate/11-198-874-p'+str(i)+'.html'
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    pat = 'data-original="(.*?)"'
    links = re.compile(pat,re.S).findall(data)
    print(links)
    for j in range(len(links)):
        link = links[j].replace("!qt324","")
        file = 'D:/photo/'+str(i)+str(j)+'.jpg'
        urllib.request.urlretrieve(link,filename=file)
        print('pass')
'''
['//preview.qiantucdn.com/58picmark/original_origin_pic/33/68/75/76n58PICF54358PICa8fifhdeMaRk.pngnew_nowater', 
'//preview.qiantucdn.com/58pic/17/84/37/4358PIC58PICJfXcfm86afbF4_PIC2018.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/33/46/11/auto_93Y58PICeiaJbB81Fnf4f_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58picmark/element_origin_pic/34/91/40/60z58PICet626NUN58PICes6wMaRk.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/51/91/auto_10a58PICP25x6K7xrGDXM_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/44/25/auto_158PIC058PICd58PIChYhd538BY6I_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/43/37/auto_8158PIC58PIC00Z73cb0FZ9Pw_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/48/61/75X58PICJ2Nay636r3N8g_PIC2018.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/28/80/80/auto_06F58PICcgc6JfXE521bi_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/35/00/24/54E58PIC44f36258PICucpYdP_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/64/76/auto_95E58PICe4VF4Y5PY7r75_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/33/46/23/auto_87958PICSttuAjqk6x0Vn_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/15/14/10/05458PIC4JbF067dW1td5_PIC2018.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/28/78/54/auto_29H58PICC5chU0GPnhM4c_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/28/33/72/58PIC4I58PIC5946758PICveq3zgF_PIC2018.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/16/57/63/66058PIC5d7v02uDV87fd_PIC2018.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/28/70/26/42V58PIC38czDec958PICHNzi_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/42/32/auto_55f58PICuj858PICdawq7khnR_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/28/85/63/10c58PICeg989dkS8ndE1_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/33/20/42/auto_69q58PICXff458PIC5hTUN0u6_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/44/01/auto_5358PIC58PIC3k91d0ehj8f58PICB_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/28/85/68/89H58PICysyqdBdKz2GSa_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/33/19/39/auto_79V58PIC1Iq2aDC7ft44N_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/61/51/auto_37c58PICC1nP34sba62AM_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/33/43/71/auto_92v58PICaueHtfgB0611a_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58picmark/original_origin_pic/33/68/78/15Y58PIC7BBuY58PICEI22b958PICMaRk.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/46/91/auto_46f58PIC1EV8zY8IVXY8P_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58pic/32/78/34/auto_87Q58PIC41Tx49quGbRdf_PIC2018.jpg!qt324new_nowater', '//preview.qiantucdn.com/58picmark/original_origin_pic/33/68/66/34u58PIC9h5yiDe4ff5P5MaRk.png!qt324new_nowater', '//preview.qiantucdn.com/58pic/26/53/77/3658PIC58PICtvr5a708db8Je_PIC2018.png!qt324new_nowater']

'''