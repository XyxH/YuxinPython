import time
from flask import Flask, render_template
from src import mysqlnum, oraclenum, tojson
from src.mythread import MyThread
#声明一个flask
app = Flask(__name__)
@app.route("/numaudit/<host>/<user>/<passwd>/<port>/<schema>/<tablename>")
def numaudit(host,user,passwd,port,schema,tablename):
    ###实例化ORACLE与MYSQL对象，同时实例化tojson对象
    start_time=time.time()#开始时间
    mysql_element = mysqlnum.MyCheck()
    oracle_element = oraclenum.OrCheck()
    tojson_element = tojson.ToJson()
    ##生成两个线程t1,t2查询数据库
    thread1 = MyThread(mysql_element.checkMysqlNum,args=(host, user, passwd, port, schema,tablename))
    thread2= MyThread(oracle_element.checkOracleNum,args=('192.168.177.133', 'SCOTT', 'tiger', tablename))
    ##启动两个线程
    thread1.start();thread2.start();thread1.join();thread2.join()
    mysqlNum=thread1.get_result();oracleNum=thread2.get_result()
    NUMCHECK=[]
    i=0
    while i < len(mysqlNum):
        NUM=str(mysqlNum[i])+","+str(oracleNum[i])
        NUMCHECK.append(NUM)
        i=i+1
    NUMCHECK=tojson_element.listToJson(NUMCHECK,tablename)
    end_time = time.time()#结束时间
    total_time=end_time-start_time
    print("总计耗时："+str(total_time))
    return f"{NUMCHECK}"
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=10000)
