import mysql.connector
#pip install mysql-connector-python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="broadridge"
)
mycursor = mydb.cursor()
# mycursor.execute("create table students (name varchar(10),email varchar(100))")
# mycursor.execute("insert into students values('Amy','amy@gmail.com')")
# mydb.commit()
# mycursor.execute("select * from students")
# result = mycursor.fetchall()
# for row in result:
#     print(row)

while True:
    name = input("Enter name: ")
    email = input("Enter email: ")
    str = f"insert into students(name,email) values({name},{email})"
    mycursor.execute(str)
    mydb.commit()
    ch = input("Continue?(y/n)")
    if ch != "y":
        break
