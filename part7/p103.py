import mysql.connector
#pip install mysql-connector-python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="broadridge"
)
mycursor = mydb.cursor()
mycursor.execute("select * from customers")
result = mycursor.fetchall()
for data in result:
    print(data)