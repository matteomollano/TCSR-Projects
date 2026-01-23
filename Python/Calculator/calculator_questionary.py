import questionary

def add(num1, num2):
    answer = num1 + num2
    return answer

def subtract(num1, num2):
    answer = num1 - num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer

while True:
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    sign = questionary.select(
        "Choose a sign", ["+", "-", "*", "/"]
    ).ask()
    
    if sign == "+":
        answer = add(number1, number2)
        print(f"{number1} {sign} {number2} = {answer}")
    elif sign == "-":
        answer = subtract(number1, number2)
        print(f"{number1} {sign} {number2} = {answer}")
    elif sign == "/":
        answer = divide(number1, number2)
        print(f"{number1} {sign} {number2} = {answer}")
    elif sign == "*":
        answer = multiply(number1, number2)
        print(f"{number1} {sign} {number2} = {answer}")
        
    again = questionary.select(
        "Do you want to perform another calculation",
        ["Yes", "No"]
    ).ask()
    
    if again == "No":
        break
    else:
        print()