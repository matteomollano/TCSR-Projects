import string, random

# name is a parameter (input you pass to a function)
def hello(name):
    print("hello", name)
    
hello("Taryn")

# calculate rectangle area
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(7, 4)
print(result)

# get the average from a list of numbers
# total and average are local variables (only known within the get_average() function)
def get_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

result = get_average([1, 500, 250, 999, 0])
print(result)

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(letters)
    return password

pass_length = int(input("Enter password length: "))
password = generate_password(pass_length)
print(password)