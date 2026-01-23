from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

# X starts so true
clicked = True
# keep track of number of moves
count = 0
# determine if user has won the game
winner = False

# Disable all buttons after game ends   
def disableAllButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    
# Reset all buttons for new game
def reset():
    global clicked, count, winner
    button1.config(text=" ", bg="Silver", state=NORMAL)
    button2.config(text=" ", bg="Silver", state=NORMAL)
    button3.config(text=" ", bg="Silver", state=NORMAL)
    button4.config(text=" ", bg="Silver", state=NORMAL)
    button5.config(text=" ", bg="Silver", state=NORMAL)
    button6.config(text=" ", bg="Silver", state=NORMAL)
    button7.config(text=" ", bg="Silver", state=NORMAL)
    button8.config(text=" ", bg="Silver", state=NORMAL)
    button9.config(text=" ", bg="Silver", state=NORMAL)
    clicked = True
    count = 0
    winner = False
  
# Button clicked function
def button_click(button):
    global clicked, count
    
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWin()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWin()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick Another Box...")
    
# Check to see if someone won
def checkWin():
    global winner
    char = " "
    
    if button1["text"] == button2["text"] == button3["text"] and button1["text"] != " ":
        button1.config(bg="green")
        button2.config(bg="green")
        button3.config(bg="green")
        winner = True
        char = button1["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
        
    elif button4["text"] == button5["text"] == button6["text"] and button4["text"] != " ":
        button4.config(bg="green")
        button5.config(bg="green")
        button6.config(bg="green")
        winner = True
        char = button4["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
        
    elif button7["text"] == button8["text"] == button9["text"] and button7["text"] != " ":
        button7.config(bg="green")
        button8.config(bg="green")
        button9.config(bg="green")
        winner = True
        char = button7["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
        
    elif button1["text"] == button4["text"] == button7["text"] and button1["text"] != " ":
        button1.config(bg="green")
        button4.config(bg="green")
        button7.config(bg="green")
        winner = True
        char = button1["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
    
    elif button2["text"] == button5["text"] == button8["text"] and button2["text"] != " ":
        button2.config(bg="green")
        button5.config(bg="green")
        button8.config(bg="green")
        winner = True
        char = button2["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
        
    elif button3["text"] == button6["text"] == button9["text"] and button3["text"] != " ":
        button3.config(bg="green")
        button6.config(bg="green")
        button9.config(bg="green")
        winner = True
        char = button3["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
    
    elif button1["text"] == button5["text"] == button9["text"] and button1["text"] != " ":
        button1.config(bg="green")
        button5.config(bg="green")
        button9.config(bg="green")
        winner = True
        char = button1["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
    
    elif button3["text"] == button5["text"] == button7["text"] and button3["text"] != " ":
        button3.config(bg="green")
        button5.config(bg="green")
        button7.config(bg="green")
        winner = True
        char = button3["text"]
        messagebox.showinfo("Tic Tac Toe", f"{char} wins!")
        disableAllButtons()
        
    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        reset()

    if winner == True:
      reset()
        
if __name__ == "__main__":
    # Build our buttons
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button3))

    button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button6))

    button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=lambda: button_click(button9))

    # Grid our buttons to the screen
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

    root.mainloop()