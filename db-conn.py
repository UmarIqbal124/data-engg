import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root' ,
    password = '',
    database = 'weatherapi'
)
print(mydb)