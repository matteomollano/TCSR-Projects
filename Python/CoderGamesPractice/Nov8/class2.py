import random

def question5():
    """
    5. Find Highest Number
    Create a list of numbers.
    Then, use a for loop to find the highest number.
    Display the answer.
    """
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 100))
    print(numbers)
    
    # x = 0
    # for number in numbers:
    #     if number > x:
    #         x = number
    # print(x)
    
    # for i in range(len(numbers)):
    #     if numbers[i] > x:
    #         x = numbers[i]
    # print(x)
    
    print(max(numbers))
    
def question6():
    """
    6. Swap Values
    Create two variables, a and b, that are integer values.
    For example:
    a = 10
    b = 20
    Swap their values so that in the example above, a becomes 20 and b becomes 10.
    """
    a = 10
    b = 20
    
    # c = b
    # b = a
    # a = c
    
    a, b = b, a
    print(a)
    print(b)

def question7():
    """
    7. Letter Frequency Counter
    Ask the user to enter a sentence.
    Then, display how many of each letter is present in the sentence.
    """
    sentence = input("Enter a sentence: ")
    # loop over every letter
    # if letter is not in the dictionary, add it with a value of 1
    # if letter is in the dictionary, update it by 1
    letter_count = {} # apple
    for letter in sentence:
        if letter == " ":
            continue
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print(letter_count)
            
def question8():
    """
    8. Factorial Finder
    Ask the user for a positive integer n.
    Calculate n! (n factorial)
    n! = n x (n-1) x (n-2) x … x 1
    5! = 5 * 4 * 3 * 2 = 120
    """
    integer = int(input("Please enter a positive integer: "))
    for i in range(integer-1, 1, -1):
        integer = integer * i
    print(integer)

def factorial(number):
    # base case
    # if n < 0, then error
    # if n is 0, 0! = 1
    if number < 0:
        return "Number must be positive."
    if number == 0: # 0! = 1
        return 1
    return number * factorial(number-1)