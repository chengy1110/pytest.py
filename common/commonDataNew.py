import os

import xlrd

from common import configHttp
import readConfig as readConfig
from common.mylog import MyLog
from readConfig import proDir
from xlutils.copy import copy

localConfigHttp = configHttp.ConfigHttp()
logger = MyLog.get_log().logger
localReadConfig = readConfig.ReadConfig()

# 从excel文件中读取测试用例

def get_sheet_data_new(xls_name,sheet_name):
        data_list  = []
        xlsPath = os.path.join(proDir, "testFile", xls_name)
        # 将excel进行实例化
        book = xlrd.open_workbook(xlsPath)
        # 通过name值进行读取sheet
        sheet = book.sheet_by_name(sheet_name)
        # 获取列表的总数
        nrows = sheet.nrows
        # 循环读取每行数据
        for i in range(1, nrows):
        # 通过每行进行读取数据
        # print(sheet.row_values(i))
        # 讲数据通过组合成dic+t格式
            d = dict(zip(sheet.row_values(0), sheet.row_values(i)))
            data_list.append(d)
        return data_list

def get_test_data_new(data_list, case_id):
        for case_data in data_list:
            if case_id == case_data["case_id"]:  # 如果字典数据中case_id与参数一致
                return case_data
        # 如果查询不到会返回None

# 向某个单元格写入数据
def write_value_new(i, row, col, value):
        xlsPath = os.path.join(proDir, "testFile", "test-data.xlsx")
        # open xls file
        data = xlrd.open_workbook(xlsPath)  # 打开文件
        data_copy = copy(data)  # 复制原文件
        sheet = data_copy.get_sheet(i) # 取得复制文件的sheet对象
        sheet.write(row, col, value)  # 在某一单元格写入value
        data_copy.save(xlsPath)  # 保存文件