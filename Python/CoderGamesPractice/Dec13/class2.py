def question1():
    """
    1. Even or Odd Checker
    Ask the user to enter any number. Tell them whether the number is even or odd.
    (Hint: Think about what the remainder means when dividing by 2.)
    """
    while True:
        number = int(input("Enter a number: "))
        # modulo
        if number % 2 == 1:
            print("The number is odd")
        elif number % 2 == 0:
            print("The number is even")
        
        exit = input("Do you want to enter another number? (yes/no): ").lower().strip()
        if exit == "no":
            break
    
def question2():
    """
    2. FizzBuzz Challenge
    Count from 1 to 20.
    If a number is divisible by 3, display “Fizz”.
    If it's divisible by 5, display “Buzz”.
    If it's divisible by both, display “FizzBuzz”.
    Otherwise, just show the number itself.
    """
    # for loop
    for i in range(1, 21, 2):
        # start is 1st num, stop is 2nd num, step is 3rd num
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def question3():
    """
    3. Multiplication Table Maker
    Ask the user for a number (for example, 5).
    Then show that number's multiplication table from 1 through 12.
    (Example: 
    5 x 1 = 5
    5 x 2 = 10,
    5 x 3 = 15,
    ...
    5 x 12 = 60
    …)
    """
    number = int(input("Enter a number 1-12: "))
    for i in range(1, 13):
        result = number * i
        # print(number, "x", i, "=", result)
        print(f"{number} x {i} = {result}")
        
def question4():
    """
    4. The Temperature Converter
    Ask the user to enter a temperature in Fahrenheit.
    Convert it to Celsius using the formula:
    F = (C x 9/5) + 32
    C = (F - 32) * 5/9
    Then display the result.
    (Bonus: allow conversion in both directions!)
    """
    number = int(input("Enter a temperature in Fahrenheit: "))
    celsius = (number - 32) * 5/9
    print(f"{number} degrees Fahrenheit = {celsius} degrees Celsius")
    
question4()
    