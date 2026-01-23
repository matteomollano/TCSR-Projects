from Ship import *
from tabulate import tabulate

class Board():
    
    # constructor
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = list()
        
    # getter and settor methods
    def getRows(self):
        return self.rows
    
    def getColumns(self):
        return self.columns
    
    # create the board
    def createBoard(self):
        rows = self.getRows()
        columns = self.getColumns()
        
        for i in range(rows):
            column = []
            for j in range(columns):
                newShip = Ship()
                column.append(newShip)
            self.board.append(column)
    
    # display the board
    def displayBoard(self):
        for row in self.board:
            for ship in row:
                print(ship, end="  ")
            print()
            
    # choose the target ship
    def chooseTarget(self, row, column):
        ship = self.board[row][column]
        ship.setTarget(True)
            
    
    def checkIfOpen(self, row_guess, column_guess):
        ship = self.board[row_guess][column_guess]
        symbol = ship.getSymbol()
        
        if symbol != "":
            return False
        return True
    
    # check if the user hit the ship
    def checkForHit(self, row_guess, column_guess):
        hitShip = self.board[row_guess][column_guess]
        target = hitShip.getTarget()
        
        if target == False: # didn't hit the ship
            hitShip.setSymbol("-")
            return False
        else:
            hitShip.setSymbol("X")
            return True
        
    # display the position of the ship if the user hasn't found it
    def gameOverDisplay(self):
        rows = self.getRows()
        columns = self.getColumns()
        
        # show the target ship
        for i in range(rows):
            for j in range(columns):
                ship = self.board[i][j]
                if ship.getTarget() == True:
                    ship.setSymbol("X")
                    break
         
    # display board as table
    def displayAsTable(self):
        # create column headers
        header = []
        for i in range(self.columns):
            header.append(i)
            
        # create row headers
        rows = []
        for i in range(self.rows):
            rows.append(i)
                
        # print formatted table
        print(tabulate(self.board, header, showindex=rows, numalign="center", stralign="center", tablefmt="simple_grid"))