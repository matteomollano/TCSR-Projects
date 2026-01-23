from tkinter import *
import random

# constants for snake game
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 35
BODY_PARTS = 3
# snake color scheme
#SNAKE_COLOR = "#00FF00" # this is hex for green
#FOOD_COLOR = "#FF0000" # this is red for apple
# python color scheme
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#FFFF00"
BACKGROUND_COLOR = "#000000" # black background

class Snake:
    def __init__(self) -> None:
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self) -> None:
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE
    
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

# functions for game
def nextTurn(snake, food):
    
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    # update the head's coordinates
    snake.coordinates.insert(0, (x, y))
    
    # create a new body and add it to the snake
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    
    # if x coordinate of snake's head == x coordinate of food (apple)
    # AND
    # if y coordinate of snake's head == y coordinate of food (apple)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        # delete the last body part of snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if checkCollisions(snake):
        gameOver()
    else:
        window.after(SPEED, nextTurn, snake, food)

def changeDirection(newDirection):
    
    global direction
    
    if newDirection == 'left' and direction != 'right':
        direction = newDirection
    elif newDirection == 'right' and direction != 'left':
        direction = newDirection
    elif newDirection == 'up' and direction != 'down':
        direction = newDirection
    elif newDirection == 'down' and direction != 'up':
        direction = newDirection

def checkCollisions(snake):
    
    # get snake head
    x, y = snake.coordinates[0]
    
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    # [1:] --> check everything after the head of the snake (only body parts)
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
    font=('consolas', 70), text="GAME OVER", fill="red", tags="game over")

if __name__ == "__main__":
    # creating the tkinter window for game
    window = Tk()
    window.title("Snake")

    # making the window non-resizable
    window.resizable(False, False)

    # creating a score label and setting initial direction
    score = 0
    direction = 'down'
    label = Label(window, text=f"Score: {score}", font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2)) - 50
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # checking if arrows keys are pressed to change direction of snake
    window.bind('<Left>', lambda event: changeDirection('left'))
    window.bind('<Right>', lambda event: changeDirection('right'))
    window.bind('<Up>', lambda event: changeDirection('up'))
    window.bind('<Down>', lambda event: changeDirection('down'))
    
    # bind wasd keys for movement
    window.bind('<w>', lambda event: changeDirection('up'))
    window.bind('<a>', lambda event: changeDirection('left'))
    window.bind('<s>', lambda event: changeDirection('down'))
    window.bind('<d>', lambda event: changeDirection('right'))
    
    # create the snake and food objects
    snake = Snake()
    food = Food()

    nextTurn(snake, food)
    window.mainloop()