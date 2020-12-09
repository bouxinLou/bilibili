#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup

from demo.utils import UrlRequest


def get_bilibili():
    """
    查看网页的常规模式：
        1. 打开浏览器输入bilibili网址确认访问
        2. 网络响应后看到bilibili的展示内容

    当前方法和常规模式类似
    访问bilibili主页获取网页内容
        print(get_bilibili())
        # 在Console端打印出常规访问看到的所有内容
    :return: bilibili 主页信息
    """
    bilibili = "https://www.bilibili.com"
    return get_page(bilibili)


def get_page(url, **kwargs):
    return UrlRequest(url, **kwargs).response


if __name__ == '__main__':
    funny = "https://www.bilibili.com/v/life/funny"
    page = get_page(funny, timeout=3)
    print(page)




