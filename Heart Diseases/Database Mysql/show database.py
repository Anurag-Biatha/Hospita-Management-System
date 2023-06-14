import mysql.connector as mq

conn=mq.connect(host='localhost',user='root',password='')
query='show databases'
curObj=conn.cursor()
if conn.is_connected():
    curObj.execute(query)
    for var in curObj:
        print(var)
else:
    print('Unsuccessfully ')
conn.close()