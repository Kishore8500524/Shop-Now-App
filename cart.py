import streamlit as st
from orders import place_order

def initialize_cart():
    if 'cart' not in st.session_state:
        st.session_state.cart = []

def add_to_cart(product):
    for item in st.session_state.cart:
        if item['product_id'] == product['product_id']:
            item['quantity'] += 1
            st.success(f"🛒 Increased quantity of {product['name']} to {item['quantity']}!")
            return
    cart_item = product.copy()
    cart_item['quantity'] = 1
    st.session_state.cart.append(cart_item)
    st.success(f"🛒 Added {product['name']} to cart!")

def print_invoice(cart_items):
    st.subheader("🧾 Invoice Summary")
    total = 0
    for item in cart_items:
        name = item['name']
        price = item['price']
        quantity = item.get('quantity', 1)
        line_total = price * quantity
        st.write(f"{name} - ₹{price:.2f} x {quantity} = ₹{line_total:.2f}")
        total += line_total
    st.markdown(f"**Total: ₹{total:.2f}**")

def view_cart():
    st.header("🛍️ Your Cart")

    if not st.session_state.cart:
        st.info("🛒 Your cart is empty.")
        return

    total = 0
    for item in st.session_state.cart:
        price_total = item['price'] * item['quantity']
        st.write(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{price_total:.2f}")
        total += price_total

    st.markdown(f"**Total: ₹{total:.2f}**")

    # Button to show invoice
    if st.button("🧾 Print Invoice"):
        print_invoice(st.session_state.cart)

    # Button to place order
    if st.button("✅ Checkout"):
        order_id = place_order(st.session_state.user['user_id'], st.session_state.cart)
        if order_id:
            st.success(f"✅ Order #{order_id} placed successfully!")
            st.session_state.cart = []
        else:
            st.error("❌ Failed to place order.")
