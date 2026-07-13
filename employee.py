from datetime import date

from database import connect_db

# Add Employee
def add_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")

    query = "INSERT INTO employee VALUES (%s, %s, %s, %s)"
    values = (emp_id, name, department, designation)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Added Successfully!")
    conn.close()


# View Employees
def view_employees():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()

    print("\nEmployee List")
    print("-" * 50)

    for row in rows:
        print(row)

    conn.close()


# Update Employee
def update_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to update: "))
    department = input("Enter New Department: ")

    query = "UPDATE employee SET department=%s WHERE emp_id=%s"
    values = (department, emp_id)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Updated Successfully!")
    conn.close()


# Delete Employee
def delete_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to delete: "))

    query = "DELETE FROM employee WHERE emp_id=%s"
    values = (emp_id,)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Deleted Successfully!")
    conn.close()


# Search Employee
def search_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to search: "))

    query = "SELECT * FROM employee WHERE emp_id=%s"
    values = (emp_id,)

    cursor.execute(query, values)
    row = cursor.fetchone()

    if row:
        print("\nEmployee Found")
        print(row)
    else:
        print("Employee Not Found!")

    conn.close()
def mark_attendance():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID: "))
    attendance_date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter Status (Present/Absent): ")

    query = "INSERT INTO attendance(emp_id,attendance_date, status) VALUES (%s, %s, %s)"
    values = (emp_id, attendance_date, status)

    cursor.execute(query, values)
    conn.commit()

    print("Attendance Marked Successfully!")

    conn.close()
def view_attendance():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()

    print("\nAttendance Report")
    print("-" * 50)

    for row in rows:
        print(row)

    conn.close()