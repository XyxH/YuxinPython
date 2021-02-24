import json
import sys
import pymysql
class MyCheck():  # 定义父类
    def checkMysqlNum(self,host,user,passwd,port,schema,tablename):
        result=[]
        db = pymysql.Connect(host=host, user=user, passwd=passwd, port=int(port))
        cursor = db.cursor()
        tablename=tablename.split(',')
        for table in tablename:
            sql = "select count(*) from "+schema+"."+table
            try:
                cursor.execute(sql)
                data = cursor.fetchall()
                data = str(data)[2:-4]
                result.append(data)
            except Exception:
                data = sys.exc_info()
                data="MySQL:"+str(data[1])[5:-1]
                result.append(str(data).replace('\'','').replace(',','').replace('\"',''))
        db.close()
        return result