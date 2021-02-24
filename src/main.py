import sys
import threading

import pymysql
from flask import Flask, render_template
from src import mysqlnum, oraclenum, tojson
#声明一个flask
app = Flask(__name__)
@app.route("/numaudit/<host>/<user>/<passwd>/<port>/<schema>/<tablename>")
def numaudit(host,user,passwd,port,schema,tablename):
    ###实例化ORACLE与MYSQL对象
    mysql_element = mysqlnum.MyCheck()
    oracle_element = oraclenum.OrCheck()
    tojson_element = tojson.ToJson()
    mysqlNum = threading.Thread(mysql_element.checkMysqlNum(host=host, user=user, passwd=passwd, port=port, schema=schema,tablename=tablename))
    oracleNum = threading.Thread(oracle_element.checkOracleNum('192.168.177.133', 'SCOTT', 'tiger', tablename))
    mysqlNum.start()
    oraclenum.start()
    NUMCHECK=[]
    i=0
    while i < len(mysqlNum):
        NUM=str(mysqlNum[i])+","+str(oracleNum[i])
        NUMCHECK.append(NUM)
        i=i+1
    NUMCHECK=tojson_element.listToJson(NUMCHECK,tablename)
    return f"{NUMCHECK}"

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=10000)
