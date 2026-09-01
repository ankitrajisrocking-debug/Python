import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT,
    department TEXT NOT NULL,
    salary REAL
)
""")

# Insert sample data
employees = [
    (101, "Rahul", "Manager", "CSE", 80000),
    (102, "Ankit", "Developer", "CSE", 60000),
    (103, "Priya", "Analyst", "ECE", 55000),
    (104, "Ravi", "Developer", "ECE", 65000),
    (105, "Neha", "Manager", "ME", 75000),
    (106, "Aman", "Engineer", "ME", 50000)
]

cursor.executemany("""
INSERT OR IGNORE INTO employees
(employee_id, name, designation, department, salary)
VALUES (?, ?, ?, ?, ?)
""", employees)

conn.commit()



def salary_report(department):

    query = """
    SELECT department,
           COUNT(*) AS total_employees,
           SUM(salary) AS total_salary,
           AVG(salary) AS average_salary,
           MAX(salary) AS highest_salary,
           MIN(salary) AS lowest_salary
    FROM employees
    WHERE department = ?
    GROUP BY department
    """

    # Parameterized SQL query
    cursor.execute(query, (department,))

    result = cursor.fetchone()

    if result:
        print("\nDepartment-wise Salary Report")
        print("--------------------------------")
        print("Department       :", result[0])
        print("Total Employees  :", result[1])
        print("Total Salary     :", result[2])
        print("Average Salary   :", round(result[3], 2))
        print("Highest Salary   :", result[4])
        print("Lowest Salary    :", result[5])
    else:
        print("No employees found in this department.")


# Take department from user
department = input("Enter department: ")

salary_report(department)

# Close connection
conn.close()
