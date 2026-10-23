
def delete_student(students):
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")
