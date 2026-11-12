
from application.helper_functions import get_str
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
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                return
            case _:
                print ("\nInvalid menu selection\n")


def search_inventory(inventory:list):
    product_name = get_str("Enter product name: ")
    for item in inventory:
        print (item.keys())
        if product_name.strip().lower == (key.strip().lower() for key in item):
            return item
    return "No such item in inventory"


def show_full_inventory(inventory:list):
    if not inventory:
        print ("no inventory")
    for item in inventory:
        print (item)
        
def create_inventory(products:list):
    inventory = []
    if not products:
        return None
    for product in products:
        if product ["stock"] > 0:
            inventory.append({product["name"]:product["stock"]})
    return inventory
    


def inventory_menu():
    print("""
------------------------
    INVENTORY MENU
------------------------
Choose Option:

1. Show full Inventory
2. Search product in inventory
3. Add units to inventory
4. Remove units from inventory
5. Show products that are out of stock
6. Show low stock prodcuts
7. Return to main menu
""")