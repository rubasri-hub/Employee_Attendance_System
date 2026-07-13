import mysql.connector
import getpass

def connect_db():
    password=getpass.getpass("Enter MySQL password:")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password, 
        database="employee_attendance"
    )
    return conn