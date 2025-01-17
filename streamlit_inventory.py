import streamlit as st
import json
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from inventory.inventory_manager import InventoryManager
from inventory.product import Product
from inventory.cart import Cart
from inventory.export_manager import InventoryExporter
from inventory.user_manager import UserManager
from inventory.user import UserRole



def scrape_product_details(url):
    """Scrapes product details from an Amazon page using Selenium."""
    
    url = expand_short_url(url)  # Expand URL before scraping

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract product details
        product_name = soup.find("span", {"id": "productTitle"})
        product_price = soup.find("span", {"class": "a-offscreen"})

        name = product_name.text.strip() if product_name else "Unknown Product"
        price = product_price.text.strip() if product_price else "0,00 €"
        
        return name, price
    except Exception as e:
        print(f"Scraping error: {e}")
        return None, None
    finally:
        driver.quit()

def save_inventory(inventory_manager):
    with open("inventory.json", "w") as f:
        json.dump([p.__dict__ for p in inventory_manager.products], f)

def load_inventory(inventory_manager):
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            products = json.load(f)
            for p in products:
                inventory_manager.add_product(Product(p.get("name", "Unknown"), p.get("price", 0.0), int(p.get("quantity", 1))))

def format_price(price):
    """Format price as European currency (1.000,00 €)"""
    try:
        price = float(str(price).replace("€", "").replace(",", ".").strip())  # Convert to float safely
        return f"{price:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
    except ValueError:
        return "0,00 €"  # Fallback for invalid price values


def main():
    st.title("📦 Inventory Management System")
    
    inventory_manager = InventoryManager()
    cart = Cart()
    user_manager = UserManager()
    
    load_inventory(inventory_manager)
    
    st.sidebar.title("🔑 Authentication")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")
    
    if login_button:
        user = user_manager.authenticate_user(username, password)
        if user:
            st.sidebar.success(f"Logged in as: {user.role.value}")
            st.session_state["user"] = user
        else:
            st.sidebar.error("Invalid credentials!")
    
    if "user" not in st.session_state:
        st.warning("Please log in to access the system.")
        return
    
    user = st.session_state["user"]
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📦 Inventory", "🛒 Cart", "📤 Export", "💳 Payment", "📜 Order History"])
    
    with tab1:
        st.header("📦 Manage Inventory")
        
        if user.role == UserRole.ADMIN:
            with st.form("add_product_form"):
                name = st.text_input("Product Name", value="", help="Required field")
                price = st.number_input("Price", min_value=0.01, format="%.2f", help="Required field")
                quantity = st.number_input("Quantity", min_value=1, step=1, format="%d", help="Required field")
                affiliate_link = st.text_input("Affiliate Product Link", value="", help="Required field")
                add_product_button = st.form_submit_button("Add Product")
                
                if add_product_button:
                    if not name or not price or not quantity or not affiliate_link:
                        st.error("All fields are required. Please provide product name, price, quantity, and affiliate link.")
                    else:
                        product_name, product_price = scrape_product_details(affiliate_link)
                        if product_name and product_price:
                            new_product = Product(product_name, product_price, int(quantity))
                            inventory_manager.add_product(new_product)
                            save_inventory(inventory_manager)
                            st.success("Product added successfully from affiliate link!")
                        else:
                            st.error("Failed to fetch product details. Check the affiliate link.")
        
        st.subheader("Inventory List")
        product_data = [{"Name": p.name, "Price (€)": format_price(p.price), "Quantity": format(p.quantity)} for p in inventory_manager.products]
        if product_data:
            df = pd.DataFrame(product_data)
            #df.loc["Total", :] = ["Total Inventory Value", format_price(df["Price (€)"].str.replace(" €", "").str.replace(".", "").str.replace(",", ".").astype(float).sum()), df["Quantity"].sum()]
            st.table(df)
    
    with tab2:
        st.header("🛒 Shopping Cart")
        product_options = [p.name for p in inventory_manager.products]
        selected_product = st.selectbox("Select a product", product_options)
        quantity = st.number_input("Quantity", min_value=1, step=1, format="%d")
        add_to_cart_button = st.button("Add to Cart")
        
        if add_to_cart_button:
            product = next((p for p in inventory_manager.products if p.name == selected_product), None)
            if product:
                cart.add_to_cart(product, quantity)
                st.success(f"Added {quantity} {product.name} to cart.")
    
    with tab3:
        st.header("📤 Export Inventory")
        if st.button("Export to Excel"):
            excel_buffer = InventoryExporter.to_excel([p.__dict__ for p in inventory_manager.products])
            st.download_button("Download Excel", excel_buffer, file_name="inventory.xlsx")
    
    with tab4:
        st.header("💳 Payment")
        st.write("Payment functionality to be implemented")
    
    with tab5:
        st.header("📜 Order History")
        st.write("Order history functionality to be implemented")

def expand_short_url(short_url):
    try:
        response = requests.get(short_url, allow_redirects=True)
        return response.url  # Returns the final expanded URL
    except requests.RequestException as e:
        print(f"Error expanding URL: {e}")
        return short_url  # Fallback to original


if __name__ == "__main__":
    main()