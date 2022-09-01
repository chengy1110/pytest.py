#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import unittest
import warnings

import requests
from common.common import *
from common.configHttp import ConfigHttp
from common.log import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()


class Login(unittest.TestCase):
    """登录"""
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        logger.info('*****启动Login用例*****')
        #读取该sheet页的所有用例数据
        self.data_list = get_xls("test-data.xlsx","testUserLogin")

    def test_login(self):

        """登录456接口"""
        # 请求参数

        case_data = get_test_data(self.data_list,"testLogin")
        if not case_data:
            logger.info("用例不存在")

        # 获取接口路径和请求数据
        url = case_data.get('url')
        data =(case_data.get('data'))

        logger.info(data)
        logger.info(url)

        # 调用configHttp的相关方法，赋值url和data
        url = configHttp.set_url(url)
        print(url)
        data = eval(configHttp.set_data(data))#从excel中获取的数据是str格式，需要转化为字典格式
        print(type(data))

        captcha = self.get_image_code()  # 获取验证码

        #登录请求是302重定向，需要重新写post方法，因为需要设置新的参数allow_redirects=False
        result = requests.session().post(url,data,allow_redirects=False)
        print(result.status_code)

        if result.status_code == 302:
            print(result.headers['Location'])
            url = configHttp.set_url(result.headers['Location'])#获取重定向地址

        print(url)

        # 将获取的cookie转化为字典，并存入全局变量cookies中
        """cookies= requests.utils.dict_from_cookiejar(result.cookies)
        print(cookies)
        logger.info(cookies)"""
        res = requests.session().get(url)#使用新的重定向地址继续访问
        """logger.info(res.text)"""

        # 判断字段是否存在与json中
        if res.status_code == 200:
            logger.info('登录成功!')
            # 将token设置到configHttp中方便其他类调用
            pass
        else:
            logger.info('登录失败!')


    def tearDown(self):
        print('*****销毁Login用例*****')

