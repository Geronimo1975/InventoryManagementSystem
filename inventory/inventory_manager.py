import logging
from inventory.product import Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("inventory_manager")

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product: Product):
        if product.name in self.inventory:
            self.inventory[product.name].update_quantity(product.quantity)
        else:
            self.inventory[product.name] = product

    def remove_product(self, product_name: str):
        if product_name in self.inventory:
            del self.inventory[product_name]
        else:
            logger.info(f"Product '{product_name}' not found in inventory.")

    def update_quantity(self, product_name: str, quantity: int):
        if product_name in self.inventory:
            self.inventory[product_name].update_quantity(quantity)
        else:
            logger.info(f"Product '{product_name}' not found in inventory.")

    def get_product_info(self, product_name: str) -> str:
        if product_name in self.inventory:
            return self.inventory[product_name].get_product_info()
        return f"Product '{product_name}' not found in inventory."

    def get_total_inventory_value(self) -> float:
        return sum(p.price * p.quantity for p in self.inventory.values())

    def list_all_products(self):
        if not self.inventory:
            logger.info("Inventory is empty.")
        for product in self.inventory.values():
            logger.info(product.get_product_info())
