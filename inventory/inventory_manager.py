from inventory.product import Product


class InventoryManager:
    def __init__(self):
        self.products = []

    # TODO Add to main branch
    def add_product(self, product: Product):
        try:
            for item in self.products:
                if item == product:
                    raise ValueError("Product already exists.")
            self.products.append(product)
        except ValueError as e:
            print(f"Error adding product:\n{e}\n")

    def remove_product(self, product_name: str):
        try:
            self.products = [
                p for p in self.products if p.name != product_name
            ]
        except Exception as e:
            print(f"Error removing product:\n{e}\n")

    # TODO Add to main branch
    def update_product_quantity(self, product_name: str, new_quantity: int):
        try:
            for product in self.products:
                if product.name == product_name:
                    product.update_quantity(new_quantity)
                    print(
                        f"Updated {product_name} quantity to {new_quantity}."
                    )
                else:
                    raise ValueError("Product not found.")
        except ValueError as e:
            print(f"Error:\n{e}\n")

    def get_product_info(self, product_name: str):
        try:
            for product in self.products:
                if product.name == product_name:
                    print(f"Product Name: {product.name}")
                    print(f"Price: ${product.price}")
                    print(f"Quantity: {product.quantity}")
                else:
                    raise ValueError("Product not found.")
        except ValueError as e:
            print(f"Error:\n{e}\n")

    def get_total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products)

    # TODO Add to main branch
    def get_inventory_data(self):
        stock_list = {}
        for item in self.products:
            stock_list[item.name] = {
                "quantity": item.quantity,
                "price": item.price,
            }
        return stock_list
