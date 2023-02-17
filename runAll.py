import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append("D:\\apache-tomcat-9.0.41\\apache-tomcat-9.0.41\\webapps\\NEW_jenkins\\workspace\\test-jiekou-project\\venv\\Lib\\site-packages")
import unittest
import HTMLTestRunner
import time
from common.mylog import MyLog
import readConfig
from common.configEmail import Email


logger = MyLog.get_log().logger
myConfig = readConfig.ReadConfig()


class Runner:

    def __init__(self):

        self.caseList = []
        pass

    def set_case_list(self):
        caselist_file = os.path.join(readConfig.proDir, 'caselist.txt')
        fb = open(caselist_file,'r')
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))


    def set_case_suite(self):
        self.set_case_list()
        #创建测试套件
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caseList:
            case_file = os.path.join(readConfig.proDir, "./testCase")
            print("文件夹名称"+case_file)
            #根据/分割文件夹、文件名
            case_name = case.split("/")[-1]
            print("用例名称"+case_name+".py")
            discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
            suite_model.append(discover)


        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
                    print("名称" + str(test_name))
        else:
            return None
        return test_suite

    def run(self):
        flag = 0
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********开始测试********")
                date = time.strftime('%Y%m%d-%H%M%S', time.localtime())
                fp = open((os.path.join(readConfig.proDir, "result", date + '_test.html')), 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试描述')
                runner.run(suit)
                flag = 1
            else:
                logger.info("没有测试用例")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********测试结束*********")
            # send test report by email
            on_off = myConfig.get_email('on_off')
            if int(on_off) == 1 and flag == 1:
                Email().send_email()
                logger.info('已发送邮件')
            elif int(on_off) == 0:
                logger.info("未发送邮件给开发")
            else:
               logger.info("不知道的状态")

if __name__ == '__main__':
    Runner().run()