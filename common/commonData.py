import os
#from xlrd import open_workbook
from xlutils.copy import copy

import xlrd
from xml.etree import ElementTree as ElementTree
from jsonpath_rw import jsonpath,parse
from common import configHttp
import readConfig as readConfig
from common.mylog import MyLog
from readConfig import proDir


localConfigHttp = configHttp.ConfigHttp()
logger = MyLog.get_log().logger
localReadConfig = readConfig.ReadConfig()

# 从excel文件中读取测试用例
class GetData:

    def get_test_data(self, case_id):
        xls_name = localReadConfig.get_excel("xls_name")
        sheet_name = localReadConfig.get_excel("sheet_name")
        # get xls file's path
        xlsPath = os.path.join(proDir, "testFile", xls_name)
        # open xls file
        file = xlrd.open_workbook(xlsPath)
        data_list = []
        # get sheet by name
        sheet = file.sheet_by_name(sheet_name)
        header = sheet.row_values(0)  # 获取标题行数据
        # get one sheet's rows
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                d = dict(zip(header, sheet.row_values(i)))
                data_list.append(d)

        for case_data in data_list:
            # 如果字典数据中case_id与参数一致
            if case_id == case_data["case_id"]:
                return case_data
     # 如果查询不到会返回None


    #获取
    def get_depend_key(self,case_id):
        case_data = self.get_test_data(case_id)
        if case_data.get("depend_case_id"):
            depend_key = case_data.get("depend_case_id")
            if depend_key:
                return depend_key
            else:
                logger.info("get_depend_case_id为空:"+case_id)

        else:
            logger.info("get_depend_case_id有点问题:"+case_id)

    def get_request_key(self,case_id):
        case_data = self.get_test_data(case_id)
        if case_data.get("request_key"):
            request_key = case_data.get("request_key")
            if request_key:
                return request_key
            else:
                logger.info("get_request_key为空:"+case_id)
        else:
            logger.info("get_request_key有点问题:"+case_id)

    def get_depend_response(self,case_id):
        case_data = self.get_test_data(case_id)
        if case_data.get("depend_response"):
            depend_response = case_data.get("depend_response")
            if depend_response:
                return  depend_response
            else:
                logger.info("get_depend_response为空:"+case_id)
        else:
            logger.info("get_depend_response有点问题:"+case_id)
            return ""


    def get_request_data(self,case_id):
        case_data = self.get_test_data(case_id)
        if case_data.get("request_data"):
            request_data = case_data.get("request_data")
            return  request_data
        else:
            logger.info("get_request_data有点问题:"+case_id)

    def get_depend_case_id(self,case_id):
        case_data = self.get_test_data(case_id)
        if case_data.get("depend_case_id"):
            depend_case_id = case_data.get("depend_case_id")
            return  depend_case_id
        else:
            logger.info("get_depend_case_id有点问题:"+case_id)

    def match_params(self,depenData,responseData):
        jsonExe = parse(depenData)  # parse用于从一个字符串中解析出json对象
        madle = jsonExe.find(responseData) # 按parse()中给定的结构格式，在responseData当中自动查找符合这个结构格式的值
        try:
             return [math.value for math in madle][0] # 返回需要的值
        except IndexError as e :
            logger.error("IndexError: list index out of range,我也不知道为啥就报错了,绝对不是BUG"
                                   "八成是你的jsonPath写错了")

    def get_method(self,case_id):
        case_data = self.get_test_data(case_id)
        method = case_data.get("method")
        return method


 # 向某个单元格写入数据
    def write_value(self,sheet_name, row, col, value):
        xlsPath = os.path.join(proDir, "testFile", "test_data.xlsx")
        # open xls file
        data = xlrd.open_workbook(xlsPath)  # 打开文件
        data_copy = copy(data)  # 复制原文件
        sheet = data_copy.sheet_by_name(sheet_name) # 取得复制文件的sheet对象
        sheet.write(row, col, value)  # 在某一单元格写入value
        data_copy.save(xlsPath)  # 保存文件