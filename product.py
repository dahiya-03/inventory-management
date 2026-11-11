class Product:
    def __init__(self, name: str, price: float, quantity: int):
            
        if name.strip() :
            self.name = name.strip()
        else:
            raise  ValueError("Product name cannot be empty or contain only spaces.")
        
        if price > 0:
            self.price = price
        else:
            raise ValueError("Product price must be greater than zero.")
        
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Product quantity cannot be negative.")

    def calculate_stock_value(self) -> float:
        return self.price * self.quantity

    def show_details(self) -> None:
        print("---------------------------")
        print(f"Product name: {self.name}")
        print(f"Product price: ₹{self.price:.2f}")
        print(f"Product quantity: {self.quantity}")
        print(f"Total stock value: ₹{self.calculate_stock_value():.2f}")
        print("---------------------------\n")

