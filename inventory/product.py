class Product:
    """
    A class to represent a product in the inventory system.
    Each product has a name, price, and quantity in stock.
    """
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        # # Check for invalid inputs
        # if not name:
        #     raise ValueError("Product name cannot be empty.")
        # if not isinstance(price, (int, float)):
        #     raise ValueError("Price must be a number.")
        # if not isinstance(quantity, int):
        #     raise ValueError("Quantity must be an integer.")

        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.name = name.strip()
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int):
        """
        Update the quantity of the product.

        Args:
            amount (int): The amount to add (positive) or subtract (negative)
                        from the current quantity.

        Raises:
            ValueError: If the resulting quantity is negative.
        """
        if self.quantity + amount < 0:
            raise ValueError(f"Insufficient stock to remove {abs(amount)} items. Current stock: {self.quantity}.")
        self.quantity += amount

    def update_price(self, new_price: float):
        """
        Update the price of the product.

        Args:
            new_price (float): The new price of the product.

        Raises:
            ValueError: If the new price is negative.
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

    def get_product_info(self) -> str:
        """
        Get a string representation of the product's information.

        Returns:
            str: The product details including name, price, and quantity.
        """
        return (
            f"Product Name: {self.name}\n"
            f"Price (per unit): ${self.price:.2f}\n"
            f"Quantity in Stock: {self.quantity}"
        )

    def calculate_total_value(self) -> float:
        """
        Calculate the total value of the product based on its price and quantity.

        Returns:
            float: The total monetary value of the product.
        """
        return self.price * self.quantity

    def __str__(self):
        """
        Override the string representation of the product.

        Returns:
            str: A one-line summary of the product's details.
        """
        return f"{self.name} - ${self.price:.2f} - Qty: {self.quantity}"

    def __eq__(self, other):
        """
        Compare two products for equality based on their name.

        Args:
            other (Product): The other product to compare.

        Returns:
            bool: True if the names are equal (case insensitive), False otherwise.
        """
        if isinstance(other, Product):
            return self.name.lower() == other.name.lower()
        return False

    def __hash__(self):
        """
        Generate a hash for the product based on its name, making it usable in sets or as dictionary keys.

        Returns:
            int: The hash value.
        """
        return hash(self.name.lower())
