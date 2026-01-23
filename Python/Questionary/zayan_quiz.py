import questionary

name = questionary.text("What's your name?").ask()
print("Welcome", name)

print("This quiz is about famous events!")

score = 0

question1 = questionary.rawselect(
    "What is my favorite thing to do in high school?",
    ["homecoming dance", "birthdays", "winter ball", "battle of the classes"]
).ask()

if question1 == "homecoming dance":
    score = score + 1
    
question2 = questionary.rawselect(
    "What number is 50% more than 30?",
    ["45", "40", "60", "100"]
).ask()

if question2 == "45":
    score = score + 1
    
question3 = questionary.rawselect(
    "What country do bacteria like the most?",
    ["USA", "Germany", "Japan", "France"]
).ask()

if question3 == "Germany":
    score = score + 1
    
question4 = questionary.rawselect(
    "What is my favorite fast-foods restaurant?",
    ["Subway", "McDonalds", "Burger King", "Wendy's"]
).ask()

if question4 == "Subway":
    score = score + 1
    
question5 = questionary.rawselect(
    "What room in my school likes stores the most?",
    ["711", "401", "301", "201"]
).ask()

if question5 == "711":
    score = score + 1
    
question6 = questionary.rawselect(
    "What is my favorite sport?",
    ["basketball", "swimming", "hockey", "soccer"]
).ask()

if question6 == "basketball":
    score = score + 1
    
question7 = questionary.rawselect(
    "What is my favorite animal?",
    ["dog", "cat", "tiger", "fish"]
).ask()

if question7 == "dog":
    score = score + 1
    
grade = (score / 7) * 100
grade = "{:.2f}".format(grade)
print("Your grade for the quiz is", grade + "%")