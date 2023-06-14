import mysql.connector as mq
conn=mq.connect(host='localhost',user='root',password='',database='mongo')
myqr="insert into student(id,fname,lname,gender,address,contact) values(%s,%s,%s,%s,%s,%s)"

val=[ (1,'Basanta','Chaw','M','Kathmandu','9808046983'),
        (2,'Ritu','chaudhary','M','Bakuliya','9808080809'),
        (3,'Indu','Chaudhary','F','Kharsal','98088867787')]
mycur=conn.cursor()
if conn.is_connected():
    mycur.executemany(myqr,val)
    conn.commit()
    print('successfully inserted data !')
else:
    print('Unsuccessfully inserted data !')
mycur.close()
conn.close()