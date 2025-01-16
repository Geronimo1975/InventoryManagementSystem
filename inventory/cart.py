from inventory.inventory_manager import InventoryManager
from inventory.product import Product


class Cart:
    def __init__(self):
        self.cart_items = {}

    # TODO Add
    def add_to_cart(self, product: Product, quantity: int):
        self.cart_items[product] = {
            "product": product,
            "quantity": quantity,
        }

    def remove_from_cart(self, product_name: str):
        try:
            if product_name in self.cart_items:
                del self.cart_items[product_name]
                print(f"Removed {product_name} from cart.")
            else:
                raise KeyError("Product not found in cart.")
        except KeyError as e:
            print(e)

    def view_cart(self):
        # Return a list of item descriptions for readability
        return [
            f"{item['product'].get_product_info()}, In Cart: {item['quantity']}"
            for item in self.cart_items.values()
        ]

    def calculate_cart_total(self):
        return sum(
            item["product"].price * item["quantity"]
            for item in self.cart_items.values()
        )
