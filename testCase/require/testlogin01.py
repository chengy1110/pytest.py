import unittest

import requests


from common.commonDataNew import *
from globalCookies import GlobalCookies
from testCase.require.deal_yaml import DealYaml

globalCookies = GlobalCookies()
dealYaml = DealYaml()

class Login01(unittest.TestCase):

    def setUp(self):
        self.datalist = get_sheet_data_new("test-data.xlsx","testUserLogin")
        print(self.datalist)

    def testlogin(self):
        case_data = get_test_data_new(self.datalist, "test_login_01")
        data = eval(case_data.get("request_data"))

        data['captcha'] = globalCookies.get_image_code()
        print(data)
        headers = case_data.get("headers")
        url = case_data.get("url")
        res = requests.post(url,data,headers,allow_redirects=False)
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        print(cookies)
        dealYaml.write_yaml(cookies)


    def tearDown(self):
        print("111111111")
