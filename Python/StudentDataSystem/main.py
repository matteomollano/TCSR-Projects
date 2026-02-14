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
        print()
        
def main():
    print("Welcome to Student Data System")
    while True:
        print("1. Search for student")
        print("2. Add new student")
        print("3. Delete student")
        print("4. Display all students")
        prompt = input("Choose an option: ")
        
        if prompt == "1":
            print("You chose search")
            student_id = input("Enter student ID to search for: ")
            search_student(student_id)
            
        elif prompt == "2":
            print("You chose add")
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            courses = {}
            for i in range(10):
                subject = input("Enter subject: ")
                letter_grade = input("Enter letter grade: ")
                courses[subject] = letter_grade

                if len(courses) >= 5:
                    again = input("Another course? y/n").lower()
                    if again == "n":
                        break  
             
            add_student(name, age, grade, courses)
                
        elif prompt == "3":
            print("You chose delete")
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
            
        elif prompt == "4":
            print("You chose display all")
            display_all_students()
            
        else:
            print("Error")
    
main()