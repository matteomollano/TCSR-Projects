from Ship import *
from Board import *
import random

# display welcome message
def display():
    print("\nWelcome to Ships!")
    print("The objective of the game is to guess where the ship is placed on the board.")
    print("You have 10 tries.")
    print("Good Luck!!!\n")
    
# get user choice for row
def getUserRow(rows):
    while True:
        row_guess = int(input(f"Please enter a row (between 0 and {rows-1}): "))
        if row_guess >= 0 and row_guess < rows:
            return row_guess
        else:
            print(f"Not a valid row. Please enter a value between 0 and {rows-1}\n")
            
# get user choice for columns
def getUserColumn(columns):
    while True:
        column_guess = int(input(f"Please enter a column (between 0 and {columns-1}): "))
        if column_guess >= 0 and column_guess < columns:
            return column_guess
        else:
            print(f"Not a valid column. Please enter a value between 0 and {columns-1}\n")

if __name__ == "__main__":
    
    display()
    
    # create the board
    rows = 7
    columns = 7
    Board = Board(rows,columns)
    Board.createBoard()
  
    # choose a random target position
    random_row = random.randint(0, rows-1)
    random_column = random.randint(0, columns-1)
    Board.chooseTarget(random_row,random_column)
    
    # game playing loop
    numOfGuesses = 10
    guessesUsed = 0
    
    for i in range(numOfGuesses):
        
        # display board
        Board.displayAsTable()
        print()
        
        # ask the user for a guess
        row_guess = getUserRow(rows)
        column_guess = getUserColumn(columns)
        
        while Board.checkIfOpen(row_guess, column_guess) == False:
            print("Spot was already taken. Choose a different board position.")
            row_guess = getUserRow(rows)
            column_guess = getUserColumn(columns)
        
        guessesUsed += 1
        
        # check for a hit
        hit = Board.checkForHit(row_guess, column_guess)
        
        # see if you hit the ship or not
        if hit == True:
            print("You found the ship! You Win!\n")
            Board.displayAsTable()
            break
        elif hit == False and guessesUsed < 10:
            print("Missed ship. Try again\n\n")
        else:
            print("Sorry. You didn't find the ship.\nThe ship's location can be seen below.\n\n")
            Board.gameOverDisplay()
            Board.displayAsTable()