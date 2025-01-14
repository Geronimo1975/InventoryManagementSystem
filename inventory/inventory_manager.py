from inventory.product import Product

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_name: str):
        self.products = [
            p for p in self.products
            if p.name != product_name
        ]

    def update_product_quantity(self, product_name: str, new_quantity: int):
        for product in self.products:
            if product.name == product_name:
                product.update_quantity(new_quantity)
                return True
        return False

    def get_product_info(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product.get_product_info()
        return "Product not found."

    def get_total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products)
