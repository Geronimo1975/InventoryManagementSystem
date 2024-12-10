import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager

class TestInventoryManagement(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up a fresh InventoryManager instance before each test.
        """
        self.inventory_manager = InventoryManager()

    def test_add_product(self) -> None:
        """
        Test adding a product to the inventory.
        """
        product = Product(name="Laptop", price=1500.00, quantity=10)
        self.inventory_manager.add_product(product)
        self.assertIn("Laptop", self.inventory_manager.inventory)
        self.assertEqual(self.inventory_manager.inventory["Laptop"].quantity, 10)

    def test_get_product_info(self) -> None:
        """
        Test retrieving product information.
        """
        product = Product(name="Laptop", price=1500.00, quantity=10)
        self.inventory_manager.add_product(product)
        product_info = self.inventory_manager.get_product_info("Laptop")
        self.assertIn("Laptop", product_info)
        self.assertIn("$1500.00", product_info)

    def test_update_quantity(self) -> None:
        """
        Test updating the quantity of a product.
        """
        product = Product(name="Laptop", price=1500.00, quantity=10)
        self.inventory_manager.add_product(product)
        self.inventory_manager.update_quantity("Laptop", 5)
        self.assertEqual(self.inventory_manager.inventory["Laptop"].quantity, 15)

        # Test reducing quantity to below zero
        with self.assertRaises(ValueError):
            self.inventory_manager.update_quantity("Laptop", -20)

    def test_get_product_quantity(self) -> None:
        """
        Test retrieving the quantity of a specific product.
        """
        product = Product(name="Laptop", price=1500.00, quantity=10)
        self.inventory_manager.add_product(product)
        quantity = self.inventory_manager.inventory["Laptop"].quantity
        self.assertEqual(quantity, 10)

    def test_remove_product(self) -> None:
        """
        Test removing a product from the inventory.
        """
        product = Product(name="Laptop", price=1500.00, quantity=10)
        self.inventory_manager.add_product(product)
        self.inventory_manager.remove_product("Laptop")
        self.assertNotIn("Laptop", self.inventory_manager.inventory)

    def test_search_product(self) -> None:
        """
        Test searching for a product by name.
        """
        product = Product(name="Laptop", price=1500.00, quantity=10)
        self.inventory_manager.add_product(product)
        product_info = self.inventory_manager.get_product_info("Laptop")
        self.assertIn("Laptop", product_info)

        # Test searching for a nonexistent product
        product_info = self.inventory_manager.get_product_info("NonexistentProduct")
        self.assertEqual(product_info, "Product 'NonexistentProduct' not found in inventory.")

    def test_get_total_inventory_value(self) -> None:
        """
        Test calculating the total value of the inventory.
        """
        product1 = Product(name="Laptop", price=1500.00, quantity=10)
        product2 = Product(name="Mouse", price=25.00, quantity=50)
        self.inventory_manager.add_product(product1)
        self.inventory_manager.add_product(product2)
        total_value = self.inventory_manager.get_total_inventory_value()
        self.assertEqual(total_value, 1500.00 * 10 + 25.00 * 50)

    def test_generate_inventory_product_list(self) -> None:
        """
        Test generating a product list from the inventory.
        """
        product1 = Product(name="Laptop", price=1500.00, quantity=10)
        product2 = Product(name="Mouse", price=25.00, quantity=50)
        self.inventory_manager.add_product(product1)
        self.inventory_manager.add_product(product2)

        # Check if products are correctly logged
        with self.assertLogs('inventory_manager', level='INFO') as captured_logs:
            self.inventory_manager.list_all_products()
        self.assertIn("Product Name: Laptop", captured_logs.output[0])
        self.assertIn("Product Name: Mouse", captured_logs.output[1])

if __name__ == "__main__":
    unittest.main()
