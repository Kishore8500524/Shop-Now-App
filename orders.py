import pyodbc

from db import get_connection
from datetime import datetime
import streamlit as st

def place_order(user_id, cart_items):
    conn = get_connection()
    cursor = conn.cursor()
    
    total = sum([item['price'] * item.get('quantity', 1) for item in cart_items])
    order_date = datetime.now()

    insert_query = """
    INSERT INTO Orders (user_id, total_amount, order_date)
    OUTPUT INSERTED.order_id
    VALUES (?, ?, ?)
    """

    order_id_row = cursor.execute(insert_query, (user_id, total, order_date)).fetchone()
    if not order_id_row or order_id_row[0] is None:
        raise Exception("Failed to retrieve order_id after insert.")

    order_id = order_id_row[0]
    print(f"Inserted order_id: {order_id}")  # Debug

    for item in cart_items:
        cursor.execute(
            "INSERT INTO OrderItems (order_id, product_id, price, quantity) VALUES (?, ?, ?, ?)",
            (order_id, item['product_id'], item['price'], item.get('quantity', 1))
        )

    conn.commit()
    return order_id
    
def get_order_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT o.order_id, o.order_date, o.total_amount, 
           p.name AS product_name, oi.quantity, oi.price
    FROM Orders o
    JOIN OrderItems oi ON o.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
    WHERE o.user_id = ?
    ORDER BY o.order_date DESC, o.order_id DESC
    """
    cursor.execute(query, user_id)
    
    results = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in results]
    





