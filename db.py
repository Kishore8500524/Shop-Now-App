import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=KISHORE\\SQLEXPRESS;"
            "Database=AMAZON;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print(f"❌ Could not connect to the database. Error: {e}")
        return None
