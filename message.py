# -*- coding:utf-8 -*-
# @Time   :2019/4/24 17:10
# @File   :message.py
# @Author :Vsonli
import tushare as ts
import itchat, time
from itchat.content import TEXT
import datetime

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def earnings(stock_list):
    message = "收益播报：\r\n" + "\n"

    # 获取上证指数
    sh = ts.get_realtime_quotes('sh')
    sh_pro = float(sh.to_dict()['price'][0]) - float(sh.to_dict()['pre_close'][0])
    message += "{}\t{}\t{}\t{}".format("上证指数", str(round(float(sh.to_dict()['price'][0]), 2)), str(round(sh_pro, 3)),
                                       sh.to_dict()['time'][0]) + "\n"
    message += '股票\t\t现价\t买入价\t持仓\t盈亏\n'
    pro_sum = 0.000
    # 遍历股票列表，分割出股票的名称，代码，价格，数量
    for stock in stock_list:
        # 名称
        stock_name = stock.split("_")[0]
        # 代码
        stock_code = stock.split("_")[1]
        # 价格
        stock_price = stock.split("_")[2]
        # 数量
        stock_num = stock.split("_")[3]
        # 通过ts获取股票实时信息
        df = ts.get_realtime_quotes(stock_code)
        # 计算收益
        profit = (float(df['price']) - float(stock_price)) * int(stock_num)
        #print('%.2f'%profit)
        pro_sum += profit
        #print(pro_sum)
        #持仓转字符串,并且判断位数是否少于4为，否则添加一个字符包，输出的时候格式可以统一
        stock_num = str(stock_num)
        if len(stock_num) != 4:
            stock_num = stock_num+' '
        # 写成txt
        str_pro = "{}\t{}\t{}\t{}\t{}".format(stock_name, str(round(float(df.to_dict()['price'][0]), 2)),stock_price,stock_num,
                                          str(round(profit, 4)))
        message += str_pro + "\r\n"
    sh = ts.get_realtime_quotes('sh')
    num = 1
    message += '总盈亏为： ' + str(round(pro_sum, 4))+'\r\n'
    message += '最后更新时间' + nowTime
    return message
stock_list1=['东方财富_300059_20.713_400','宝钢股份_600010_2.021_7000','东方电子_000682_6.336_4500','银星能源_000862_7.717_2000',
             '晨鑫科技_002447_4.560_500','永泰能源_600157_2.706_900','四川金顶_600678_8.530_500','国电电力_600795_2.724_5000']
string1 = earnings(stock_list1)
print(string1)
# itchat.logout()
# itchat.auto_login(hotReload=True)
# users = itchat.search_friends(name='A.宇宙超级无敌可爱咸鱼老大')
# userName = users[0]['UserName']
# itchat.send(string1,toUserName = userName)