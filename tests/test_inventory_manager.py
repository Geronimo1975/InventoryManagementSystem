import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()

    def test_add_product(self):
        product = Product("Laptop", 1500.00, 10)
        self.manager.add_product(product)
        self.assertIn("Laptop", self.manager.inventory)

    def test_remove_product(self):
        product = Product("Mouse", 20.00, 5)
        self.manager.add_product(product)
        self.manager.remove_product("Mouse")
        self.assertNotIn("Mouse", self.manager.inventory)

    def test_update_quantity(self):
        product = Product("Keyboard", 50.00, 15)
        self.manager.add_product(product)
        self.manager.update_quantity("Keyboard", 5)
        self.assertEqual(self.manager.inventory["Keyboard"].quantity, 20)

    def test_get_total_inventory_value(self):
        product1 = Product("Laptop", 1500.00, 5)
        product2 = Product("Mouse", 25.00, 40)
        self.manager.add_product(product1)
        self.manager.add_product(product2)
        self.assertEqual(self.manager.get_total_inventory_value(), 1500 * 5 + 25 * 40)
