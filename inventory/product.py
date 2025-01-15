
class Product:
    """Class representing a product in the inventory system."""
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        """Initialize a new product."""
        self._validate_inputs(price, quantity)
        self.name = name.strip()
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int) -> None:
        """Update product quantity, ensuring it doesn't go below zero."""
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to remove.")
        self.quantity += amount

    def get_product_info(self) -> str:
        """Return formatted product information."""
        return (
            f"Product Name: {self.name}\n"
            f"Price (per unit): ${self.price:.2f}\n"
            f"Quantity in Stock: {self.quantity}"
        )

    def _validate_inputs(self, price: float, quantity: int) -> None:
        """Validate price and quantity inputs."""
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")

    def __str__(self) -> str:
        """Return string representation of the product."""
        return f"{self.name} - ${self.price:.2f} - Qty: {self.quantity}"
