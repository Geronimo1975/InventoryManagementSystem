# test

import logging
from inventory.product import Product

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('inventory_manager')  # Ensure the logger name matches the test case


class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product: Product):
        """
        Add a new product to the inventory. If the product already exists, 
        increase its quantity.

        Args:
            product (Product): The product to be added.
        """
        if product.name in self.inventory:
            self.inventory[product.name].update_quantity(product.quantity)
        else:
            self.inventory[product.name] = product

    def remove_product(self, product_name: str):
        """
        Remove a product from the inventory by its name.

        Args:
            product_name (str): Name of the product to remove.
        """
        if product_name in self.inventory:
            del self.inventory[product_name]
        else:
            logger.info(f"Product '{product_name}' not found in inventory.")

    def update_quantity(self, product_name: str, quantity: int):
        """
        Update the quantity of an existing product.

        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity to update (can be positive or negative).
        """
        if product_name in self.inventory:
            self.inventory[product_name].update_quantity(quantity)
        else:
            logger.info(f"Product '{product_name}' not found in inventory.")

    def get_product_info(self, product_name: str) -> str:
        """
        Retrieve the information of a product.

        Args:
            product_name (str): Name of the product.

        Returns:
            str: The product information, or a message if not found.
        """
        if product_name in self.inventory:
            return self.inventory[product_name].get_product_info()
        return f"Product '{product_name}' not found in inventory."

    def get_total_inventory_value(self) -> float:
        """
        Calculate the total value of the inventory.

        Returns:
            float: Total value of all products in the inventory.
        """
        total_value = 0.0
        for product in self.inventory.values():
            total_value += product.price * product.quantity
        return total_value

    def list_all_products(self):
        """
        List all products in the inventory using logging.
        """
        if not self.inventory:
            logger.info("Inventory is empty.")
        else:
            for product_name, product in self.inventory.items():
                logger.info(product.get_product_info())
