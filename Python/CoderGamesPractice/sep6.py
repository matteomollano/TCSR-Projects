# Question 20.04
for i in range(1, 100):
    if i % 8 != 0:
        print(i)
        
# Question 20.02
sum = 0
for i in range(10):
    x = input("Enter a single character or integer: ")
    if x.isdigit():
        sum = sum + int(x)
print(f"Sum: {sum}")

# Question 30.01
number = 5
factorial = 1
for i in range(number, 1, -1):
    factorial = factorial * i
print(f"{number}! = {factorial}")

# Question 50.04
num = int(input("Enter a positive integer: "))
remainder = num % 12

months = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

print(months[remainder])