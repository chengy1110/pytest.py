import yaml

class DealYaml:
    def open_yaml(self):
        with open(r"D:\apache-tomcat-9.0.41\apache-tomcat-9.0.41\webapps\Jenkins\PROJECT\workspace\test_jiekou_project\testCase\require\deal_yaml.py",encoding='utf-8') as f:
             result = yaml.load(f,Loader=yaml.FullLoader)
             print(result)
             return  result

    def write_yaml(self,data):
        with open(r"D:\apache-tomcat-9.0.41\apache-tomcat-9.0.41\webapps\Jenkins\PROJECT\workspace\test_jiekou_project\testCase\require\deal_yaml.py",'w',encoding='utf-8') as f:
            yaml.dump(data,stream=f)

    if __name__ == '__main__':
        data = {'123':'abc'}
        write_yaml(data)
