CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    fullname VARCHAR(255),
    category VARCHAR(255),
    size_product VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""

INSERT_PRODUCTS_QUERY = """
    INSERT INTO products_info (fullname, category, size_product, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""