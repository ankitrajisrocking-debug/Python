class StudentRecords:
    def __init__(self):
        self.students = []

    def insert(self, roll_no, name, branch, cgpa):
        if self.search(roll_no):
            print(f"Student with roll no {roll_no} already exists.")
            return
        self.students.append({
            "roll_no": roll_no,
            "name": name,
            "branch": branch,
            "cgpa": cgpa
        })
        print(f"Inserted: {name} ({roll_no})")

    def delete(self, roll_no):
        record = self.search(roll_no)
        if record:
            self.students.remove(record)
            print(f"Deleted student with roll no {roll_no}")
        else:
            print(f"No student found with roll no {roll_no}")

    def search(self, roll_no):
        for s in self.students:
            if s["roll_no"] == roll_no:
                return s
        return None

    def search_by_name(self, name):
        return [s for s in self.students if s["name"].lower() == name.lower()]

    def update(self, roll_no, **fields):
        record = self.search(roll_no)
        if record:
            record.update(fields)
            print(f"Updated {roll_no}: {fields}")
        else:
            print(f"No student found with roll no {roll_no}")

    def display_all(self):
        if not self.students:
            print("No records found.")
            return
        for s in self.students:
            print(f"{s['roll_no']} | {s['branch']} | CGPA: {s['cgpa']}")


if __name__ == "__main__":
    db = StudentRecords()
    db.insert("CS101", "Ankit Raj", "CSE", 8.7)
    db.insert("CS102", "priya Sharma", "CSE", 9.1)
    db.insert 

    print("\nAll records:")
    db.display_all()

    print("\nSearch CS102:", db.search("CS102"))

    print("\nUpdating CGPA for CS101...")
    db.update("CS101", cgpa=9.0)

    print("\nDeleting EE101...")
    db.delete("EE101")

    print("\nFinal records:")
    db.display_all()