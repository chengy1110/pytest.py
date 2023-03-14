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



class Test_AddChildTask():
    """新增子任务"""
    def setup(self):
        logger.info('*****启动testAddChildTask用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_sheet_data_new("test-data.xlsx","testSearch")
        case_data = get_test_data_new(self.data_list,"test_task_search_08")

        database_name = case_data.get("database_name")
        table_name = case_data.get("table_name")
        sql_id = case_data.get("sql_id")
        sql = db.get_sql(database_name,table_name,sql_id)
        db.executeSQL(sql)



    def test_add_child_task(self):

        """新增子任务接口"""
        # 请求参数
        self.data_list = get_sheet_data_new("test-data.xlsx","testTask")
        case_data = get_test_data_new(self.data_list,"test_task_02")
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


    def teardown(self):
        self.data_list = get_sheet_data_new("test-data.xlsx","testSearch")
        case_data = get_test_data_new(self.data_list,"test_task_search_09")


        #删子任务
        database_name = case_data.get("database_name")
        table_name = case_data.get("table_name")
        sql_id = case_data.get("sql_id")
        sql = db.get_sql(database_name,table_name,sql_id)
        db.executeSQL(sql)

        #删父任务
        case_data01 = get_test_data_new(self.data_list, "test_task_search_10")
        database_name01 = case_data01.get("database_name")
        table_name01 = case_data01.get("table_name")
        sql_id01 = case_data01.get("sql_id")
        sql01 = db.get_sql(database_name01, table_name01, sql_id01)
        db.executeSQL(sql01)

        print('*****销毁Add用例*****')

