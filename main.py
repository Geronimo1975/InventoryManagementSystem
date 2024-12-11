from inventory.inventory_manager import InventoryManager

# Initialize InventoryManager
inventory_manager = InventoryManager()


def register_user():
    """Register a new user."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(f"User '{username}' registered successfully!")


def login_user():
    """Login an existing user."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(f"Welcome back, {username}!")


def show_inventory():
    """Display the list of available products."""
    print("\nAvailable products:")
    inventory_manager.list_all_products()


def add_product_to_cart():
    """Add a product to the shopping cart."""
    product_name = input("Enter the product name to add to cart: ")
    if product_name in inventory_manager.inventory:
        quantity = int(input(f"Enter the quantity of {product_name}: "))
        inventory_manager.update_quantity(product_name, -quantity)
        print(f"Added {quantity} of {product_name} to your cart.")
    else:
        print(f"Product '{product_name}' not found.")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. View Inventory")
        print("4. Add Product to Cart")
        print("5. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            register_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            show_inventory()
        elif choice == 4:
            add_product_to_cart()
        elif choice == 5:
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
