from tkinter import *

expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""
    
def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry("325x400")
    
    display = StringVar()
    entry = Entry(root, textvariable=display, background="white", fg='black')
    entry.grid(columnspan=4, ipadx=70)
    
    # number buttons
    btn1 = Button(root, text='1', fg='black', bg='black', height=2, width=2, command=lambda: press(1))
    btn1.grid(row=2, column=0)
    
    btn2 = Button(root, text='2', fg='black', bg='black', height=2, width=2, command=lambda: press(2))
    btn2.grid(row=2, column=1)
    
    btn3 = Button(root, text='3', fg='black', bg='black', height=2, width=2, command=lambda: press(3))
    btn3.grid(row=2, column=2)
    
    btn4 = Button(root, text='4', fg='black', bg='black', height=2, width=2, command=lambda: press(4))
    btn4.grid(row=3, column=0)
    
    btn5 = Button(root, text='5', fg='black', bg='black', height=2, width=2, command=lambda: press(5))
    btn5.grid(row=3, column=1)
    
    btn6 = Button(root, text='6', fg='black', bg='black', height=2, width=2, command=lambda: press(6))
    btn6.grid(row=3, column=2)
    
    btn7 = Button(root, text='7', fg='black', bg='black', height=2, width=2, command=lambda: press(7))
    btn7.grid(row=4, column=0)
    
    btn8 = Button(root, text='8', fg='black', bg='black', height=2, width=2, command=lambda: press(8))
    btn8.grid(row=4, column=1)
    
    btn9 = Button(root, text='9', fg='black', bg='black', height=2, width=2, command=lambda: press(9))
    btn9.grid(row=4, column=2)
    
    btn0 = Button(root, text='0', fg='black', bg='black', height=2, width=2, command=lambda: press(0))
    btn0.grid(row=5, column=1)
    
    # operator buttons
    plus = Button(root, text='+', fg='black', height=2, width=2, command=lambda: press('+'))
    plus.grid(row=2, column=3)
    
    minus = Button(root, text='-', fg='black', height=2, width=2, command=lambda: press('-'))
    minus.grid(row=3, column=3)
    
    times = Button(root, text='x', fg='black', height=2, width=2, command=lambda: press('*'))
    times.grid(row=4, column=3)
    
    divide = Button(root, text='÷', fg='black', height=2, width=2, command=lambda: press('/'))
    divide.grid(row=5, column=3)
    
    # other buttons
    equal = Button(root, text='=', fg='black', height=2, width=2, command=equal)
    equal.grid(row=6, column=3)
    
    dot = Button(root, text='.', fg='black', height=2, width=2, command=lambda: press('.'))
    dot.grid(row=5, column=2)
    
    clear = Button(root, text='AC', fg='black', height=2, width=2, command=clear)
    clear.grid(row=5, column=0)
    
    root.mainloop()
