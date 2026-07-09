import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password",
    database="employee_attendance"
)

if conn.is_connected():
    print("Connected to MySQL Successfully!")

conn.close()
from employee import view_employees

print("EMPLOYEE ATTENDANCE SYSTEM")
print("--------------------------")

view_employees()
