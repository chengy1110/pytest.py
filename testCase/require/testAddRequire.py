#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import warnings

from common.commonDataNew import *
from common.configHttp import ConfigHttp
from common.mylog import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()

class AddRequire(unittest.TestCase):
    """新增需求"""
    def setUp(self):
        logger.info('*****启动testAddRequire用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_sheet_data_new("test-data.xlsx","testRequire")


    def test_add_require(self):

        """新增需求接口"""
        # 请求参数
        case_data = get_test_data_new(self.data_list,"test_require_01")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))


        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        print("self.url:"+self.url)
        self.data =configHttp.set_data(data)
        print(type(self.data))
        self.headers =configHttp.set_headers(headers)

        res = configHttp.post01()


        logger.info(res)
        print(res.text)
        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('新增成功!')
            pass
        else:
            logger.info('新增失败!')


    def tearDown(self):
        print('*****销毁Add用例*****')

