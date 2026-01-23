score = 0

# Question 1
answer1 = input("1. What is the capital of New York? \na. Buffalo \nb. Albany \nc. Rochester \nd. Syracuse \nAnswer: ").lower()
if answer1 == "b" or answer1 == "albany":
    score += 1
    print("Correct! Good job")
else:
    print("Incorrect! The correct answer is b. Albany")
    
# Question 2
answer2 = input("\n2. Which state is the city of Knoxville found? \na. South Carolina \nb. Kentucky \nc. Missouri \nd. Tennessee \nAnswer: ").lower()
if answer2 == "d" or answer2 == "tennessee":
    score += 1
    print("Correct! Good job")
else:
    print("Incorrect! The correct answer is d. Tennessee")
   
# Question 3 
answer3 = input("\n3. What month does Mardi Gras usually take place? \na. December \nb. January \nc. February \nd. March \nAnswer: ").lower()
if answer3 == "c" or answer3 == "feb" or answer3 == "february":
    score += 1
    print("Correct! Good job")
else:
    print("Incorrect! The correct answer is c. February")
    
# Grade
if score <= 1:
    print(f"\nYour score is {score}. Better luck next time!")
elif score == 2:
    print(f"\nYour score is {score}. Decent effort!")
else:
    print(f"\nYour score is {score}. You did great! Awesome job!")