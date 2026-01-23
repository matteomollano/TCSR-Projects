# Question 20.03
numbers = [1, 2, 3, 4, 5]
print(sum(numbers)/len(numbers))

# Question 20.05
for i in range(1, 101):
    if i % 3 != 0:
        print(i)
    
# Question 25.01    
decimal = 1.0
print(decimal.__class__)
print(type(decimal))

# Question 40.08
word = "condition"
letters = ["c", "o", "d", "e", "r"]
new_word = ""
# for letter in word:
#     if letter in letters:
#         new_word += letter
# print(new_word)

for i in range(len(word)):
    for j in range(len(letters)):
        if word[i] == letters[j]:
            new_word += word[i]
print(new_word)

# Question 70.01
word = input("Enter a word: ")
print(word[::-1] == word)