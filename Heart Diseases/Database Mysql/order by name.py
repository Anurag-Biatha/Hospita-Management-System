import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mongo"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM student ORDER BY fname DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
