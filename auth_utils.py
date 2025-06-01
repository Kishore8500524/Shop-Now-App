from sqlalchemy import create_engine, text
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ⚠️ Replace this with your actual credentials for cloud-compatible DB
# Use SQL authentication (username and password) if deploying to cloud
engine = create_engine(
engine = create_engine("mssql+pytds://myuser:mypassword@192.168.1.6:1433/AMAZON")
)

def register_user(username, password):
    try:
        with engine.begin() as conn:
            result = conn.execute(text("SELECT username FROM Users WHERE username = :u"), {"u": username})
            if result.fetchone():
                return "Username already exists"

            hashed_pwd = hash_password(password)
            conn.execute(text("""
                INSERT INTO Users (username, password_hash, is_admin)
                VALUES (:u, :p, 0)
            """), {"u": username, "p": hashed_pwd})
            return "Success"
    except Exception as e:
        return str(e)

def login_user(username, password):
    try:
        hashed_pwd = hash_password(password)
        with engine.begin() as conn:
            result = conn.execute(text("""
                SELECT user_id, username, is_admin FROM Users
                WHERE username = :u AND password_hash = :p
            """), {"u": username, "p": hashed_pwd})
            row = result.fetchone()
            if row:
                return {"user_id": row[0], "username": row[1], "is_admin": row[2]}
            return None
    except Exception as e:
        print("Login error:", e)
        return None
