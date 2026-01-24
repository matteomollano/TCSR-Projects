import uuid

students = {}

def add_student(name, age, grade, courses):
    # generate student id
    student_id = str(uuid.uuid4())
    student_id = "stu-" + student_id[0:8]
    
    data = {
        "name": name,
        "age": age,
        "grade": grade,
        "courses": courses
    }
    
    students[student_id] = data

def delete_student(student_id):
    del students[student_id]
    
def display_student(data):
    name = data["name"]
    age = data["age"]
    grade = data["grade"]
    courses = data["courses"]
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    
    print("Courses:")
    for subject, letter_grade in courses.items():
        print(f"{subject}: {letter_grade}")
    
def search_student(student_id):
    print(f"Searching for student with ID {student_id}")
    student_data = students[student_id]
    display_student(student_data)

def display_all_students():
    for student_id, data in students.items():
        print(f"Student ID: {student_id}")
        display_student(data)
        
def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    grade = input("Enter your school grade: ")
    
    courses = {}
    while True:
        subject = input("Enter a subject: ")
        letter_grade = input("Enter letter grade: ")
        courses[subject] = letter_grade
        
        again = input("Do you want to enter another course? (y/n): ")
        if again != "y":
            break
    
    add_student(name, age, grade, courses)
    display_all_students()
    
main()