from application.menus import sales_menu,open_sale_menu
from application.helper_functions import get_num,get_str

def sales_manager(products:list):
    sales = []
    while True:
        sales_menu()
        menu_selection = get_num()
        match menu_selection:
            case 1:
                open_sale(products,sales)
            case 2:
                return
            case _:
                print("Invalid menu selection")

def open_sale(prodcuts:list,sales:list):
    cart = []
                
    while True:
        open_sale_menu()
        menu_selection = get_num()
        match menu_selection:
            case 1:
                add_item_to_cart(cart,prodcuts)
            case 2:
                update_item_quantity(cart)
            case 3:
                remove_item_from_cart(cart)
            case 4:
                print(calculate_total(cart))
            case 5:
                discount()
            case 6:
                complete_sale(cart,sales)
            case 7:
                return
            case _:
                print ("Invalid menu selection")
"""
sale = {
    "id": 1,
    "items": [
        {
            "product_id": 1,
            "name": "Gaming Mouse",
            "quantity": 2,
            "unit_price": 150.0,
            "total": 300.0
        }
    ],
    "subtotal": 300.0,
    "discount": 0.0,
    "total": 300.0
}
"""
def show_added_item(item):
    print (f"""
Product ID: {item["product_id"]}
Quantity: {item["quantity"]}

Added to Cart!

""")

def show_sale_summary(sale):
    print ("""
=====================
    SALE SUMMARY
=====================
    """)

    items = sale["items"]
    for item in items:
        print (f"{item["name"]}   {item["quantity"]} x {item["unit_price"]} = {item["total"]}")

    print ("""
------------------------------------
""")

def complete_sale(cart,sales):
    id = len(sales)+1
    total = calculate_total(cart) - discount()
    if total < 0:
        total = 0
    sale = {"id":id,"items":cart,"subtotal":calculate_total(cart),"discount":discount(),"total":total}
    sales.append(sale)
    print ("Sale Completed")

    return

    
def discount():
    discount = get_num("Enter discount amount")
    return discount

def calculate_total(cart):
    total = 0
    if not cart:
        print ("no items in cart")
        return
    for item in cart:
        total+= item["total"]
    return total

def remove_item_from_cart(cart):
    item_name = get_str("Enter item name: ").strip().lower()
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            return
    print ("No such item in cart")

def update_item_quantity(cart):
    item_name = get_str("Enter item name: ").strip().lower()
    for item in cart:
        if item["name"] == item_name:
            quantity = get_num("enter updated quantity")
            item["quantity"] = quantity
            item["total"] = quantity*item["unit_price"]
            print("Quantity updated")

def add_item_to_cart(cart,products):
    item_name = get_str("Enter Item name: ").strip().lower()
    if not does_exist(products,item_name):
        print ("no such item exists")
        return
    quantity = get_num("Enter quantity: ")
    if not enough_available_stock(products,item_name,quantity):
        print (f"not enough available {item_name} in stock")
        return
    
    for product in products:
        if product["name"].strip().lower() == item_name:
            item = {"product_id":product["id"],"name":product["name"],"quantity":quantity,"unit_price":product["price"],"total":product["price"]*quantity}
            cart.append(item)
    show_added_item(item)


def does_exist(products,item_name):
    for product in products:
        if product["name"].strip().lower() == item_name:
            return True
    return False

def enough_available_stock(products,item_name,quantity):
    for product in products:
        if  product["name"].strip().lower() == item_name:
            if product["stock"] <= quantity:
                return True
    return False