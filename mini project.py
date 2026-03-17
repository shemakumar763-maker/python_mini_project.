student={}
def add_student(name, mark):
    student[name]=mark
    print("Student added successfully")
def display_students():
    for name, mark in student.items():
        print(f"Name: {name}, Mark: {mark}")
add_student("Alice", 85)
add_student("Bob", 90)
display_students()
