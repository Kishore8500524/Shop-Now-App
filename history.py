import streamlit as st
from orders import get_order_history
from collections import defaultdict

def view_order_history():
    st.header("📜 Order History")

    user_id = st.session_state.user['user_id']
    history = get_order_history(user_id)

    if not history:
        st.info("No orders found.")
        return

    grouped_orders = defaultdict(list)
    for row in history:
        grouped_orders[row['order_id']].append(row)

    for order_id, items in grouped_orders.items():
        st.subheader(f"🧾 Order #{order_id} - {items[0]['order_date'].strftime('%Y-%m-%d %H:%M')}")
        total = 0
        for item in items:
            line_total = item['price'] * item['quantity']
            st.write(f"{item['product_name']} - ₹{item['price']} x {item['quantity']} = ₹{line_total:.2f}")
            total += line_total
        st.markdown(f"**Total: ₹{total:.2f}**")
        st.markdown("---")
