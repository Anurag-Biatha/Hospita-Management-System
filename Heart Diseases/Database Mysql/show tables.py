import mysql.connector as mq
conn=mq.connect(host='localhost',user='root',password='',database='mongo')
myquery='show tables'
mycur=conn.cursor()
if conn.is_connected():
    mycur.execute(myquery)
    for var in mycur:
        print(var)
    print('succeddfully !')
else:
    print('unsuccessfully show tables !')
mycur.close()
conn.close()