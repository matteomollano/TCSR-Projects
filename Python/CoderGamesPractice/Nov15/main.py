def question3():
    """
    3. Multiplication Table Maker
    Ask the user for a number (for example, 5).
    Then show that number's multiplication table from 1 through 12.
    (Example: 
    5 x 1 = 5
    5 x 2 = 10,
    5 x 3 = 15,
    5 x 4 = 20, 
    …)
    """
    number = int(input("Enter a number between 1 and 12: "))
    # repeat 12
    for i in range(1, 13):
        print(number, "x", i, "=", number * i)

def question4():
    """
    4. The Temperature Converter
    Ask the user to enter a temperature in Celsius.
    Convert it to Fahrenheit using the formula:
    F = (C x 9/5) + 32
    Then display the result.
    (Bonus: allow conversion in both directions!)
    """
    temp = float(input("Enter a temperature in Celsius: "))
    # float is decimal
    f = temp * 9/5 + 32
    print(temp, "degrees C =", f, "degrees F")
    
question4()