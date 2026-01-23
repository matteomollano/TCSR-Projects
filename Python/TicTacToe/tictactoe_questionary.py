import questionary, random

global board, options

board = ["  ", "  ", "  ", 
         "  ", "  ", "  ", 
         "  ", "  ", "  "]

options = ["Upper Left", "Upper Middle", "Upper Right", 
         "Middle Left", "Center", "Middle Right", 
         "Bottom Left", "Bottom Middle", "Bottom Right"]

dictionary = {
    "Upper Left": 0,
    "Upper Middle": 1,
    "Upper Right": 2,
    "Middle Left": 3,
    "Center": 4,
    "Middle Right": 5,
    "Bottom Left": 6,
    "Bottom Middle": 7,
    "Bottom Right": 8
}

characters = ["🏀", "😂", "🚗", "🐕", "🍕", "🍟", "🍎", "🔥"]

game_playing = True

# print the game board
def printBoard(board):
  print(f"{board[0]} | {board[1]} | {board[2]}")
  print("------------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("------------")
  print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput():
    choice = questionary.select(
        "Pick a spot:", 
        options
    ).ask()
    options.remove(choice)
    return choice
    
def playerCharacter():
    playerChoice = questionary.select(
        "Choose your character:",
        characters
    ).ask()
    return playerChoice
    
def computerCharacter():
    computer = random.choice(characters)
    while computer == current_player:
        computer = random.choice(characters)
    return computer

def addToBoardPlayer(board, choice):
    index = dictionary[choice]
    board[index] = current_player
    
def getKeyFromValue(choice):
    for key, value in dictionary.items():
        if value == choice:
            return key

def addToBoardComputer(board, choice):
    option_to_remove = getKeyFromValue(choice)
    options.remove(option_to_remove)
    board[choice] = current_computer
    
def getEmptySpot(board):
    emptySpots = []
    for i in range(len(board)):
        if board[i] == "  ":
            emptySpots.append(i)
    
    emptySpot = random.choice(emptySpots)
    return emptySpot

def checkVertical(board):
    #0, 3, 6 - 1, 4, 7 - 2, 5, 8
    if board[0] == board[3] == board[6] and board[0] != "  ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != "  ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != "  ":
        return True
    else:
        return False
    
def checkHorizontal(board):
    if board[0] == board[1] == board[2] and board[0] != "  ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != "  ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != "  ":
        return True
    else:
        return False
    
def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "  ":
        return True
    elif board[2] == board[4] == board[6] and board[2] != "  ":
        return True
    else:
        return False
    
def checkWinner(board):
    if checkVertical(board):
        return True
    elif checkHorizontal(board):
        return True
    elif checkDiagonal(board):
        return True
    else:
        return False
    
def checkTie(board):
    if "  " not in board:
        return True
    else:
        return False

def resetBoard():
    global board, options
    board = ["  ", "  ", "  ", 
         "  ", "  ", "  ", 
         "  ", "  ", "  "]

    options = ["Upper Left", "Upper Middle", "Upper Right", 
            "Middle Left", "Center", "Middle Right", 
            "Bottom Left", "Bottom Middle", "Bottom Right"]
    
def playAgain():
    global current_player, current_computer
    print("\n")
    play_again = questionary.select(
        "Do you want to play again?",
        ["Yes", "No"]
    ).ask()
            
    if play_again == "Yes":
        resetBoard()
        print("Starting new game...\n")
        current_player = playerCharacter()
        current_computer = computerCharacter()
        return True
    else:
        return False
         
if __name__ == "__main__":
    current_player = playerCharacter()
    current_computer = computerCharacter()

    while game_playing == True:
        board_spot = playerInput()
        addToBoardPlayer(board, board_spot)
        if checkWinner(board):
            game_playing = False
            print(f"Player {current_player} wins!")
            printBoard(board)
            game_playing = playAgain()
            continue
        print("\n")
        
        if checkTie(board):
            print("It's a tie")
            printBoard(board)
            game_playing = playAgain()
            continue
        
        empty_spot = getEmptySpot(board)
        addToBoardComputer(board, empty_spot)
        if checkWinner(board):
            game_playing = False
            print(f"Computer {current_computer} wins!")
            game_playing = playAgain()
        printBoard(board)
        print("\n")
        
        if checkTie(board):
            print("It's a tie")
            printBoard(board)
            game_playing = playAgain()