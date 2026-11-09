import xml.etree.ElementTree as ET

# Load the existing XML file
tree = ET.parse("students.xml")
root = tree.getroot()

# Display all students
print("Student Information:")
for student in root.findall("student"):
    print("ID:", student.get("id"))
    print("Name:", student.find("name").text)
    print("Department:", student.find("department").text)
    print("Year:", student.find("year").text)
    print("Email:", student.find("email").text)
    print("CGPA:", student.find("cgpa").text)
    print("-" * 30)


# -------- MODIFY A STUDENT --------

# Find student with ID 103
student = root.find("./student[@id='103']")

if student is not None:
    student.find("name").text = "Rohit Kumar"
    student.find("cgpa").text = "8.3"

# -------- ADD A NEW STUDENT --------

new_student = ET.SubElement(root, "student")
new_student.set("id", "111")

ET.SubElement(new_student, "name").text = "Karan Singh"
ET.SubElement(new_student, "department").text = "CSE"
ET.SubElement(new_student, "year").text = "2"
ET.SubElement(new_student, "email").text = "karan.singh@example.com"
ET.SubElement(new_student, "cgpa").text = "8.8"


# -------- SAVE / GENERATE XML --------

tree.write("students_modified.xml",
           encoding="UTF-8",
           xml_declaration=True)

print("XML file generated successfully!")
