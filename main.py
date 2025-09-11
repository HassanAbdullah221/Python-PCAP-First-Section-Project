from restaurant import chef

menu = dict()
while True:
    print("Hello and welcome to the restaurant!, please pick from the actions below.")
    res = input("1. add dish\n2. remove dish\n3. update price\n4. place order\n5. display the current menu\n")
    if res not in "12345" or res == '':
        print("Invalid option, please try again! :(")
        continue
    res = int(res)
    if res == 1:
        name = input("Please specify the name of the dish you want to add: ")
        price = input("Please specify the price of the dish you want to add: ")
        try:
            price = float(price)
        except:
            print("The price is invalid please enter a valid price!")
            continue

        chef.add_dish(menu, name, price)
    elif res == 2:
        name = input("Please specify the name of the dish you want to remove: ")
        chef.remove_dish(menu, name)
    elif res == 3:
        name = input("Please specify the name of the dish you want to update the price of: ")
        price = input("Please specify the new price: ")
        try:
            price = float(price)
        except:
            print("The new price is invalid please enter a valid price!")
        
        chef.update_price(menu, name, price)
    elif res == 4:
        name = input("Please specify the name of the dish you want to order: ")
        chef.place_order(menu, name)
    else:
        print("This is the current menu!")
        chef.display_menu(menu)

        