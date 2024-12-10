from inventory.product import Product


class InventoryManager:
    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        The inventory is a dictionary where keys are product names and
        values are Product objects.
        """
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
            print(f"Product '{product_name}' not found in inventory.")

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
            print(f"Product '{product_name}' not found in inventory.")

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
        List all products in the inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for product_name, product in self.inventory.items():
                print(product.get_product_info())
