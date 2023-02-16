#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import warnings
from time import sleep

from common.commonDataNew import *
from common.configHttp import ConfigHttp
from common.mylog import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()

class AddTaskForm(unittest.TestCase):
    """新增父任务工单"""
    def setUp(self):
        logger.info('*****启动testAddTaskForm用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_sheet_data_new("test-data.xlsx","testTaskForm")

    # 正确新建父任务工单
    def test_add_task_form_01(self):
        """新增任务工单接口"""
        # 请求参数
        case_data = get_test_data_new(self.data_list, "test_taskForm_01")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))

        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        self.data = configHttp.set_data(data)
        self.headers = configHttp.set_headers(headers)
        res = configHttp.post()

        logger.info("test_taskForm_01:" + res.url)
        logger.info("test_taskForm_01:" + res.text)
        logger.info("test_taskForm_01:" + str(res.status_code))
        print("test_taskForm_01:" + res.text)
        print("test_taskForm_01:" + str(res.status_code))

        # 判断字段是否存在与json中
        self.assertEqual(res.status_code,200)
        logger.info('新增父工单成功!')


        # 不传必填项taskName
    def test_add_task_form_02(self):
        '''不传必填项taskName'''
        # 请求参数
        case_data = get_test_data_new(self.data_list, "test_taskForm_02")
        if not case_data:
            logger.info("用例不存在")

            # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))

            # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        self.data = configHttp.set_data(data)
        self.headers = configHttp.set_headers(headers)
        sleep(6)
        res = configHttp.post()


        logger.info("test_taskForm_02:" + res.url)
        logger.info("test_taskForm_02:" + res.text)
        logger.info("test_taskForm_02:" + str(res.status_code))

        self.assertNotEqual(res.status_code,200)
        logger.info('不传必填项taskName:测试成功')

    # 必填项taskName有特殊字符
    def test_add_task_form_03(self):
        '''必填项taskName有特殊字符'''
        # 请求参数
        case_data = get_test_data_new(self.data_list, "test_taskForm_03")
        if not case_data:
            logger.info("用例不存在")

            # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))

            # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        self.data = configHttp.set_data(data)
        self.headers = configHttp.set_headers(headers)
        sleep(6)
        res = configHttp.post()

        logger.info("test_taskForm_03:" + res.url)
        logger.info("test_taskForm_03:" + res.text)
        logger.info("test_taskForm_03:" + str(res.status_code))

        self.assertNotEqual(res.status_code, 200)
        logger.info('必填项taskName有特殊字符:测试成功')


    # 必填项taskName长度超出255字符限制
    def test_add_task_form_04(self):
        '''必填项taskName长度超出255字符限制'''
        # 请求参数
        case_data = get_test_data_new(self.data_list, "test_taskForm_04")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('request_data'))
        headers = eval(case_data.get('headers'))

        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        self.data = configHttp.set_data(data)
        self.headers = configHttp.set_headers(headers)
        sleep(6)
        res = configHttp.post()

        logger.info("test_taskForm_04:" + res.url)
        logger.info("test_taskForm_04:" + res.text)
        logger.info("test_taskForm_04:" + str(res.status_code))

        self.assertNotEqual(res.status_code,200)
        logger.info('必填项taskName长度超出255字符限制:测试成功')




    def tearDown(self):
        print('*****销毁Add用例*****')

