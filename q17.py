import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()


# CREATE
def add_employee():
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    designation = input("Designation: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    try:
        cursor.execute("""
        INSERT INTO employees
        VALUES (?, ?, ?, ?, ?)
        """, (emp_id, name, designation, department, salary))

        conn.commit()
        print("Employee added successfully!")

    except sqlite3.IntegrityError:
        print("Employee ID already exists!")


# READ
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        print("No employee records found.")
        return

    print("\nID | Name | Designation | Department | Salary")
    print("-" * 60)

    for emp in employees:
        print(emp)


# UPDATE
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))

    cursor.execute(
        "SELECT * FROM employees WHERE employee_id = ?",
        (emp_id,)
    )

    if cursor.fetchone() is None:
        print("Employee not found!")
        return

    name = input("New Name: ")
    designation = input("New Designation: ")
    department = input("New Department: ")
    salary = float(input("New Salary: "))

    cursor.execute("""
    UPDATE employees
    SET name = ?, designation = ?, department = ?, salary = ?
    WHERE employee_id = ?
    """, (name, designation, department, salary, emp_id))

    conn.commit()
    print("Employee updated successfully!")


# DELETE
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employees WHERE employee_id = ?",
        (emp_id,)
    )

    if cursor.rowcount == 0:
        print("Employee not found!")
    else:
        conn.commit()
        print("Employee deleted successfully!")


# MAIN MENU
while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

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
        conn.close()
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
