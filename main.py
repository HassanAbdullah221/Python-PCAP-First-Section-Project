from restaurant import chef

menu = {
    "Pizza": {"name": "Pizza", "price": 12.99},
    "Pasta": {"name": "Pasta", "price": 9.99},
    "Salad": {"name": "Salad", "price": 6.99},
    "Burger": {"name": "Burger", "price": 10.49},
    "Soup": {"name": "Soup", "price": 5.50},
}

print('''

        Welcome to Abo Youseef Restaurant
    

    This is the menu:


''')

while True:
    chef.display_menu(menu)

    welcom = int(input('''
    Select the type of service:
                
            1- Add a dish
            2- Remove a dish
            3- Update a price
            4- Place an order
            5- View menu
            6- exit
        Your Select: '''))
    
    if welcom == 6:
        print("bey")
        break

    elif welcom == 1:
        add = input("Enter dish name: ")
        price = float(input("Enter dish price: "))
        chef.add_dish(menu, add, price)


    elif welcom == 2:
        remove = input("Enter dish name to remove: ")
        chef.remove_dish(menu, remove)

    elif welcom == 3:
        name = input("Enter dish name to update price: ")
        new_price = float(input("Enter new price: "))
        chef.update_price(menu, name, new_price)

    elif welcom == 4:
        order = input("Enter dish name to order: ")
        chef.place_order(menu, order)

    elif welcom == 5:
        chef.display_menu(menu)