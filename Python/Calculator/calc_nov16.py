def hello(name):
    return "Hello", name

print(hello("Hayden"))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    choice = input("Do you want to add, subtract, multiply, or divide? (a, s, m, or d): ")
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    
    if choice == 'a':
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
    elif choice == 's':
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
    elif choice == 'm':
        result = multiply(num1, num2)
        print(num1, "+", num2, "=", result)
    elif choice == 'd':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)            