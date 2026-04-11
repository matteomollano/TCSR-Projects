# Question 1
# 1. Even or Odd Checker
# Ask the user to enter any number. Tell them whether the number is even or odd.
# (Hint: Think about what the remainder means when dividing by 2.)
try:
    number = int(input("Enter any number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("You must enter digits only (no letters).")
    
# Question 5
# 5. Find Highest Number
# Create a list of numbers.
# Then, use a for loop (Python) to find the highest number.
# Display the answer.
numbers = [24, 8, 76, 14, 25, 11, 17, 4, 7, 90, 31]
print(max(numbers)) # update to use a for loop next week