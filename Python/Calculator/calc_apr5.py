
while True:
    choice = input('Do you want to add (+), subtract (-), multiply (*), or divide (/): ').strip()
    while choice not in ['+', '-', '*', '/']:
        choice = input(choice + " is not a valid option. Enter again: ").strip()
    
    num1 = input('Enter a number: ') # 10
    while not num1.isnumeric():
        num1 = input('Enter a number only: ')
    num1 = int(num1)
    
    num2 = input('Enter a second number: ') # 5
    while not num2.isnumeric():
        num2 = input('Enter a number only: ')
    num2 = int(num2)
    
    if choice == '+':
        result = num1 + num2
        print(num1, "+", num2, "=", result) # 10 + 5 = 15
    elif choice == '-': # elif means else if
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif choice == '*':
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif choice == '/':
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    print()