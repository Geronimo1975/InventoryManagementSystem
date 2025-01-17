class Product:
    def __init__(self, name, price, quantity, image_url=""):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image_url = image_url

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_product_info(self):
        # Format price with two decimals
        return f"Product: {self.name}, Price: {self.price:.2f}€, Quantity: {self.quantity:.2f}"
