# -*- coding:utf-8 -*-
# @Time   :2019/4/24 17:10
# @File   :message.py
# @Author :Vsonli
import requests
from bs4 import BeautifulSoup
import os
import re, random

Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def get_page_name(url):  # 获得图集最大页数和名称
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('span')
    title = soup.find('h2', class_="main-title")
    return span[10].text, title.text


def get_html(url):  # 获得页面html代码
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    try:
        req = requests.get(url, headers=Hostreferer, proxies=proxies)
    except:
        get_html(url)
    html = req.text
    return html


def get_img_url(url, name):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find('img', alt=name)
    return img_url['src']


def save_img(img_url, count, name):
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    try:
        req = requests.get(img_url, headers=Picreferer, proxies=proxies)
    except:
        save_img(img_url, count, name)
    new_name = rename(name)
    with open(new_name + '/' + str(count) + '.jpg', 'wb') as f:
        f.write(req.content)


def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name


def save_one_atlas(old_url):
    page, name = get_page_name(old_url)
    new_name = rename(name)
    os.mkdir(new_name)

    print("图集--" + name + "--开始保存")
    for i in range(1, 9):
        url = old_url + "/" + str(i)
        img_url = get_img_url(url, name)
        # print(img_url)
        save_img(img_url, i, name)
        print('正在保存第' + str(i) + '张图片')
    print("图集--" + name + "保存成功")


def get_atlas_list(url):
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    try:
        req = requests.get(url, headers=Hostreferer, proxies=proxies)
    except:
        get_atlas_list(url)
    soup = BeautifulSoup(req.text, 'lxml')
    atlas = soup.find_all(attrs={'class': 'lazy'})
    atlas_list = []
    for atla in atlas:
        atlas_list.append(atla.parent['href'])
    return atlas_list


def save_one_page(start_url):
    atlas_url = get_atlas_list(start_url)
    for url in atlas_url:
        save_one_atlas(url)


if __name__ == '__main__':
    start_url = "http://www.mzitu.com/"
    for count in range(1, 3):
        url = start_url + "page/" + str(count) + "/"
        save_one_page(url)
    print("爬取完成")