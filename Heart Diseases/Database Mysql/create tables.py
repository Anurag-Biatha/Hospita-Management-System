import mysql.connector as mq
conn=mq.connect(host='localhost',user='root',password='',database='mongo')
mycur=conn.cursor()
myquery=('''
create table student(
    id int not null,
    fname varchar(20) not null,
    lname varchar(20) not null,
    gender varchar(1) not null,
    address varchar(20) not null,
    contact varchar(20) not null
    
)
''')
if conn.is_connected():
    mycur.execute(myquery)
    conn.commit()
    print('successfully created tables !')
else:
    print('unsuccessfully create tables !')
mycur.close()
conn.close()