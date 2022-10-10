import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS order_items (
 id INTEGER PK PRIMARY KEY,
 order_id INTEGER FK NOT NULL UNIQUE,
 product_id INTEGER FK NOT NULL UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS products(
id INTEGER PK PRIMARY KEY,
title VARCHAR(36),
description VARCHAR(140),
category_id INTEGER FK
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
id INTEGER PK PRIMARY KEY,
name VARCHAR(24) UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PK PRIMARY KEY,
user_id INTEGER,
status_id INTEGER
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS statuses(
id INTEGER PK PRIMARY KEY,
name VARCHAR(10) UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
 id INTEGER PK PRIMARY KEY,
 name varchar(24) NOT NULL,
 email varchar(24) NOT NULL UNIQUE
);
''')
conn.commit()

cur.execute('''
SELECT name, email FROM users WHERE name = 'petya'
            ''')