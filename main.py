from inventory.cart import Cart
from inventory.inventory_manager import InventoryManager
from inventory.product import Product


def main():
    # Create an InventoryManager instance
    inventory_manager = InventoryManager()

    # Create some products
    laptop = Product("Laptop", 1000.00, 5)
    smartphone = Product("Smartphone", 500.00, 10)
    laptop = Product("Laptop", 1000.00, 3)

    # Add products to inventory
    inventory_manager.add_product(laptop)
    inventory_manager.add_product(smartphone)
    inventory_manager.add_product(laptop)

    # Display product details
    print("Initial Inventory:")
    for product in inventory_manager.products:
        print(product.get_product_info())

    # Create a cart
    cart = Cart()
    cart.load_stock(inventory_manager.get_inventory_data())

    # Add items to the cart
    cart.add_to_cart(laptop, 2)
    cart.add_to_cart(smartphone, 3)
    cart.add_to_cart(smartphone, 1)

    # View cart details
    print("\nCart Details:")
    for item in cart.view_cart():
        print(item)

    # Calculate and display total inventory value
    print(
        f"\nTotal Inventory Value: {inventory_manager.get_total_inventory_value():.2f} €"
    )

    # Calculate and display cart total
    print(f"Total Cart Value: {cart.calculate_cart_total():.2f} €")

    print(inventory_manager.get_inventory_data())


if __name__ == "__main__":
    main()
