#sql server
import pyodbc
mydb = pyodbc.connect(
    server="jsidcwrevdb2,1448",
    database="gimqr04",
    username="username",
    password="mypassword"
)
cursor = mydb.cursor()
cursor.execute("select * from tablename")
result = cursor.fetchall()
for data in result:
    print(data)
