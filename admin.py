import streamlit as st
import os
from db import get_connection

def admin_panel():
    st.header("🛠️ Admin Panel")

    name = st.text_input("Product Name")
    description = st.text_area("Description")
    price = st.number_input("Price", step=1.0)
    category = st.text_input("Category")
    stock = st.number_input("Stock", step=1)
    image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if st.button("Add Product"):
        image_path = None
        if image:
            os.makedirs("product_images", exist_ok=True)
            image_path = f"product_images/{image.name}"
            with open(image_path, "wb") as f:
                f.write(image.getbuffer())
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Products (name, description, price, category, stock, image_path) VALUES (?, ?, ?, ?, ?, ?)",
            (name, description, price, category, stock, image_path)
        )
        conn.commit()
        st.success("✅ Product added successfully!")
