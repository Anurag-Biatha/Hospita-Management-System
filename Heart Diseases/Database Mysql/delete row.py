import mysql.connector as mq

conn=mq.connect(host='localhost',user='root',password='',database='mongo')
mqr='delete from student where id=3'
mycur=conn.cursor()
if conn.is_connected():
    mycur.execute(mqr)
    conn.commit()
    print('successfully deleted data !')
else:
    print('Unsuccessfully deleted data !')
mycur.close()
conn.close()