class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")
        self.name = name.strip()
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int):
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to remove.")
        self.quantity += amount

    def get_product_info(self) -> str:
        return f"Product Name: {self.name}\nPrice (per unit): ${self.price:.2f}\nQuantity in Stock: {self.quantity}"

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Qty: {self.quantity}"
