
from application.helper_functions import get_str,get_num
from application.menus import inventory_menu
def inventory_manager(products):
    inventory = create_inventory(products)
    while True:
        inventory_menu()
        menu_selection = input()
        match menu_selection:
            case "1":
                show_full_inventory(inventory)
            case "2":
                print(search_inventory(inventory))
            case "3":
                add_stock(inventory)
            case "4":
                remove_stock(inventory)
            case "5":
                show_out_of_stock(inventory)
            case "6":
                show_low_stock(inventory)
            case "7":
                return
            case _:
                print ("\nInvalid menu selection\n")

def show_low_stock(inventory:dict):
    for key, value in inventory.items():
        if  0 < value < 5:
            print (key)

def show_out_of_stock(inventory:dict):
    for key,value in inventory.items():
        if value == 0:
            print(key)
    
def remove_stock(inventory:dict):
    product_name = get_str("Enter product name: ")
    if not is_in_inventory(inventory,product_name):
        print ("No such item in inventory")
        return  
    amount = get_num(f"Enter the  amount you would like to add to {product_name}: ")
    if amount > inventory[product_name]:
        print ("dont have enough stock to remove that amount")
        return
    inventory[product_name] -= amount
    print(f"{amount} removed from stock. Item is now: {product_name} | {inventory[product_name]}")

def add_stock(inventory:dict):
    product_name = get_str("Enter product name: ")
    if not is_in_inventory(inventory,product_name):
        print ("No such item in inventory")
        return  
    amount = get_num(f"Enter the  amount you would like to add to {product_name}: ")
    inventory[product_name] += amount
    print(f"{amount} Added to item. Item is now: {product_name} | {inventory[product_name]}")
    
def is_in_inventory(inventory:list,product_name:str):
    if inventory.get(product_name,False):
        return True
    return False
 
def search_inventory(inventory:list):
    product_name = get_str("Enter product name: ").lower().strip()
    if is_in_inventory(inventory,product_name):
        return product_name,inventory[product_name]
    return "No such item in inventory"

def show_full_inventory(inventory:list):
    if not inventory:
        print ("no inventory")
    for product_name,stock in inventory.items():
        print(f"{product_name} | {stock}")
        
def create_inventory(products:list):
    return {product["name"].lower().strip(): product["stock"] for product in products}