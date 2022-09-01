#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import unittest
import warnings
from common.common import *
from common.configHttp import ConfigHttp
from common.log import MyLog
from testCase.testLogin import Login
from globalCookies import GlobalCookies

logger = MyLog.get_log().logger
configHttp = ConfigHttp()
login = Login()


class Search(unittest.TestCase):
    """查询"""
    def setUp(self):
        logger.info('*****启动testSearch用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_xls("test-data.xlsx","testUserSearch")


    def test_search(self):
        """ globalCookies = GlobalCookies()
        globalCookies.save_cookies()
        cookies = globalCookies.cookies"""

        """查询接口"""
        # 请求参数
        case_data = get_test_data(self.data_list,"testSearch")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        headers =  case_data.get('headers')
        """headers = {'Cookies':cookies}

        print(headers)"""
        logger.info(data)
        logger.info(url)


        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        print("self.url:"+self.url)
        self.data = configHttp.set_data(data)
        self.headers = configHttp.set_data(headers)
        print(configHttp.post())
        res = configHttp.post()


        logger.info(res.url)
        logger.info(res.text)
        """result_json = json.dumps(result)"""
        logger.info(res)
        print(res.text)
        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('查询成功!')
            # 将token设置到configHttp中方便其他类调用
            """configHttp.token['token'] = result_json['data']['token']"""
            pass
        else:
            logger.info('查询失败!')


    def tearDown(self):
        print('*****销毁Search用例*****')

