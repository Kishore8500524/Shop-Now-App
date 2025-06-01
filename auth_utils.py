import pyodbc
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=KISHORE\\SQLEXPRESS;"
            "Database=AMAZON;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        # Check if username exists
        cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
        if cursor.fetchone():
            return "Username already exists"
        hashed_pwd = hash_password(password)
        cursor.execute("INSERT INTO Users (username, password_hash, is_admin) VALUES (?, ?, ?)",
                       (username, hashed_pwd, False))
        conn.commit()
        return "Success"
    except Exception as e:
        return str(e)

def login_user(username, password):
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=KISHORE\\SQLEXPRESS;"
            "Database=AMAZON;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        hashed_pwd = hash_password(password)
        cursor.execute("SELECT user_id, username, is_admin FROM Users WHERE username = ? AND password_hash = ?",
                       (username, hashed_pwd))
        row = cursor.fetchone()
        if row:
            return {"user_id": row[0], "username": row[1], "is_admin": row[2]}
        else:
            return None
    except Exception as e:
        print("Login error:", e)
        return None
