"""
1. Even or Odd Checker
Ask the user to enter any number.
Tell them whether the number is even or odd.
(Hint: Think about what the remainder means when dividing by 2.)
Odd / 2 = remainder 1
Even / 2 = remainder 0
"""
number = int(input("Enter a number: "))
if number % 2 == 1:
    print("Odd")
else:
    print("Even")
    
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