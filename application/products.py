from application.helper_functions import get_str,get_num
def product_manager(products:list):
    while True:
        show_product_menu()
        menu_selection = get_str()
        match menu_selection:
            case "1":
                add_product(products)
            case "2":
                display_all_products(products)
            case "3":
                search_product(products)
            case "4":
                update_product(products)
            case "5":
                delete_product(products)
            case "6":
                 return
            case _:
                print ("Invalid menu selction. Try again: ")


def delete_product(products):
    product_id = get_num("Enter product id: ")
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return
    print ("No product with that id")

def update_product(products):
    product_id = get_num("Enter product id to update: ")

    desired_product = None
    for product in products:
        if product["id"] == product_id:
            desired_product = product
            break
    if desired_product == None:
        print ("no product with this id")
        return
    
    update_product_menu()
    menu_selection = input("Enter menu selection: ")
    match menu_selection:
        case "1":
            new_name = get_str("enter new name: ","str")
            product["name"] = new_name
            return
        case "2":
            new_category = get_str("enter new category: ", "str")
            product["category"] = new_category
            return
        case "3":
            new_price = get_num("enter new price: ")
            product["price"] = new_price
            return
        case "4":
            product["status"] = not product["status"]
            return

def update_product_menu():
    print ("""
--- UPDATE PRODUCT ---
1. name
2. category
3. price
4. status
""")

def search_product(products):
    search_product_menu()
    while True:
        menu_selection = get_str("Enter Menu Selection: ")
        match menu_selection:
            case "1":
                print(search_product_in_inventory(products,"id"))
                break
            case "2":
                print(search_product_in_inventory(products,"name"))
                break
            case "3":
                print(search_product_in_inventory(products,"category"))
                break
            case _:
                print ("invalid menu selection")
            
def search_product_in_inventory(products,search_type):
    if search_type == "id":
        id = get_num("Enter id: ")
        for product in products:
            if product[search_type] == id:
                return product
        return "no product with that id"
        
    if search_type == "name":
        name = get_str("Enter name: ")
        for product in products:
            if product[search_type] == name:
                return product
    else:
        category = get_str("enter category: ")
        searched_products = []
        for product in products:
            if product[search_type] == category:
                searched_products.append(product)
        return searched_products


def search_product_menu():
    print ("""
--- SEARCH PRODUCT BY ---
1. id
2. name
3. category
""")
    
def display_all_products(products):
    if not products:
        print ("No products")
    for product in products:
        if product["active"]:
            print (product)

def add_product(products:list):
    product_name,category,price,starting_stock = get_product_details()
    new_id = len (products)+1
    product = {"id":new_id,"name":product_name,"category":category,"price": price,"stock":starting_stock,"active":True}
    products.append(product)
        
def get_product_details():
    product_name = get_str("Enter product name: ")
    category = get_str("Enter product category: ")
    price = get_num("Enter price: ")
    starting_stock = get_num("Enter starting stock: ")
    return product_name,category,price,starting_stock

def show_product_menu():
    print ("""
--------- PRODUCTS MANAGEMENT ---------

1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
""")