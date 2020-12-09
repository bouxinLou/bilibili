#!/usr/bin/env python
# coding: utf-8
import requests


class UrlRequest:
    """
    这是对Python requests类库的一个简单封装
    以便于使用
    """
    def __init__(self, url, method="GET", body=None, proxy=False, **kwargs):
        self.url = url
        self.method = method
        self.request_body = body
        self.proxy = proxy
        self.response = None
        self._switcher(**kwargs)

    def _switcher(self, **kwargs):
        method = self.method
        if method == "GET":
            self.__do_get__(**kwargs)
        elif method == "POST":
            self.__do_post__(**kwargs)
        else:
            pass

    def __do_get__(self, **kwargs):
        try:
            # 真正开始用requests类库发起网络请求
            response = requests.get(self.url, **kwargs)
            self.response = response.text
        except RuntimeError as e:
            raise e

    def __do_post__(self, **kwargs):
        pass








