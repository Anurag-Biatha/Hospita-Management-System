import mysql.connector as mq
conn=mq.connect(host='localhost',user='root')
mycursor=conn.cursor()
creates='create database mongos'
if (conn.is_connected()):
    mycursor.execute(creates)
    print('successfully Created Database !')
else:
    print('unsuccessfully Created Database !')
conn.close()