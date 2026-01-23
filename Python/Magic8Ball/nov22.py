import random

responses = [
    "Sorry I don't know the answer.",
    "NOOOOOO",
    "Ask again later.",
    "I refuse to answer you.",
    "YES",
    "Maybe",
    "Probably not",
    "I have no idea. Figure it out yourself.",
    
    # Kind
    "Absolutely! Good things are coming your way.",
    "Yes — and I'm rooting for you!",
    "It looks very promising, keep going!",
    "Definitely yes. You've got this.",

    # Confused
    "Uh… what was the question again?",
    "I mean… maybe? I think? Hard to say.",
    "My vision is blurry. Ask later?",
    "I'm not totally sure what's happening here.",

    # Rude
    "No. And honestly, that was a terrible question.",
    "Why would you even ask that?",
    "Please… just no.",
    "Try again when you're thinking more clearly.",

    # Angry
    "ABSOLUTELY NOT. Don't make me answer that again.",
    "No! Stop asking me that!",
    "I refuse to answer this nonsense.",
    "I'm too annoyed to respond. Ask later.",

    # Classic 8-ball style
    "Outlook good.",
    "Very doubtful.",
    "Ask again later.",
    "Cannot predict now.",
    "Yes, definitely.",
    "Signs point to yes.",
    "My sources say no."
]

while True:
    question = input("I am Magic 8 Ball! Ask me anything or q to quit: ").strip()
    if question == "q":
        print("Game over. Thanks for playing!")
        break
    elif question == "":
        print("Please enter a real question.")
    else:
        answer = random.choice(responses)
        print(answer)