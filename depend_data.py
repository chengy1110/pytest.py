import json



from common.commonData import *
from common.configHttp import ConfigHttp
from common.commonData import GetData
from common.mylog import MyLog

logger = MyLog.get_log().logger
configHttp = ConfigHttp()
getData = GetData()


class DependData:

    def get_depend_data(self, case_id):
        logger.info('*****启动DependData用例*****')
        # 读取case_id的用例数据
        case_data = getData.get_test_data(case_id)
        depend_case_id = case_data.get("depend_case_id")
        depend_case_list = []
        depend_response_list= []
        # 获取用例的所有依赖用例
        if depend_case_id:
            while depend_case_id:
                depend_case_list.append(depend_case_id)
                depend_case_id = (getData.get_test_data(depend_case_id)).get("depend_case_id")
            depend_case_list.reverse()
            print(depend_case_list)
            depend_case_list.append(case_id)
            print(depend_case_list)
            num = len(depend_case_list)

            # 所有依赖用例的返回值list
            march_result_list = []
            # 执行依赖用例和有依赖的用例
            for i in range(num):
                # 获取该caseid的测试用例中依赖case_id
                case_data = getData.get_test_data(depend_case_list[i])
                """depend_case_id = getData.get_depend_case_id(depend_case_list[i])"""
                # 获取该caseid的测试用例中被依赖case所需的参数，并用,分开
                params_key_list = getData.get_request_key(depend_case_list[i])
                if not params_key_list == None:
                    params_key_list = getData.get_request_key(depend_case_list[i]).split(",")

                params = eval(getData.get_request_data(depend_case_list[i]))

                # 判断该caseid的测试用例中case依赖是否为空
                if not params_key_list == None:
                    # 获取上一个依赖接口返回的依赖参数

                    params_data_list = march_result_list[i - 1]
                    # 根据该caseid数据依赖字段构造该接口的传参
                    for k in range(len(params_key_list)):
                        if params_key_list[k] == "taskNumber":
                            params[params_key_list[k]] = (params_data_list[k])[-5:]
                        else:
                            params[params_key_list[k]] = params_data_list[k]
                    method = getData.get_method(depend_case_list[i])
                    if method == 'post':
                        url = case_data.get('url')
                        data = params
                        headers = eval(case_data.get('headers'))

                        self.url = configHttp.set_url(url)
                        self.data = configHttp.set_data(data)
                        self.headers = configHttp.set_headers(headers)
                        result = configHttp.post()
                        #assert result.status_code == 200
                        text1 = result.text
                        print(text1)
                    else:
                        url = case_data.get('url')
                        params = params
                        headers = eval(case_data.get('headers'))

                        self.url = configHttp.set_url(url)
                        self.params = configHttp.set_params(params)
                        self.headers = configHttp.set_headers(headers)
                        result = configHttp.get()
                        #assert result.status_code == 200
                    # 判断该接口是否需要为下一接口返回依赖参数
                    depend_response_data = getData.get_depend_response(depend_case_list[i])
                    if depend_response_data:
                        depend_response_list = depend_response_data.split(",")
                        results = result
                        matchlist = depend_response_list
                        matchparams = getData.match_params(matchlist, results)
                        march_result_list.append(matchparams)
                    else:
                        print("caseid={}不需要返回被依赖的字段".format(depend_case_list[i]))
                        march_result_list.append("依赖字段为空")
                # 当该caseid测试用例中case依赖为空时直接请求该接口，返回匹配到的下一关联接口的请求参数
                else:
                    depend_response_data = getData.get_depend_response(depend_case_list[i])
                    depend_response_list = depend_response_data.split(",")
                    method = getData.get_method(depend_case_list[i])
                    if method == "post":
                        url = case_data.get('url')
                        data = eval(case_data.get('request_data'))
                        headers = eval(case_data.get('headers'))

                        self.url = configHttp.set_url(url)
                        self.data = configHttp.set_data(data)
                        self.headers = configHttp.set_headers(headers)

                        result = configHttp.post()
                        #assert result.status_code == 200
                    else:
                        url = case_data.get('url')
                        params = eval(case_data.get('request_data'))
                        headers = eval(case_data.get('headers'))

                        self.url = configHttp.set_url(url)
                        self.params = configHttp.set_params(params)
                        self.headers = configHttp.set_headers(headers)
                        result1 = (configHttp.get()).text
                        result = json.loads(result1)


                    if depend_response_data:
                        matchparams_all = []
                        results = result
                        matchlist = depend_response_list
                        for i in range(len(matchlist)):
                            matchparams = getData.match_params(matchlist[i], results)
                            matchparams_all.append(matchparams)
                        march_result_list.append(matchparams_all)
                    else:
                        print("caseid={}不需要返回被依赖的字段".format(depend_case_list[i]))
                        march_result_list.append("依赖字段为空")

        return matchparams


"""if __name__ == '__main__':
    dd = DependData()
    dd.get_depend_data("test_taskForm_05")"""
