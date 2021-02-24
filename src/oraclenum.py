import json
import sys
import cx_Oracle
class OrCheck():
    def checkOracleNum(self,host,user,passwd,tablename):
        jsonList=[]
        result=[]
        connparameter=host+'/'+"orcl.localdomain"
        db = cx_Oracle.connect(user,passwd,connparameter)  # 连接数据库
        cursor = db.cursor()  # 获取cursor
        tablename = tablename.split(',')
        for table in tablename:
            sql = 'select /*+ parallel(4) */  count(*) from ' +user+'.'+table
            try:
                results=cursor.execute(sql)
                data = results.fetchone()  # 获取结果集
                data = str(data)[1:-2]
                result.append(data)
            except Exception:
                data = sys.exc_info()
                data=data[1]
                result.append(str(data))
        db.close()
        return result
