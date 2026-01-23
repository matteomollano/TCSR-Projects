import questionary

# Julian Quiz
butter = questionary.text("Enter your name").ask()
password = questionary.password("Enter your password").ask()

gross = 0
fanboy = 0
motherschild = 0
alien = 0

question1 = questionary.select(
    "What's your favorite food?", 
    ["Strawberries", "Pizza", "Spinach", "Poo"]
).ask()

if question1 == "Strawberries":
    gross += 1
elif question1 == "Pizza":
    fanboy += 1
elif question1 == "Spinach":
    motherschild += 1
else:
    alien += 1

question2 = questionary.select(
    "What worries you most?", 
    ["Not eating canteloupes", "Not being the most popular", "Mom being sad", "My home planet"]
).ask()

if question2 == "Not eating canteloupes":
    gross += 1
elif question2 == "Not being the most popular":
    fanboy += 1
elif question2 == "Mom being sad":
    motherschild += 1
else:
    alien += 1
    
question3 = questionary.select(
    "What do you want to be when you grow up?", 
    ["Durian eater", "Guy in the stadium", "Janitor", "Pooping on the sidewalk person"]
).ask()

if question3 == "Durian eater":
    gross += 1
elif question3 == "Guy in the stadium":
    fanboy += 1
elif question3 == "Janitor":
    motherschild += 1
else:
    alien += 1
    
question4 = questionary.select(
    "What's your favorite animal?", 
    ["Gorilla", "Myself", "Whatever Mom thinks", "Flies"]
).ask()

if question4 == "Gorilla":
    gross += 1
elif question4 == "Myself":
    fanboy += 1
elif question4 == "Whatever Mom thinks":
    motherschild += 1
else:
    alien += 1
    
question5 = questionary.select(
    "What's your daily hobby?", 
    ["Eating everything", "Cheering on sports people", "Cleaning up after Mom", "Watching banana peels rot"]
).ask()

if question4 == "Eating everything":
    gross += 1
elif question4 == "Cheering on sports people":
    fanboy += 1
elif question4 == "Cleaning up after Mom":
    motherschild += 1
else:
    alien += 1
    
# finding your personality
if gross > fanboy and gross > motherschild and gross > alien:
    print("You are...a gross person!")
elif fanboy > gross and fanboy > motherschild and fanboy > alien:
    print("You are...a fantastic fanboy!")
elif motherschild > gross and motherschild > fanboy and motherschild > alien:
    print("You are...a mother's child!")
else:
    print("You are...an out-of-this-word alien!")