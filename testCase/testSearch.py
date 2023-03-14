#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
import warnings
from common.commonData import *
from common.configDB import MyDB
from common.configHttp import ConfigHttp
from common.mylog import MyLog


logger = MyLog.get_log().logger
configHttp = ConfigHttp()

db = MyDB()
getData = GetData()

class Test_Search():
    """数据库查询"""
    def setup(self):
        logger.info('*****启动testSearch用例*****')
        warnings.simplefilter('ignore',ResourceWarning)



    def test_search(self):
        """ globalCookies = GlobalCookies()
        globalCookies.save_cookies()
        cookies = globalCookies.cookies"""
        #从excel中获取数据
        case_data = getData.get_test_data("test_taskForm_search_01")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        database_name = case_data.get('database_name')
        table_name = case_data.get('table_name')
        sql_id = case_data.get('sql_id')

        """查询接口"""

        sql = db.get_sql(database_name,table_name,sql_id)
        #db.connectDB()
        db.executeSQL(sql)
        result = db.get_all(db.cursor)
        print(result)

#因为返回结果是字典与list嵌套形式，所以要分开查找
        """ list01 = data01['dataList']['list']
        print(list01[0]['taskName'])

        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('查询成功!')
            # 将token设置到configHttp中方便其他类调用
            "configHttp.token['token'] = result_json['data']['token']"
            pass
        else:
            logger.info('查询失败!')"""


    def teardown(self):
        print('*****销毁Search用例*****')

