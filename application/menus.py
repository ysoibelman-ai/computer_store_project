def main_menu():
    print ("""
=================================
       COMPUTER STORE SYSTEM
=================================

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit

Choose an option:
""")

# Product

def product_menu():
    print ("""
--------- PRODUCTS MANAGEMENT ---------

1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
""")
def update_product_menu():
    print ("""
--- UPDATE PRODUCT ---
1. name
2. category
3. price
4. status
""")
    
def search_product_menu():
    print ("""
--- SEARCH PRODUCT BY ---
1. id
2. name
3. category
""")

# Inventory

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

# Sales
def sales_menu():
    print("""
=====================
      SALES MENU
=====================
Choose Option:

1. Open Sale
2. Return to main menu
""")
    
def open_sale_menu():
    print ("""
=======================
     OPEN SALE MENU
=======================
Choose Option:

1. Add item to cart
2. Update item quantity
3. Remove item from cart
4. Calculate total
5. Discount
6. Complete sale
7. Return to main menu
""")