import questionary

score = 0

name = questionary.text("What is your name?").ask()
print("Welcome", name)

question1 = questionary.select(
    "What is my favorite color?",
    ["red", "blue", "green", "I don't have one"]
).ask()

if question1 == "I don't have one":
    score += 1
    
question2 = questionary.select(
    "What is my favorite animal?",
    ["tiger", "panda", "dog", "none of the above"]
).ask()

if question2 == "dog":
    score += 1
    
question3 = questionary.select(
    "What is 2^14?",
    ["1024", "4098", "512", "16384"]
).ask()

if question3 == "16384":
    score += 1
    
grade = (score / 3) * 100
print("Your grade is", grade)