rooms = {
    "basement": {
        "description": "You wake up in the basement with no memory of how you got there.",
        "choices": {
            "look in your storage box": "you find some old family photos",
            "look on the book shelf": "you find a key inside of a book",
            "look in your freezer": "you find some ice cream, but nothing else.",
            "try to open door to hallway": "the door is locked"
        }
    },
    "hallway": {
        "description": "When you go to the hallway, you find a door, 2 paintings, and a rug.",
        "choices": {
            "look behind painting 1": "you find a wall",
            "look behind painting 2": "you find a secret opening in the wall with the key to the living room",
            "look under the rug": "you find a lot of dust",
            "try to open door to living room": "the door is locked"
        }
    },
    "living room": {
        "description": "When you go to the living room, you find a couch, a tv, vase, and a door to escape.",
        "choices": {
            "look under the couch pillows": "you find a they key to escape!",
            "look behind the tv": "you find some wires, but nothing else.",
            "look inside the vase": "you find some dirt and flowers.",
            "try to open escape door": "the door is locked",
        }
    }
}

current_room = rooms["basement"]

description = current_room["description"]
print(description)

choices = list(current_room["choices"].keys())

print("What do you do? ")
for i in range(4):
    print(f"{i+1}. {choices[i]}")

choice = input("Enter your choice: ")

# validate user input
while choice not in ["1", "2", "3", "4"]:
    print("Your choice must be 1, 2, 3, or 4 only.")
    choice = input("Enter your choice: ")

if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "3":
    pass
else: #4
    pass