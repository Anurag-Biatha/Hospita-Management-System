import mysql.connector as mq

conn=mq.connect(host='localhost',user='root',password='',database='mongo')
mqr="update student set lname='chaudhary' where id=1"
mycur=conn.cursor()
if conn.is_connected():
    mycur.execute(mqr)
    conn.commit()
    print('successfully updated data !')
else:
    print('Unsuccesfully updated data !')
mycur.close()
conn.close()