# dictionary practice
a = {1:"A", 2:"B", 3:"C"}
print(a.items())

for k, v in a.items():
    print(k, v)

a = {}
a[2] = 1 
a[1] = [2, 3, 4]
# what a looks like now
a = {2:1, 1:[2, 3, 4]}

print(a[1][1]) # prints 3

# string contains
s1 = "apples"
s2 = "apple"
print(s2 in s1)

# THESE TWO QUESTIONS NEED TO BE ALTERED FOR FUTURE QUIZZES
# To check whether string s1 contains another string s2, use:
# Answer: s1_contains_(s2) NOT RIGHT
# print(s1__contains__(s2))

# What will be the output of the following code?
# a = {} a[2] = 1 a[1] = [2, 3, 4] print(a[1][1])

# string methods
print("abcdef".find("cd"))
print("ab,12".isalnum())

number = "$400,000,000"
number = number.replace("$", "")
number = number.replace(",", "")
number = float(number)
print(number)

# floor division
nums = [1, 2, 3, 4, 5, 6, 7]
print(len(nums) // 2)

# bit shifting
x = 1
print(x << 2)