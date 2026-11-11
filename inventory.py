from product import Product
import json

class Inventory:
    def __init__(self) -> None:
        self.products : list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def show_all_products(self) -> None:
        if not self.products :
            print("No products available.")
        else:
            for product in self.products:
                product.show_details()

    def search_product(self, name: str) -> Product | None:
        product_name = name.lower().strip()
        if not product_name:
            return None
        
        for product in self.products:
            if product.name.lower().strip() == product_name:
                return product    
        return None

    def update_quantity(self, name: str, new_quantity: int) -> bool:
        if new_quantity < 0:
            raise ValueError("Product quantity cannot be negative")
         
        product = self.search_product(name)
        if product is not None:
            product.quantity = new_quantity
            return True
        return False

    def delete_product(self, name: str) -> bool:
        product = self.search_product(name)
        if product is not None:
            self.products.remove(product)
            return True
        return False
    
    def calculate_total_inventory_value(self) -> float:
        total = 0
        for product in self.products:
            total += product.calculate_stock_value()
        return total

    def show_low_stock_products(self, threshold: int = 3) -> None:
        if threshold < 0:
            raise ValueError("Threshold cannot be negative.")
        found = False
        for product in self.products:
            if product.quantity < threshold:
                found = True
                product.show_details()
        if not found:
            print("No low-stock products found")

    def save_to_file(self, filename: str = "products.json") -> None:
        data = []
        for product in self.products:
            product_data={"name":product.name, "price":product.price, "quantity":product.quantity}
            data.append(product_data)
        with open(filename,"w") as file:
            json.dump(data,file,indent=4)

    def load_from_file(self, filename: str = "products.json") -> None:
        try:
            with open(filename,"r") as file:
                data = json.load(file)
                loaded_product = []
                for item in data:
                    name = item["name"]
                    price = item["price"]
                    quantity = item["quantity"]
                    product_data = Product(name,price,quantity)
                    loaded_product.append(product_data)
                self.products = loaded_product
                print("Inventory loaded successfull")
        except FileNotFoundError:
            print("No saved inventory found.")