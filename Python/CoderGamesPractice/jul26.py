# Question 30.07
for i in range(1, 101):
    if i % 3 == 0 and i % 4 == 0:
        print(i, "CoderSchool")
    elif i % 3 == 0:
        print(i, "Coder")
    elif i % 4 == 0:
        print(i, "School")
    else:
        print(i)
        
# Question 60.01
s = "python"
new_s = ""

for char in s:
    new_s += chr(ord(char) + 1)
    print(new_s)

# Question 90.01
num = 42
print(bin(num))