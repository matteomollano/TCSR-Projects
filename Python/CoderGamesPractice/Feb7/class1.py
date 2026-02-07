# Question 1
# 4. The Temperature Converter
# Ask the user to enter a temperature in Celsius.
# Convert it to Fahrenheit using the formula:
# F = (C × 9/5) + 32
# Then display the result.
# (Bonus: allow conversion in both directions!)

# str -> "Hello"
# int -> 5
# float -> 5.4
# boolean -> True/False
# char -> 'c'

c = float(input("Enter a temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c} degrees Celsius = {f} degrees Fahrenheit")


# Question 2
# 5. Find Highest Number
# Create a list of numbers.
# Then, use a for loop (Python) to find the highest number.
# Display the answer.

numbers = [345, 78, 235, 329085, 234, 390, 13, 4, 11, 2345]

# Steps
# 1. Use a variable (max_num) to keep track of largest number
# 2. Compare each number to max_num
# 3. If number > max_num, then update max_num to that number

# Option 1:
max_num = 0

for i in range(0, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        
print("Using for loop:", max_num)

# Option 2:
print("Using max():", max(numbers))


# Question 3
# 6. Swap Values
# Create two variables, an and b, that are integer values.
# For example:
# a = 10
# b = 20
# Swap their values so that in the example above, a becomes 20 and b becomes 10.
a = 10
b = 20

# Option 1
temp = a
a = b
b = temp

print(a)
print(b)

# Option 2
a, b = b, a