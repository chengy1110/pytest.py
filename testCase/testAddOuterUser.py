#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import unittest
import warnings
from ast import literal_eval
import random
from shlex import join

from faker import Faker
import pandas as pd
import regex

from common.commonData import *
from common.configHttp import ConfigHttp
from common.mylog import MyLog


fk= Faker(["zh_CN"])
logger = MyLog.get_log().logger
configHttp = ConfigHttp()

class AddOuterUser(unittest.TestCase):
    """新增外部人员"""
    def setUp(self):
        logger.info('*****启动testAddOuterUser用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_xls("test-data.xlsxx","testUserSearch")

    #随机生成外部人员名字
    def random_outer_name(self):
        value_01=["1","2","3","4", "5","6", "7", "8", "9","0"]
        value_02 = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j","k", "l", "m", "n", "o","p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
        #使用join方法将list转变成字符串
        name = join(random.sample(value_01,2) + random.sample(value_02,3))
        name01 = name.split()# 字符串按空格分割成列表
        new_name = "".join(name01)# 使用一个空字符串合成列表内容生成新的字符串
        print(f"名字:{new_name}")
        return new_name


    def test_add_outer_user(self):

        """新增外部人员接口"""
        # 请求参数
        case_data = get_test_data(self.data_list,"testAddOuterUser")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('data'))
        headers = eval(case_data.get('headers'))

        data['name']= self.random_outer_name()#覆盖excel中的变量${name}
        data['numberPhone'] = fk.phone_number()#faker函数随机生成手机号
        data['area'] = fk.address()#faker函数随机生成地址
        print(data)


        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        print("self.url:"+self.url)
        self.data =configHttp.set_data(data)
        print(type(self.data))
        self.headers =configHttp.set_headers(headers)

        res = configHttp.post()


        logger.info(res.url)
        logger.info(res.text)
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

