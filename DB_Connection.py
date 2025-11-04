import mysql.connector

def DB_Connect():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root123',
        database='jt2'
    )
    return mydb

