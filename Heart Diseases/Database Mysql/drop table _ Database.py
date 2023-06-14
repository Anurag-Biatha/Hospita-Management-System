import mysql.connector as mq

conn=mq.connect(host='localhost',user='root',password='',database='mongo')
mqr='drop database mongos'
mycur=conn.cursor()
if conn.is_connected():
    mycur.execute(mqr)
    print('successfully dropt data base')
else:
    print('Unsuccessfully dropt data base')
mycur.close()
conn.close()