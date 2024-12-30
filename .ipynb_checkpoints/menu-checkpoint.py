# Starter code / Menu Printing (example)
menu_items = {
    1: {"Item name": "Apple",         "Price": 0.49},
    2: {"Item name": "Tea - Thai iced","Price": 3.99},
    3: {"Item name": "Fried banana",  "Price": 4.49}
}

# Print the sub-menu
print("---------- MENU ----------")
for key, value in menu_items.items():
    print(f"{key}. {value['Item name']} - ${value['Price']:.2f}")

# Create an empty list for storing the customer's order
order_list = []

# Variable to control if the customer wants to place an order
place_order = True

# Continuous ordering loop
while place_order:
    # Prompt the customer to enter their selection
    menu_selection = input("\nPlease enter the number of the item you'd like to order: ")
    
    # Validate that the selection is a number
    if not menu_selection.isdigit():
        print("Error: Please enter a valid number for your menu selection.")
        continue
    
    menu_selection = int(menu_selection)
    
    # Check if the selection is in the menu_items keys
    if menu_selection not in menu_items:
        print("Error: That item number is not on the menu.")
        continue
    
    # Retrieve the item name and price from menu_items
    item_name = menu_items[menu_selection]["Item name"]
    item_price = menu_items[menu_selection]["Price"]
    
    # Ask the customer for the quantity
    quantity_input = input(f"How many '{item_name}' would you like to order? ")
    
    # Validate the quantity
    if not quantity_input.isdigit():
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    else:
        quantity = int(quantity_input)
    
    # Append the order details to the order_list
    order_list.append({
        "Item name": item_name,
        "Price": item_price,
        "Quantity": quantity
    })
    
    # Ask if the customer would like to keep ordering
    while True:
        more_order = input("Would you like to keep ordering? (y/n): ")
        match more_order.lower():
            case 'y':
                place_order = True
                break  # break from this inner while loop
            case 'n':
                place_order = False
                print("Thank you for your order!")
                break  # break from this inner while loop
            case _:
                print("Invalid input. Please try again!")
    
# --------------------- PRINTING THE RECEIPT ---------------------
print("\n----------- ORDER RECEIPT -----------")
# Print the header
print("Item name                | Price  | Quantity")
print("-------------------------|--------|---------")

# Loop through each item in the order_list
for item in order_list:
    item_name  = item["Item name"]
    price      = item["Price"]
    quantity   = item["Quantity"]
    
    # Using formatted string widths for alignment:
    # - 24 characters for item_name, left-justified
    # - 6 characters for price, left-justified
    # - 8 characters for quantity, left-justified
    print(f"{item_name:24} | ${price:<5.2f}| {quantity:<2}")

# Calculate and print the total price
total_price = sum(i["Price"] * i["Quantity"] for i in order_list)
print("-------------------------------------")
print(f"Total Price: ${total_price:.2f}")
