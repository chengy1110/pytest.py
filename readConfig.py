import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig:
    def __init__(self):
        fd = open(configPath,encoding='UTF-8')
        data = fd.read()

        # 判断是否有BOM文件
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w",encoding='UTF-8')
            #改写文件
            file.write(data)
            file.close()
        fd.close()

        #创建configparser实例
        self.cf = configparser.ConfigParser()
        #读取配置文件
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value