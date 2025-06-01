import streamlit as st
import hashlib
from db import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)",
                       (username, hash_password(password)))
        conn.commit()
        st.success("✅ Registration successful!")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username=? AND password_hash=?", 
                   (username, hash_password(password)))
    return cursor.fetchone()
