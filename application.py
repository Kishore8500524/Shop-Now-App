import streamlit as st
from models import get_all_products

st.title("🛍️ MyShop - E-Commerce Store")

st.header("Available Products")
products = get_all_products()

for product in products:
    pid, name, price, stock = product
    st.subheader(name)
    st.write(f"💲 Price: ₹{price}")
    st.write(f"📦 In stock: {stock}")
    st.button(f"🛒 Add to Cart", key=pid)
