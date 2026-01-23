# french fries, s/m/l drink, milkshake, ice cream, chicken nuggets, mozzarella sticks, pasta, hamburger, rice
food_items = {
    "1": {"name": "Chicken Nuggets", "price": 4.00},
    "2": {"name": "French Fries", "price": 2.50},
    "3": {"name": "Hamburger", "price": 5.00},
    "4": {"name": "Pasta", "price": 5.50},
    "5": {"name": "Rice", "price": 4.00},
    "6": {"name": "Mozzarella Sticks", "price": 3.00},
    "7": {"name": "Small Drink", "price": 1.25},
    "8": {"name": "Medium Drink", "price": 1.50},
    "9": {"name": "Large Drink", "price": 1.75},
    "a": {"name": "Milkshake", "price": 3.50},
    "b": {"name": "Ice Cream", "price": 2.75}
}

def display_menu():
    print("---------- MENU ----------")
    for id, food_item in food_items.items():
        name = food_item["name"]
        price = food_item["price"]
        
        # print(f"{id}. {name} - ${price:.2f}")
        print(str(id) + ". " + name + " - $" + "{:.2f}".format(price))

# if the order contains any characters that aren't 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b
# validate_order = function name, order = parameter
def validate_order(order):
    for char in order:
        if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']:
            return False
    return True

# create and print the customer's receipt
# def create_receipt(order):
#     items = {}
#     for char in order:
#         food_item = food_items[char]
#         name = food_item["name"]
#         price = food_item["price"]
#         if name not in items:
#             items[name] = {"price": price, "quantity": 1}
#         else:
#             items[name]['price'] += price
#             items[name]['quantity'] += 1
    
#     print("\n---------- RECEIPT ----------")   
#     for name, obj in items.items():
#         price = obj['price']
#         quantity = obj['quantity']
#         print(str(quantity) + "x " + name + " -- ${:.2f}".format(price))
        
# calculate and display the total for the order
def display_total(order):
    total_cost = 0
    for char in order:
        food = food_items[char]
        price = food['price']
        total_cost += price

    print("Your total cost is", "${:.2f}".format(total_cost))
    
def create_receipt(order):
    items = {}
    # 11223 
    # char = 1
    for char in order:
        food = food_items[char]
        name = food['name']
        price = food['price']
        
        if name not in items:
            # creating a new key in items
            items[name] = {'price': price, 'quantity': 1}
        else: # if the item already exists in the dictionary
            items[name]['quantity'] += 1
    
    print("---------- RECEIPT ----------")
    for key, value in items.items():
        price = value['price']
        quantity = value['quantity']
        print(str(quantity) + "x", key, "->", "${:.2f}".format(price*quantity))
        
    
while True:
    display_menu()
    order = input("\nPlace your order: ")
    while validate_order(order) == False:
        order = input("Invalid order. Please re-enter your order: ")

    create_receipt(order)
    display_total(order)
    
    # 11233
    # Receipt
    # 2x Chicken Nuggets - $8.00
    # 1x French Fries - $2.50
    # 2x Hamburger - $10
    # Total Cost - $20.50

    # Do you want to change your order?
    change_order = input("Do you want to change your order? (y/n): ").lower()
    if change_order == 'y':
        continue
    else:
        print("Thank you for placing an order with us!\n")

    another_order = input("Do you want to make another order? (y/n): ").lower()
    if another_order != 'y':
        break
    else:
        print()