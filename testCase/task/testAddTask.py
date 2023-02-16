#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import warnings

from common.commonDataNew import *
from common.configDB import MyDB

from common.configHttp import ConfigHttp
from common.mylog import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()
db = MyDB()

class AddTask(unittest.TestCase):
    """新增任务"""

    def setUp(self):
        logger.info('*****启动testAddTask用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_sheet_data_new("test-data.xlsx","testTask")


    def test_add_task(self):

        """新增任务接口"""
        # 请求参数
        case_data = get_test_data_new(self.data_list,"test_task_01")
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

        """ print(configHttp.post())"""
        res = configHttp.post()


        logger.info(res.url)
        logger.info(res.text)
        """result_json = json.dumps(result)"""
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
       """ self.data_list = get_sheet_data_new("test-data.xlsx","testSearch")
        case_data = get_test_data_new(self.data_list,"test_task_search_07")
        database_name = case_data.get("database_name")
        table_name = case_data.get("table_name")
        sql_id = case_data.get("sql_id")

        sql = db.get_sql(database_name,table_name,sql_id)
        db.executeSQL(sql)
        print('*****销毁Add用例*****')"""

