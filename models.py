from db import get_connection

def get_all_products(category=None, keyword=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT product_id, name, description, price, category, stock, image_url FROM Products WHERE 1=1"
    params = []
    if category:
        query += " AND category = ?"
        params.append(category)
    if keyword:
        query += " AND name LIKE ?"
        params.append(f"%{keyword}%")
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    # Convert rows to list of dicts for convenience
    products = []
    for row in rows:
        products.append({
            "product_id": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "category": row[4],
            "stock": row[5],
            "image_url": row[6],
        })
    return products
