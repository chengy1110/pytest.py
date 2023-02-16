import yaml

class DealYaml:
    def open_yaml(self):
        with open('./testCase/require/data.yaml',encoding='utf-8') as f:
             result = yaml.load(f,Loader=yaml.FullLoader)
             print(result)
             return  result

    def write_yaml(self,data):
        with open('./testCase/require/data.yaml','w',encoding='utf-8') as f:
            yaml.dump(data,stream=f)

    if __name__ == '__main__':
        data = {'123':'abc'}
        write_yaml(data)
