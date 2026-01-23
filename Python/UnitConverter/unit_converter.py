# parameter: input to a function
def convert_temperature():
  print("1. Celsius to Fahrenheit")
  print("2. Fahrenheit to Celsius")
  choice = input("Choose 1 or 2: ")
  while choice not in ["1", "2"]:
    choice = input("Invalid choice. Enter 1 or 2 only: ")
  value = float(input("Enter temperature value: "))
  
  if choice == "1":
    F = value * 9/5 + 32
    print(value, "°C =", F, "°F")
  elif choice == "2":
    C = value - 32 * 5/9
    print(value, "°F =", C, "°C")

def convert_weight():
  print("1. Kilograms to Pounds")
  print("2. Pounds to Kilograms")
  choice = input("Choose 1 or 2: ")
  while choice not in ["1", "2"]:
    choice = input("Invalid choice. Enter 1 or 2 only: ")
  value = float(input("Enter weight value: "))
  
  if choice == "1":
    pounds = value * 2.205
    print(value, "kg =", pounds, "lbs")
  elif choice == "2":
    kilograms = value / 2.205
    print(value, "lbs =", kilograms, "kg")

def convert_length():
  print("1. Meters to Kilometers")
  print("2. Kilometers to Meters")
  print("3. Feet to Miles")
  print("4. Miles to Feet")
  choice = input("Choose 1-4: ")
  while choice not in ["1", "2", "3", "4"]:
    choice = input("Invalid choice. Enter 1, 2, 3, or 4 only: ")
  value = int(input("Enter value to convert: "))
  
  if choice == '1':
    km = value / 1000
    print(value, "meters =", km, "kilometers")
  elif choice == '2':
    meters = value * 1000
    print(value, "kilometers =", meters, "meters")
  elif choice == '3':
    miles = value / 5280
    print(value, "feet =", miles, "miles")
  elif choice == '4':
    feet = value * 5280
    print(value, "miles =", feet, "feet")

def main():
    while True:
        print("---- Unit Converter ----")
        print("1. Convert Temperature")
        print("2. Convert Weight")
        print("3. Convert Length")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("\nConverting Temperature")
            convert_temperature()
        elif choice == '2':
            print("\nConverting Weight")
            convert_weight()
        elif choice == '3':
            print("\nConverting Length")
            convert_length()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid selection")
        print()

if __name__ == "__main__":
    main()