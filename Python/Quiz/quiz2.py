print("Welcome to our quiz!")
score = 0
question1 = "What's my favorite season?"
answer1 = "a) Fall, b) Winter, c) Spring, d) Summer"
print(question1)
print(answer1)
choice1 = input("Please enter a, b, c, or d: ")
if choice1 == 'b':
    print("You chose the right answer!")
    score += 1
    
question2 = "\nWhat's my favorite color?"
answer2 = "a) red b) orange c) yellow d) green e) blue f) purple g) pink h) black i) brown"
print(question2)
print(answer2)
choice2 = input("Please enter a, b, c, d, e, f, g, h, or i: ")
if choice2 == 'e':
    print("You chose the right answer!")
    score += 1
    
question3 = "\nWhat's my favorite food?"
answer3 = "a) burgers b) pizza c) pasta d) sushi"
print(question3)
print(answer3)
choice3 = input("Please enter a, b, c, or d: ")
if choice3 == 'c':
    print("You chose the right answer!")
    score += 1
    
question4 = "\nWhat's my zodiac sign?"
answer4 = "a) Aries b) Taurus c) Gemini d) Cancer e) Leo f) Virgo"
print(question4)
print(answer4)
choice4 = input("Please enter a, b, c, d, e, or f: ")
if choice4 == 'f':
    print("You chose the right answer!")
    score += 1
    
question5 = "\nAm I a nice friend?"
answer5 = "a) Yes b) No"
print(question5)
print(answer5)
choice5 = input("Please enter a or b: ")
if choice5 == 'a':
    print("You got it right!")
    score += 1
    
grade = (score/5) * 100
print("Your grade is", grade, "%")