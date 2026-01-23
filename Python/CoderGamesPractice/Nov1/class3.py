
def question1():
    """
    1. Even or Odd Checker
    Ask the user to enter any number.
    Tell them whether the number is even or odd.
    (Hint: Think about what the remainder means when dividing by 2.)
    4/2=2 R0
    5/2=2 R1
    6/2=3 R0
    7/2=3 R1
    """
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def question2():
    """
    2. FizzBuzz Challenge
    Count from 1 to 20.
    If a number is divisible by 3, display “Fizz”.
    If it's divisible by 5, display “Buzz”.
    If it's divisible by both, display “FizzBuzz”.
    Otherwise, just show the number itself.
    """
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")
        else:
            print(i)
        
def question3():
    """
    Ask the user for a number (for example, 5).
    Then show that number's multiplication table from 1 through 12.
    (Example: 
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15 
    …)
    """
    number = int(input("Enter a number: "))
    for i in range(1, 13):
        print(number, "x", i, "=", number * i)

def question4():
    """
    4. The Temperature Converter
    Ask the user to enter a temperature in Fahrenheit.
    Convert it to Celsius using the formula:
    C = (F - 32) * 5/9
    Then display the result.
    (Bonus: allow conversion in both directions!)
    """
    temp = float(input("Enter a fahrenheit temperature: "))
    celsius = (temp - 32) * 5/9
    print(temp, "degrees F =", celsius, "degrees C")

question4()

# Owen did
# - letter frequency
# - word counter
# - palindrome detector
# - all text based stuff (using harrypotter.txt)