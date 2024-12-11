import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()

    def test_list_all_products_empty(self):
        """
        Test listing all products when the inventory is empty.
        """
        with self.assertLogs('inventory_manager', level='INFO') as captured_logs:
            self.inventory_manager.list_all_products()
        self.assertIn("Inventory is empty.", captured_logs.output[0])

    def test_list_all_products(self):
        """
        Test listing all products in the inventory.
        """
        product1 = Product(name="Laptop", price=1500.00, quantity=10)
        product2 = Product(name="Mouse", price=25.00, quantity=50)
        self.inventory_manager.add_product(product1)
        self.inventory_manager.add_product(product2)

        with self.assertLogs('inventory_manager', level='INFO') as captured_logs:
            self.inventory_manager.list_all_products()
        self.assertIn("Product Name: Laptop", captured_logs.output[0])
        self.assertIn("Product Name: Mouse", captured_logs.output[1])
