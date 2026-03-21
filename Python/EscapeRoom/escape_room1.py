import questionary

key_1 = False
key_2 = False
key_3 = False

rooms = {
    "kitchen": {
        "description": "In the kitchen, you find a lot of cabinets full of food that look like they can hide something.",
        "choices": {
            "look in the first cabinet": "There was nothing in there other than food.",
            "look in the second cabinet": "There is only food.",
            "look in the fridge": "you find a key to the hallway",
            "try to open the door to the hallway": "the door is locked",
        }
    },
    "hallway": {
        "description": "When you go to the hallway, you find a door to the basement, 2 paintings, and a rug.",
        "choices": {
            "look under the rug": "you find a lot of dust",
            "look behind painting 1": "you find a wall",
            "look behind painting 2": "you find a secret opening in the wall with the key to the basement",
            "try to open the door to the basement": "the door is locked"
        }
    },
    "basement": {
        "description": "When you go down into the basement, you find a couch, a tv next to a wall, and a mini-fridge.",
        "choices": {
            "look under the couch": "you find a key labeled front door",
            "look behind the tv": "you find the nothing",
            "look inside the mini-fridge": "you find some snacks, but nothing else"
        }
    }
}

current_room = rooms["kitchen"]
print(current_room)

description = current_room["description"]
print(description)

choices = current_room["choices"]
print(choices.keys())

choice = questionary.select(
    "What do you do?",
    choices.keys(),
).ask()
print(choice)