
def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("----------------")
