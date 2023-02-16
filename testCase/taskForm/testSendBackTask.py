#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import unittest
import warnings

from common.commonData import *
from common.configHttp import ConfigHttp
from common.mylog import MyLog
from depend_data import DependData

logger = MyLog.get_log().logger
configHttp = ConfigHttp()


class SendBackTask(unittest.TestCase):
    """回退任务工单"""
    def setUp(self):
        logger.info('*****启动testSendBackTask用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        """self.data_list = get_sheet_data_new("test-data.xlsx","testTaskForm")"""


    def test_send_back_task_form(self):

        """新增任务工单接口"""
        dependData = DependData()

        dependData.get_depend_data("test_taskForm_12")
        # 请求参数
        """ case_data = get_test_data_new(self.data_list,"test_taskForm_12")
        if not case_data:
            logger.info("用例不存在")


        # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))

        logger.info(data)
        logger.info(url)


        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        print("self.url:"+self.url)
        self.data =configHttp.set_data(data)
        print(type(self.data))
        self.headers =configHttp.set_headers(headers)

        res = configHttp.post()



        logger.info(res.url)
        logger.info(res.text)
        "result_json = json.dumps(result)"
        logger.info(res)
        print(res.text)
        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('退回成功!')
            pass
        else:
            logger.info('退回失败!')"""


    def tearDown(self):
        print('*****销毁Add用例*****')

