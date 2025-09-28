def add_dish(menu, name, price):
    if name in menu:
        print("the ",name,"already in the menu.")
    else:
        menu[name] = {'name': name, 'price': price}
        print("Dish '",name,"' added successfully.")

def remove_dish(menu, name):
    if name in menu:
        del menu[name]
        print("Dish '",name,"' removed successfully.")
    else:
        print("Dish '",name,"' does not exist in the menu.")

def update_price(menu, name, new_price):
    if name in menu:
        menu[name]['price'] = new_price
        print("Price of '",name,"' updated to ",new_price,".")
    else:
        print("Dish '",name,"' does not exist in the menu.")

def place_order(menu, name):
    if name not in menu:
        print("Dish '",name,"' does not exist in the menu.")
    else:
        print("Order placed for '",name,"'. Preparing now...")

def display_menu(menu):
    if not menu:
        print("The menu is empty.")
        return
    else:
        print(menu)