from inventory.product import Product
from inventory.inventory_manager import InventoryManager

def main():
    manager = InventoryManager()

    # Add products
    manager.add_product(Product("Laptop", 1500.00, 10))
    manager.add_product(Product("Mouse", 25.00, 50))

    # List products
    manager.list_all_products()

    # Get total value
    print(f"Total Inventory Value: ${manager.get_total_inventory_value():.2f}")

if __name__ == "__main__":
    main()
