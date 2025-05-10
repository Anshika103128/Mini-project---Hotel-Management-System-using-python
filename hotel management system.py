#Define the menu of restaurent
menu = {
    'Pizza':140,
    'Burger':120,
    'Pasta':160,
    'Salad':80,
    'French fries':100,
    'Coffe':70,
}

print(" Welcome to Tiyasa's restro")
print("Pizza: 140\nBurger: 120\nPasta: 160\nSalad :80\nFrench fries: 100\nCoffe: 70,")

order_total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been addded to your order")

else:
    print(f"Ordered item  is not available yet!")

another_order = input("Do you want to add another item in your current order ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been addded to your order")
    
else:
    print(f"Ordered item is not available yet!")

print(f"The total amount of items to pay is {order_total}")