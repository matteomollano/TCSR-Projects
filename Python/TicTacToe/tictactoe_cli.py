import random

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

current_player = "X"
winner = None
game_running = True


# print the game board
def printBoard(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("----------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("----------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# get input from the player
def playerInput(board):
  input1 = int(input("Enter a number 0-8: "))
  if input1 >= 0 and input1 <= 8 and board[input1] == "-":
    board[input1] = current_player
  else:
    print("Oops that spot is already taken!")
    playerInput(board)

# check for a horizontal win
def checkHorizontal(board):
  global winner
  if board[0] == board[1] == board[2] and board[1] != "-":
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[3]
    return True
  elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    return True
  return False

# check for a vertical win
def checkVertical(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True
  return False

# check for a diagonal win
def checkDiagonal(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True
  return False

# check for a tie
def checkTie(board):
  global game_running
  if "-" not in board:
    if checkHorizontal(board) == False:
      if checkVertical(board) == False:
        if checkDiagonal(board) == False:
          print()
          printBoard(board)
          print()
          print("It is a tie!")
          game_running = False

# check for a win
def checkWin(board):
  global game_running
  if checkHorizontal(board):
    print()
    printBoard(board)
    print()
    print(f"The winner is {winner}!")
    game_running = False
  elif checkVertical(board):
    print()
    printBoard(board)
    print()
    print(f"The winner is {winner}")
    game_running = False
  elif checkDiagonal(board):
    print()
    printBoard(board)
    print()
    print(f"The winner is {winner}")
    game_running = False
    
# switch the player
def switchPlayer():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O": ## or just else
    current_player = "X"

# create the AI
def AI(board):
  while current_player == "O":
    position = random.randint(0,8)
    if board[position] == "-":
      board[position] = "O"
      print(f"AI chose position {position}")
      switchPlayer()
  
# run the game
while game_running == True:
  printBoard(board)
  print()
  playerInput(board)
  checkWin(board)
  checkTie(board)

  if game_running == False:
    break
  
  switchPlayer()
  ## to play vs the AI!
  print()
  AI(board)
  checkWin(board)
  checkTie(board)
  print()