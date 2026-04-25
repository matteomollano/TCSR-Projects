import random

print("Answer 10 multiplication questions")
print("Numbers will be between 1 and 12")
input("Press enter to start!")

score = 0
num_questions = 10

for i in range(1, num_questions + 1):
    print(f"\nQuestion #{i} of {num_questions}")
    
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    result = num1 * num2
    
    answer = input(f"What is {num1} x {num2}? ")
    if int(answer) == result:
        score += 1
        

percent = score / num_questions
percent = percent * 100
print(f"\nYou got {percent}%")

if percent == 100:
    print("Perfect score! You know your times tables! 🏆")
elif percent >= 75:
    print("Really well done! Keep it up! 🌟")
elif percent >= 50:
    print("Good effort! A bit more practice and you'll ace it! 💪")
else:
    print("Keep practising — you'll get there! 📚")