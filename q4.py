students = {
    101: ("101", "Ankit"),
    102: ("102", "Priya"),
    103: ("103", "Rahul"),
    104: ("104", "Sneha"),
    105: ("105", "Farhan"),
}

python_course = {101, 102, 103, 104}
ml_course = {102, 103, 105}
dsa_course = {101, 103, 104, 105}

courses = {
    "Python": python_course,
    "Machine Learning": ml_course,
    "DSA": dsa_course
}

def student_names(id_set):
    """Convert a set of student IDs into a list of names using the tuple records."""
    return [students[sid][1] for sid in id_set]

def print_result(title, id_set):
    print(f"\n{title} ({len(id_set)} students):")
    for sid in sorted(id_set):
        print(f"{students[sid][0]} - {students[sid][1]}")

# set operations

union_py_ml = python_course | ml_course
print_result("Union: Python OR Machine Learning ", union_py_ml)

common_py_ml = python_course & ml_course
print_result("Intersection: Python AND Machine Learning (common)", common_py_ml)

only_ml = ml_course - python_course
print_result("Difference: ML only ", only_ml)

sym_diff = python_course ^ ml_course
print_result("Symmetric Difference: python XOR ml", sym_diff)

all_three = python_course & ml_course & dsa_course
print_result("Students enrolled in all three courses", all_three)

any_course = python_course | ml_course | dsa_course
print_result("Students enrolled in atleast one course", any_course)

all_students = set(students.keys())
no_course = all_students - any_course
print_result("Students not enrolled in any course", no_course)

only_one = set()
for sid in all_students:
    count = sum(sid in c for c in courses.values())
    if count == 1:
        only_one.add(sid)

print_result("Students enrolled in exactly one course", only_one)