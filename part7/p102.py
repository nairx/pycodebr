import mysql.connector
#pip install mysql-connector-python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)
mycursor = mydb.cursor()
mycursor.execute("create database broadridge")
