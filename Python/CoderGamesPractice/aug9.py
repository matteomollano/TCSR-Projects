# Challenge Question 50.03
number = int(input("Enter a number: "))
print(number % 7)

if number == 0:
    print("Sunday")
elif number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
    
# Challenge Question 40.01
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
lst = set(lst)
print(lst)

# Challenge Question 90.01
decimal = 42
binary = ""
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    binary = str(remainder) + binary
print(binary)