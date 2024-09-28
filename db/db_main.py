import sqlite3
from db import querries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')


        cursor.execute(querries.CREATE_TABLE_PRODUCTS)
        db.commit()

async def sql_insert_products(fullname, category, size_product, price, product_id, photo):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(querries.INSERT_PRODUCTS_QUERY, (
            fullname,
            category,
            size_product,
            price,
            product_id,
            photo
        ))
        db_with.commit()