# Question 10.03
min = int(input("What is your starting value? "))
max = int(input("What is your ending value? "))
import random
print(random.randint(min, max))

# Question 20.06
for i in range(1, 11):
    print(i**2)
    
# Question 20.05
for i in range(1, 101):
    if i % 3 != 0:
        print(i)
        
# Question 30.02
sentence = "Simplicity is the soul of efficiency"
lst = sentence.split()
word_count = len(lst)
print(word_count)

# Question 30.01
number = 9876
# number = str(number)
# print(number[0])

while number >= 10:
    number = number // 10
print(number)