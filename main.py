from application.products import product_manager
from application.inventory import inventory_manager
from application.sales import sales_manager
from application.menus import main_menu
def main():
    products = [
    {
        "id": 1,
        "name": "Gaming Mouse",
        "category": "Gaming",
        "price": 150.0,
        "stock": 20,
        "active": True },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "category": "Accessories",
        "price": 350.0,
        "stock": 0,
        "active": True
    }
]
    main_menu()
    product_manager(products)
    inventory_manager(products)
    sales_manager(products)

if __name__ == "__main__":
    main()