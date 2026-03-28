keys = []

rooms = {
    "kitchen": {
        "description": "In the kitchen, you find a lot of cabinets full of food that look like they can hide something.",
        "choices": {
            "look in the first cabinet": "There was nothing in there other than food.",
            "look in the second cabinet": "There is only food.",
            "look in the fridge": "You find a key to the hallway!",
            "try to open the door to the hallway": "The door is locked.",
        }
    },
    "hallway": {
        "description": "When you go to the hallway, you find a door to the basement, 2 paintings, and a rug.",
        "choices": {
            "look under the rug": "You find a lot of dust.",
            "look behind painting 1": "You find a wall.",
            "look behind painting 2": "You find a secret opening in the wall with the key to the basement!",
            "try to open the door to the basement": "The door is locked."
        }
    },
    "basement": {
        "description": "When you go down into the basement, you find a couch, a tv next to a wall, and a mini-fridge.",
        "choices": {
            "look under the couch": "You find a key labeled front door!",
            "look behind the tv": "You find the nothing.",
            "look inside the mini-fridge": "You find some snacks, but nothing else.",
            "try to open the escape door": "The door is locked."
        }
    }
}

room_names = list(rooms.keys()) # ["kitchen", "hallway", "basement"]
current_room_number = 0

def display_choices(choices_list):
    print("You can do the following:")
    for i, choice in enumerate(choices_list):
        print(f"{i+1}. {choice}")
    
def get_choice():
    choice = input("What do you do? ")
    while choice not in ["1", "2", "3", "4"]:
        print("Error: you must enter 1, 2, 3, or 4 only.")
        choice = input("What do you do? ")
    return int(choice) - 1

print("You wake up in the kitchen with no memory of how you got there. You must escape.")

# get current room name and dictionary (starts off as kitchen)
current_room_name = room_names[current_room_number]
current_room = rooms[current_room_name]

# track last room to control when to display description/choices
last_room_number = -1

# game loop
while True:
    # get choices and responses for current room
    choices = list(current_room["choices"].keys())
    responses = list(current_room["choices"].values())
    
    # only display description and choices when entering new room
    if current_room_number != last_room_number:
        description = current_room["description"]
        print(description)
        display_choices(choices)
        # update last room to current room
        last_room_number = current_room_number
    
    # get the user's choice
    choice = get_choice()
    
    # display the response to the user's choice
    response = responses[choice]
    print(response)

    # if the response includes the key, add to the key list
    if "key" in response:
        keys.append(f"{current_room_name}_key")
        displayed_already = False
        
        # if before last room, switch to next room
        # if it's already last room, it's not possible to switch to next room
        if current_room_number < len(rooms) - 1:
            current_room_number += 1
            current_room_name = room_names[current_room_number]
            current_room = rooms[current_room_name]
        
    if len(keys) == len(rooms):
        # you win here
        print("You were able to escape the house! Phew ...")
        break
    
    if keys and current_room_number != last_room_number:
        print(f"Your keys: {keys}")

    print()