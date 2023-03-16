#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
import warnings

from common.commonDataNew import *
from common.configDB import MyDB
from common.configHttp import ConfigHttp
from common.mylog import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()
db = MyDB()

class Test_DelTaskForm():
    """删除任务工单"""
    def setup(self):
        logger.info('*****启动testDelTaskForm用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        # 读取该sheet页的所有用例数据
        self.data_list = get_sheet_data_new("test-data.xlsx", "testSearch")
        case_data = get_test_data_new(self.data_list,"test_taskForm_search_05")
        #向数据库中插入数据
        # 接口路径
        database_name = case_data.get('database_name')
        table_name = case_data.get('table_name')
        sql_id = case_data.get('sql_id')

        """数据库中插入数据"""

        sql = db.get_sql(database_name, table_name, sql_id)
        # db.connectDB()
        db.executeSQL(sql)
        #result = db.get_all(db.cursor)
        #print(result)

    def test_del_task_form(self):

        """删除任务工单接口"""
        # 请求参数
        self.data_list = get_sheet_data_new("test-data.xlsx", "testTaskForm")
        case_data = get_test_data_new(self.data_list,"test_taskForm_13")
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
        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('成功!')
            pass
        else:
            logger.info('失败!')


    def teardown(self):
        self.data_list = get_sheet_data_new("test-data.xlsx", "testSearch")
        case_data = get_test_data_new(self.data_list, "test_taskForm_search_06")
        # 在数据库中删除数据
        # 接口路径
        database_name = case_data.get('database_name')
        table_name = case_data.get('table_name')
        sql_id = case_data.get('sql_id')

        """数据库中删除数据"""

        sql = db.get_sql(database_name, table_name, sql_id)
        # db.connectDB()
        db.executeSQL(sql)
        print('*****销毁Add用例*****')

