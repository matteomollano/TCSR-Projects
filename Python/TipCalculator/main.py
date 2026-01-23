bill_amount = input("Enter your bill amount: ")

while bill_amount.isnumeric() == False:
    bill_amount = input("You must enter a number: ")
    
tip_choice = input("What tip do you want to give?\na) 18%\nb) 20%\nc) 22%\nd) 24%\nEnter a, b, c, or d: ").lower().strip()

while tip_choice not in ['a', 'b', 'c', 'd']:
    tip_choice = input("Enter a, b, c, or d only: ").lower().strip()