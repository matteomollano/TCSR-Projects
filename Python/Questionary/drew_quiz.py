import questionary

question1 = questionary.select(
    "What is my fortnite name?",
    ["sh1ft-", "ASB-lurk", "sh1ftzy", "sh1ft", "lurk"]
).ask()

if question1 == "sh1ftzy":
    print("You are correct")
else:
    print("You are wrong")