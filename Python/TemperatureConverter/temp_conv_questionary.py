import questionary

while True:
    choice = questionary.select(
        "Do you want to convert from Celsius or from Fahrenheit?",
        ["Celsius", "Fahrenheit"]
    ).ask()

    if choice == "Celsius":
        celsius_temp = int(input("Enter a celsius temperature: "))
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        print(f"The fahrenheit temp is {fahrenheit_temp}")
        
    else:
        fahrenheit_temp = int(input("Enter a fahrenheit temperature: "))
        celsius_temp = (fahrenheit_temp - 32) / (9/5)
        print(f"The celsius temperature is {celsius_temp}")
        
    play_again = questionary.select(
        "Do you want to enter another temperature?",
        ["Yes", "No"]
    ).ask()
    
    if play_again == "Yes":
        print()
    else:
        break
