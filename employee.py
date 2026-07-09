from database import connect_db

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