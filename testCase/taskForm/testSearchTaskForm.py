#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import warnings

from common.commonDataNew import *
from common.configHttp import ConfigHttp
from common.mylog import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()


class SearchTaskForm(unittest.TestCase):
    """查询任务工单"""
    def setUp(self):
        logger.info('*****启动testSearchTaskForm用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        # 读取该sheet页的所有用例数据
        self.data_list = get_sheet_data_new("test-data.xlsx", "testTaskForm")


    def test_search_task_form(self):

        """查询任务工单接口"""
        # 请求参数
        case_data = get_test_data_new(self.data_list,"test_taskForm_03")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        params =eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))

        logger.info(params)
        logger.info(url)


        # 调用configHttp的相关方法

        self.params =configHttp.set_params(params)
        print(type(self.params))
        self.headers =configHttp.set_headers(headers)
        self.url = configHttp.set_url(url)
        print("self.url:" + self.url)


        """ print(configHttp.post())"""
        res = configHttp.get()



        logger.info(res.url)
        logger.info(res.text)
        """result_json = json.dumps(result)"""
        logger.info(res)
        print(res.json())
        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('成功!')
            pass
        else:
            logger.info('失败!')


    def tearDown(self):
        print('*****销毁Add用例*****')

