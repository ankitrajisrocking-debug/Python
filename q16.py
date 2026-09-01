import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    cgpa REAL
)
""")

conn.commit()


# Add student
def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll, name, dept, cgpa)
        )
        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Roll number already exists!")


# Display all students
def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\nRoll No\tName\tDepartment\tCGPA")
    print("-" * 45)

    for student in students:
        print(student[0], "\t", student[1], "\t",
              student[2], "\t\t", student[3])


# Search student
def search_student():
    roll = int(input("Enter Roll Number to search: "))

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:
        print("\nRoll Number:", student[0])
        print("Name:", student[1])
        print("Department:", student[2])
        print("CGPA:", student[3])
    else:
        print("Student not found.")


# Update student
def update_student():
    roll = int(input("Enter Roll Number to update: "))

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll,)
    )

    if cursor.fetchone() is None:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    dept = input("Enter new department: ")
    cgpa = float(input("Enter new CGPA: "))

    cursor.execute("""
        UPDATE students
        SET name = ?, department = ?, cgpa = ?
        WHERE roll_no = ?
    """, (name, dept, cgpa, roll))

    conn.commit()
    print("Student updated successfully!")


# Delete student
def delete_student():
    roll = int(input("Enter Roll Number to delete: "))

    cursor.execute(
        "DELETE FROM students WHERE roll_no = ?",
        (roll,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main menu
while True:
    print("\n===== STUDENT INFORMATION SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        conn.close()
        print("Program closed.")
        break

    else:
        print("Invalid choice!")
