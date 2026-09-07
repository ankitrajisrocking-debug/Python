import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("university.xml")
root = tree.getroot()

# Display university information
print("==============================================")
print("           UNIVERSITY INFORMATION")
print("==============================================")

print("University Name:", root.get("name"))

campus = root.find("campus")

print("Location:", campus.find("location").text)
print("Established:", campus.find("established").text)
print("Website:", campus.find("website").text)

# Display department information
print("\n==============================================")
print("              DEPARTMENT DETAILS")
print("==============================================")

for department in root.find("departments").findall("department"):

    print("\nDepartment ID:", department.get("id"))
    print("Department Name:", department.find("name").text)
    print("HOD:", department.find("hod").text)
    print("Building:", department.find("building").text)

    # Display student information
    print("\n  STUDENTS")
    print("  --------")

    students = department.find("students")

    for student in students.findall("student"):

        student_id = student.get("id")

        personal = student.find("personal_details")
        academic = student.find("academic_details")

        name = personal.find("name")
        first_name = name.find("first_name").text
        last_name = name.find("last_name").text

        print("\n  Student ID:", student_id)
        print("  Name:", first_name, last_name)
        print("  Gender:", personal.find("gender").text)
        print("  Date of Birth:", personal.find("date_of_birth").text)
        print("  Phone:", personal.find("phone").text)
        print("  Email:", personal.find("email").text)

        # Address
        address = personal.find("address")

        print("  Address:")
        print("    Street:", address.find("street").text)
        print("    City:", address.find("city").text)
        print("    State:", address.find("state").text)
        print("    Postal Code:", address.find("postal_code").text)

        # Academic information
        print("  Academic Details:")
        print("    Year:", academic.find("year").text)
        print("    Semester:", academic.find("semester").text)
        print("    CGPA:", academic.find("cgpa").text)
        print("    Advisor:", academic.find("advisor").text)

        # Courses
        print("  Courses:")

        courses = academic.find("courses")

        for course in courses.findall("course"):
            print("    - Course Code:", course.get("code"))
            print("      Course Name:", course.find("name").text)
            print("      Credits:", course.find("credits").text)
            print("      Marks:", course.find("marks").text)
            print("      Grade:", course.find("grade").text)
