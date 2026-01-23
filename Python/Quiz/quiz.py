import time

print("Welcome to the quiz game!")

score = 0

question1 = "Which airplane has 32 wheels?"
answer1 = "a) Boeing 747 b) An-225, c) Boeing 737, d) Wright Flyer"
print(question1)
print(answer1)
choice1 = input("Enter a, b, c, or d: ")

if choice1 == 'b':
    print("You are correct :)")
    score = score + 1
else:
    print("You are wrong :(")

question2 = "\nWhat continent is Georgia located in?"
answer2 = "a) Asia b) North America c) Mars d) Europe"
print(question2)
print(answer2)
choice2 = input("Enter a, b, c, or d: ")

if choice2 == 'd':
    print("You are correct :)")
    score = score + 1
else:
    print("You are wrong :(")
    
question3 = "\nWhat is the smartest species of ape?"
answer3 = "a) You b) Chimpanzee c) Orangutan d) Salad with asparagus cucumber eggs celery and more"
print(question3)
print(answer3)
choice3 = input("Enter a, b, c, or d: ")
if choice3 == 'c':
    print("Are you sure it's c? I think it's d. Wait let me check ...")
    time.sleep(2)
    print("You are correct :)")
    score = score + 1
else:
    print("You are wrong :(")
    
grade = (score/3) * 100
print("\nYour grade is", grade, "%")