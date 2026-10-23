
def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    students.append({"name": name, "roll": roll})

    print("Student added successfully!")
