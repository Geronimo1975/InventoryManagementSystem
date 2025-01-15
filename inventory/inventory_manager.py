
import logging
from inventory.product import Product

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("inventory_manager")

class InventoryManager:
    """Class for managing inventory operations."""

    def __init__(self):
        """Initialize inventory manager with empty inventory."""
        self.inventory = {}

    def add_product(self, product: Product) -> None:
        """Add a product or update quantity if it exists."""
        if product.name in self.inventory:
            self.inventory[product.name].update_quantity(product.quantity)
        else:
            self.inventory[product.name] = product

    def remove_product(self, product_name: str) -> None:
        """Remove a product from inventory."""
        if product_name in self.inventory:
            del self.inventory[product_name]
            logger.info(f"Product '{product_name}' removed from inventory.")
        else:
            logger.info(f"Product '{product_name}' not found in inventory.")

    def update_quantity(self, product_name: str, quantity: int) -> None:
        """Update quantity of a product."""
        if product_name in self.inventory:
            self.inventory[product_name].update_quantity(quantity)
            logger.info(f"Updated quantity for '{product_name}'")
        else:
            logger.info(f"Product '{product_name}' not found in inventory.")

    def get_product_info(self, product_name: str) -> str:
        """Get information about a specific product."""
        if product_name in self.inventory:
            return self.inventory[product_name].get_product_info()
        return f"Product '{product_name}' not found in inventory."

    def get_total_inventory_value(self) -> float:
        """Calculate total value of inventory."""
        return sum(p.price * p.quantity for p in self.inventory.values())

    def list_all_products(self) -> None:
        """List all products in inventory."""
        if not self.inventory:
            logger.info("Inventory is empty.")
            return
            
        for product in self.inventory.values():
            logger.info(product.get_product_info())
