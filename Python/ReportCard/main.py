
# reusable block of code
# task -> convert a number grade to a letter grade
def get_letter_grade(number_grade):
    if number_grade >= 97:
        return 'A+'
    elif number_grade >= 93:
        return 'A'
    elif number_grade >= 90:
        return 'A-'
    elif number_grade >= 87:
        return 'B+'
    elif number_grade >= 83:
        return 'B'
    elif number_grade >= 80:
        return 'B-'
    elif number_grade >= 77:
        return 'C+'
    elif number_grade >= 73:
        return 'C'
    elif number_grade >= 70:
        return 'C-'
    elif number_grade >= 67:
        return 'D+'
    elif number_grade >= 63:
        return 'D'
    elif number_grade >= 60:
        return 'D-'
    else:
        return 'F'

# main code
num_subjects = input("How many subjects do you take in school? ")
while not num_subjects.isdecimal():
    num_subjects = input("Please enter an integer only: ")
num_subjects = int(num_subjects)

# get student's subjects and corresponding grades
grades = []
for i in range(num_subjects):
    grade = input("Enter your subject and grade (ex: Math 95): ")
    grades.append(grade)

print("\n-----------------------------------")
print("Report Card")
print("-----------------------------------")

# compute gpa and display report card
total = 0
for grade in grades:
    subject, grade_num = grade.split(' ')
    grade_num = int(grade_num)
    letter_grade = get_letter_grade(grade_num)
    print(subject, grade_num, '->', letter_grade)
    total = total + grade_num
    
average = total / num_subjects
overall_letter_grade = get_letter_grade(average)
print('GPA:', average, '=', overall_letter_grade)
print("-----------------------------------")