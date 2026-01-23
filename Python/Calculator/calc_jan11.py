
# parameters - a value that you pass to the function
def add(num1, num2): # function header
    return num1 + num2 # function body

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def mul(num1, num2):
    return num1 * num2

while True:
    choice = input("1 for add, 2 for subtract, 3 for multiply, 4 for divide: ")
    
    while choice not in ['1', '2', '3', '4']:
        choice = input("Invalid input. You must enter 1, 2, 3, or 4 only: ")
        
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    
    if choice == "1":
        sum = add(a, b)
        print("The sum is", sum)
    elif choice == "2":
        difference = sub(a, b)
        print("The difference is", difference)
    elif choice == "3":
        product = mul(a, b)
        print("The product is", product)
    else:
        quotient = div(a, b)
        print("The quotient is", quotient)
    
    print()