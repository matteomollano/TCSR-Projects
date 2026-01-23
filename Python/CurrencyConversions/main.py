import questionary

us_dollars = float(input("Enter an amount in US Dollars ($): "))
currency = questionary.select("Which currency do you want to convert to?", ["Japanese Yen", "Vietnamese Dong", "Afghan Afghani", "Chinese Yuan"]).ask()

if currency == "Japanese Yen":
    japanese_yen = us_dollars * 160.88
    print(f"${us_dollars} = ¥{japanese_yen}") # $100 = ¥16088.00
elif currency == "Vietnamese Dong":
    vietnamese_dong = us_dollars * 25455
    print(f"${us_dollars} = {vietnamese_dong}₫")
elif currency == "Afghan Afghani":
    afghan = us_dollars * 71.06
    print(f"${us_dollars} = {afghan}؋")
else:
    yuan = us_dollars * 7.27
    print(f"${us_dollars} = {yuan}¥")
