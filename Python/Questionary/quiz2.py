import questionary

score = 0
name = questionary.text("What is your name?").ask()

question1 = questionary.select(
    "What is my favorite animal", 
    ["Dog", "Cat", "Tiger", "Bear"]
).ask()

question2 = questionary.select(
    "What is my favorite color?",
    ["Red", "Blue", "Lilac", "Dandelion"]
).ask()

question3 = questionary.select(
    "What is my favorite food?",
    ["Pasta", "Chicken", "Pizza", "Rice"]
).ask()

question4 = questionary.select(
    "What is my favorite song?",
    ["Juna", "Amoeba", "I Wonder"]
).ask()

question5 = questionary.select(
    "What is my favorite soccer team?",
    ["Inter", "Real Madrid", "AC Milan", "Man City"]
).ask()

if question1 == "Dog":
    score += 1
    
if question2 == "Blue":
    score += 1

if question3 == "Pasta":
    score += 1
    
if question4 == "Amoeba":
    score += 1
    
if question5 == "AC Milan":
    score += 1
    
total_score = (score / 5) * 100
print(f"Your total score is {total_score:.2f}%")