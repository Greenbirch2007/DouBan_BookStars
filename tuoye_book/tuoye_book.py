

#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

from selenium import webdriver

driver = webdriver.Chrome()

def get_one_page(url):

    driver.get(url)
    html = driver.page_source
    return html


def next_page():
    for i in range(1,139):  # 有一个翻页小技巧
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/a[last()]').click()
        html = driver.page_source
        return html

def parse_page(html):
    selector = etree.HTML(html)
    title = selector.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a/text()')
    stars = selector.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/span[2]/text()')
    conments_Num = selector.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/span[3]/text()')

    for i1,i2,i3 in zip(title,stars,conments_Num):
        big_list.append((i1,i2,i3))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='DouBan_BookStars',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into tuoye_book (title,stars,conments_Num) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    url = 'https://book.douban.com/subject_search?search_text=%E6%89%98%E4%B8%9A&cat=1001'
    time.sleep(1)
    html = get_one_page(url)
    content = parse_page(html)
    insertDB(content)
    while True:
        time.sleep(1)
        html = next_page()
        time.sleep(1)

        content = parse_page(html)
        insertDB(content)
        print(datetime.datetime.now())

#
# create table tuoye_book(
# id int not null primary key auto_increment,
# title text,
# stars varchar(10),
# conments_Num text
# ) engine=InnoDB  charset=utf8;


# drop  table tuoye_book;



