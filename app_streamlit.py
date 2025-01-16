# streamlit run app_streamlit.py
# http://localhost:8501
# exit: Ctrl+C


import streamlit as st
from inventory.product import Product
from inventory.inventory_manager import InventoryManager
from inventory.cart import Cart

def init_data():
    """
    Initializes an InventoryManager, creates some sample products,
    and returns both the manager and a Cart object.
    """
    inventory_manager = InventoryManager()
    cart = Cart()

    # Create a few sample products
    product1 = Product("Laptop", 1000.00, 5)
    product2 = Product("Smartphone", 500.00, 10)

    # Add them to the inventory
    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)

    return inventory_manager, cart


LIGHT_THEME ='
    <style>
        body {
    color: #000000;
    background-color: #FFFFFF;
        }
    </style>
    '

DARK_THEME = '
<style>
body {
    color: #FFFFFF;
    background-color: #262730;
}
</style>
'

def main():
    st.title("Simple Inventory Management System")

    st.title("Simple Inventory Management System with Theme Toggle")

    # Theme radio
    theme_choice = st.radio("Select Theme:", ["Light", "Dark"])

    if theme_choice == "Light":
        st.markdown(LIGHT_THEME, unsafe_allow_html=True)
    else:
        st.markdown(DARK_THEME, unsafe_allow_html=True)

    st.write("Check whether theme toggles between light and dark.")
    
    # Initialize data in session state
    if "inventory_manager" not in st.session_state:
        st.session_state["inventory_manager"], st.session_state["cart"] = init_data()

    inventory_manager = st.session_state["inventory_manager"]
    cart = st.session_state["cart"]

    # Section to add products to inventory
    st.subheader("Add Products to Inventory")
    product_name = st.text_input("Product Name:", "")
    product_price = st.number_input("Product Price:", value=0.0, step=0.01)
    product_quantity = st.number_input("Product Quantity:", value=0, step=1)

    if st.button("Add Product"):
        if product_name and product_price > 0 and product_quantity > 0:
            new_product = Product(product_name, product_price, product_quantity)
            inventory_manager.add_product(new_product)
            st.success(f"Product '{product_name}' has been added to the inventory!")
        else:
            st.warning("Please enter a valid name, a price > 0, and a quantity > 0.")

    st.write("---")

    # Display current inventory
    st.subheader("Current Inventory:")
    if inventory_manager.products:
        for product in inventory_manager.products:
            st.write(product.get_product_info())
    else:
        st.write("The inventory is empty.")

    # Update product quantity
    st.subheader("Update Product Quantity")
    update_name = st.text_input("Product Name to Update:", "")
    update_quantity = st.number_input("New Quantity:", value=0, step=1)

    if st.button("Update Quantity"):
        if update_name:
            success = inventory_manager.update_product_quantity(update_name, update_quantity)
            if success:
                st.success(f"The quantity of product '{update_name}' has been updated to {update_quantity}.")
            else:
                st.warning(f"Product '{update_name}' was not found.")

    # Remove a product
    st.subheader("Remove a Product from Inventory")
    delete_name = st.text_input("Product Name to Remove:", "")
    if st.button("Remove Product"):
        product_names_before = [p.name for p in inventory_manager.products]
        if delete_name in product_names_before:
            inventory_manager.remove_product(delete_name)
            st.success(f"Product '{delete_name}' has been removed from the inventory.")
        else:
            st.warning(f"Product '{delete_name}' does not exist in the inventory.")

    st.write("---")

    # Display total inventory value
    st.subheader("Total Inventory Value")
    total_value = inventory_manager.get_total_inventory_value()
    st.write(f"Total value: **{total_value:.2f}**€")

    st.write("---")

    # Cart Section
    st.subheader("Shopping Cart Management")

    cart_product_name = st.text_input("Product Name to Add to Cart:", "")
    cart_quantity = st.number_input("Quantity to Add to Cart:", value=1, step=1)

    if st.button("Add to Cart"):
        found_product = None
        for p in inventory_manager.products:
            if p.name == cart_product_name:
                found_product = p
                break
        if found_product:
            cart.add_to_cart(found_product, cart_quantity)
            st.success(f"Product '{cart_product_name}' added to cart ({cart_quantity} unit(s)).")
        else:
            st.warning(f"Product '{cart_product_name}' does not exist in the inventory.")

    # Display cart contents
    st.write("**Cart Contents:**")
    cart_items_list = cart.view_cart()
    if cart_items_list:
        for item_desc in cart_items_list:
            st.write(item_desc)
    else:
        st.write("The cart is empty.")

    # Remove from cart
    remove_from_cart_name = st.text_input("Product Name to Remove from Cart:", "")
    if st.button("Remove from Cart"):
        cart.remove_from_cart(remove_from_cart_name)
        st.info(f"Product '{remove_from_cart_name}' has been removed from the cart (if it was there).")

    # Calculate and display cart total
    cart_total = cart.calculate_cart_total()
    st.write(f"**Cart Total Value:** {cart_total:.2f} €")


if __name__ == "__main__":
    main()