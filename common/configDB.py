import os
from xml.etree import ElementTree
import pymysql
import readConfig as readConfig
from common.mylog import MyLog

proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
localReadConfig = readConfig.ReadConfig()
logger = MyLog.get_log().logger

class MyDB:

    global host, username, password, port, database, config
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):

        self.conn = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.conn = pymysql.connect(**config)
            # create cursor
            self.cursor = self.conn.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            logger.error(str(ex))

    def executeSQL(self, sql):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.conn.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.conn.close()
        print("Database closed!")

    """def __del__(self):  # 析构函数，实例删除时触发
        self.cursor.close()
        self.conn.close()"""

    # 从xml文件中读取sql语句
    database = {}
    def set_xml(self):
        if len(database) == 0:
            sql_path = os.path.join(proDir,"testFile","SQL.xml")
            tree = ElementTree.parse(sql_path)
            #print("tree",tree)
            root = tree.getroot()
            #print("root", root)
            for DB in root.iter("database"):
                db = DB.attrib
                db_name = db.get("name")
                # print(db_name)
                tables = {}
                sql = {}
                for table in DB.findall("table"):
                    for i in range(len(table)):
                        sql[table[i].get("id")] = table[i].text
                    tables[table.get("name")] = sql
                database[db_name] = tables
        return database


    def get_xml_dict(self,database_name, table_name):
        database = self.set_xml()
        database_dict = database.get(database_name).get(table_name)
        return database_dict

    def get_sql(self,database_name, table_name, sql_id):
        db = self.get_xml_dict(database_name, table_name)
        sql = db.get(sql_id)
        print(sql)
        return sql

"""if __name__ == '__main__':
        dd = MyDB()
        dd.get_sql("local_yftx","dp_task_form","selectByTask_name")"""