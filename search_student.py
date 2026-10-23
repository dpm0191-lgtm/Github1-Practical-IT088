
def search_student(students):
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found:", student["name"])
            return

    print("Student not found.")
