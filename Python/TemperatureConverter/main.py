while True:
    choice = input("Do you want to convert to Celsius or Fahrenheit (c/f)? ")
    temp = int(input("Enter temperature value: "))

    if choice == "f":
        f = temp * 9/5 + 32
        print(temp, "degrees C = ", f, "degrees F")
    elif choice == "c":
        c = (temp - 32) * 5/9
        print(temp, "degrees F = ", c, "degrees C")
    else:
        print("Invalid choice. Enter f or c only.")
    print()