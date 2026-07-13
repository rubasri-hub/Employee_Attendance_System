from employee import (
    add_employee,
    view_employees,
    update_employee,
    delete_employee,
    search_employee,
    mark_attendance,
    view_attendance
)

while True:
    print("\n===== EMPLOYEE ATTENDANCE SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Mark Attendance")
    print("7. View Attendance")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        search_employee()

    elif choice == "6":
        mark_attendance()

    elif choice == "7":
        view_attendance()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please try again.")