
import streamlit as st
import stripe
from inventory.models import Product
from decimal import Decimal

# Set your Stripe API key
stripe.api_key = st.secrets["stripe_secret_key"]

def create_checkout_session(product):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),  # Convert to cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=st.secrets["domain"] + '/success',
            cancel_url=st.secrets["domain"] + '/cancel',
        )
        return checkout_session
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

st.title("Inventory Management System")

# Sidebar for filtering
st.sidebar.title("Filters")
price_range = st.sidebar.slider("Price Range", 0, 1000, (0, 1000))

# Main content
products = Product.objects.filter(price__gte=price_range[0], price__lte=price_range[1])

for product in products:
    st.write(f"## {product.name}")
    st.write(f"Price: ${product.price}")
    st.write(f"Quantity Available: {product.quantity}")
    
    if st.button(f"Buy {product.name}"):
        checkout_session = create_checkout_session(product)
        if checkout_session:
            st.write("Redirecting to payment...")
            st.markdown(f"<a href='{checkout_session.url}' target='_blank'>Click here to complete payment</a>", unsafe_allow_html=True)

st.sidebar.markdown("### About")
st.sidebar.info("This is a simple inventory management system with Stripe payment integration.")
