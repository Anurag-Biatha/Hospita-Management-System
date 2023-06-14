import mysql.connector as mq
conn=mq.connect(host='localhost',user='root',password='')
try:
    if conn.is_connected:
        pass
except IOError:
    print('Unsuccessfully connection !')

else:
    print('Successfully connection !')