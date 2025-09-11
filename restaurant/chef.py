from tabulate import tabulate


def add_dish(menu: dict, name: str, price: float):
    if name in menu:
        print("This dish already exists in the menu!")
        return
    
    menu[name] = (price, True)
    print(f"Added {name} to the menu!")

def remove_dish(menu: dict, name: str):
    if name not in menu:
        print("This dish doesn't exist in the menu!")
        return
    
    del menu[name]
    print("Item deleted successfully!")

def update_price(menu: dict, name: str, price: float):
    if name not in menu:
        print("This item doesn't exist!")
        return
    
    menu[name] = (price, menu[name][1])
    print("Price changed successfully!")

def place_order(menu: dict, name: str):
    if name not in menu:
        print("We don't sell this item!")
        return
    if menu[name][1] == False:
        print("This item is currently unavailable!, sorry! :(")

    menu[name] = (menu[name][0], False)
    print("Thank you for submitting your order!, It will be ready shortly! :)")

def display_menu(menu: dict):
    headers = ["Item", "Price", "Availability"]


    print(tabulate([[key, *value] for key, value in menu.items()], headers, tablefmt="github"))



