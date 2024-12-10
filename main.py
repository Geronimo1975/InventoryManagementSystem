from inventory.product import Product
from inventory.inventory_manager import InventoryManager


def main():
    """
    Main function to demonstrate the Inventory Management System.
    """
    # Create an instance of InventoryManager
    inventory_manager = InventoryManager()

    # Add some products
    product1 = Product(name="Laptop", price=1500.00, quantity=10)
    product2 = Product(name="Mouse", price=25.00, quantity=50)
    product3 = Product(name="Keyboard", price=45.00, quantity=30)

    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)
    inventory_manager.add_product(product3)

    # Display all products
    print("Current Inventory:")
    inventory_manager.list_all_products()
    print()

    # Update product quantity
    print("Updating product quantity:")
    inventory_manager.update_quantity("Laptop", -2)  # Sell 2 laptops
    inventory_manager.update_quantity("Mouse", 10)   # Add 10 mice
    print()

    # Get product info
    print("Product Info for 'Laptop':")
    print(inventory_manager.get_product_info("Laptop"))
    print()

    # Get total inventory value
    print("Total Inventory Value:")
    total_value = inventory_manager.get_total_inventory_value()
    print(f"${total_value:.2f}")
    print()

    # Remove a product
    print("Removing 'Keyboard' from inventory.")
    inventory_manager.remove_product("Keyboard")
    print()

    # Display updated inventory
    print("Updated Inventory:")
    inventory_manager.list_all_products()

if __name__ == "__main__":
    main()
