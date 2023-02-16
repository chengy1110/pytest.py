import requests
import readConfig as readConfig
from common.mylog import MyLog as Log

from globalCookies import GlobalCookies
from testCase.require.deal_yaml import DealYaml

localReadConfig = readConfig.ReadConfig()
dealYaml = DealYaml()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout, cookies
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")



        self.logger = Log.get_log().logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}


    def set_url(self, url):
        self.url =host + url
        return self.url

    def set_headers(self, headers):
        self.headers = headers
        return self.headers

    def set_params(self, params):
        self.params = params
        return self.params

    def set_data(self, data):
        self.data = data
        return self.data

    def set_files(self, file):
        self.files = file
        return self.files


    # defined http get method
    def get(self):
        globalCookies = GlobalCookies()
        cookies = globalCookies.save_cookies()
        try:
            response = requests.session().get(self.url, params=self.params, headers=self.headers, cookies=cookies, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        globalCookies = GlobalCookies()
        cookies = globalCookies.save_cookies()
        try:
            response = requests.session().post(self.url, json=self.data, headers=self.headers,cookies=cookies,files=self.files,timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post01(self):
        cookies = dealYaml.open_yaml()
        try:
           response1 = requests.session().post(self.url, json=self.data, headers=self.headers,cookies=cookies,files=self.files,timeout=float(timeout))
           return response1
        except:
            self.logger.error("请求错误")
            return None