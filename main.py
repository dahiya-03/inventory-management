from product import Product
from inventory import Inventory
import logging



logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Inventory Management System started.")
inventory = Inventory()
inventory.load_from_file()

while True:
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Show All Products")
    print("2. Add New Product")
    print("3. Search Product")
    print("4. Update Product Quantity")
    print("5. Delete Product")
    print("6. Calculate Total Inventory Value")
    print("7. Show Low-Stock Products")
    print("8. Exit")

    try:
        choice : int = int(input("Enter your choice: "))


        if choice == 1:
            inventory.show_all_products()

        elif choice == 2:
            try:
                name: str = input("Enter Product name: ")
                price: float = float(input("Enter Product price: "))
                quantity: int = int(input("Enter Product quantity: "))
                product = Product(name, price, quantity)
                inventory.add_product(product)
                logging.info(f"Product added: {product.name}.")
                print("Product added successfully.")
            except ValueError as error:
                logging.exception(f"Failed to add product: {error}")
                print("Error: ",error)

        elif choice == 3:
            name: str = input("Enter Product name: ")
            result =inventory.search_product(name)
            if result is not None:
                result.show_details()
            else:
                print("Product not found.")
                logging.warning(f"Product not found: {name}")

        elif choice == 4:
            try:
                name: str = input("Enter Product name: ")
                new_quantity: int = int(input("Enter New quantity: "))
                result = inventory.update_quantity(name,new_quantity)
                if result:
                    logging.info(f"Product '{name}'quantity updated to {new_quantity}.")
                    print("Product quantity updated successfully.")
                else:
                    print(f"Product '{name}' not found.")
            except ValueError as error:
                logging.exception(f"Failed to update quantity: {error}")
                print("Error: ",error)

        elif choice == 5:
            name: str = input("Enter Product name: ")
            result = inventory.delete_product(name)
            if result:
                logging.info(f"Product: {name} deleted successfully.")
                print("Product deleted successfully.")
            else:
                logging.warning(f"Product: {name} not found.")
                print("Product not found.")

        elif choice == 6:
            stock_value = inventory.calculate_total_inventory_value()
            print(f"Total Inventory Value: ₹{stock_value:.2f}")

        elif choice == 7:
            try:
                threshold = int(input("Enter the Stock threshold: "))
                inventory.show_low_stock_products(threshold)
            except ValueError as error:
                print("Error: ",error)

        elif choice == 8:
            try:
                inventory.save_to_file()
                logging.info("Inventory saved successfully.")
                logging.info("Inventory Management System closed.")
                print("Exiting Inventory Management System...")
                break
            except OSError as error:
                print("File not saved. Pleae try again")
                logging.exception("Failed to save inventory: ",error)

        else:
            print("Invalid choice. Please select an option between 1 and 8.")

    except ValueError:
        print("Invalid input. Please enter a number from 1-8")


