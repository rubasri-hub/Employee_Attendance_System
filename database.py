import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rubasri*86",   # Unga MySQL password
        database="employee_attendance"
    )
    return conn