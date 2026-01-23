def question9():
    """
    9. Hide Credit Card Number
    Ask the user to enter a 16 digit credit card number (add validation to ensure the input is the right length and no letters
    Replace all digits but the last 4 with asterisks (*)
    Display the new credit card number
    """
    ccn = input("Enter credit card number: ")
    while len(ccn) != 16 or ccn.isdigit() == False:
        if len(ccn) != 16:
            print("Wrong length. Enter 16 numbers")
        if ccn.isdigit() == False: # this means ccn contains letters
            print("Credit card number cannot contain letters. Numbers only.")
        ccn = input("Enter credit card number: ")
    
    print("*" * 12 + ccn[12:16]) # string slice, sub-string

def question10():
    """
    10. Friday the 13th Detector
    Create a date object for the 13th day of a given month and year.
    The year and month should be received as input (month is an integer between 1 and 12)
    Return True if the day falls on a Friday, return False otherwise
    Hint: Use Python datetime module (Monday is 1 and Sunday is 7 in this library)
    """
    from datetime import datetime
    
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    day = 13
    
    date = datetime(year, month, day)
    print(date)
    weekday = date.isoweekday()
    
    if weekday == 5: # 5 is Friday
        return True
    else:
        return False
    
result = question10()
print(result)