import mysql.connector as mq

conn=mq.connect(host='localhost',user='root',password='',database='mongo')
mqr='select* from student'
mycur=conn.cursor()
if conn.is_connected():
    mycur.execute(mqr)
    for var in mycur:
        print(var)
else:
    print('Unsuccessfully !')
mycur.close()
conn.close()
