import sqlite3

# Connect to the SQLite database (creates a new database if not exists)
conn = sqlite3.connect('supermarket.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS address (
    user_id TEXT PRIMARY KEY,
    street_address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    pin_code INTEGER NOT NULL,
    country TEXT NOT NULL
);''')

# Create the categories table
cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
    category_id TEXT PRIMARY KEY,
    category_name TEXT NOT NULL
);''')

# Create the orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    product_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    date_ordered DATE NOT NULL
);''')

# Create the payment table
cursor.execute('''CREATE TABLE IF NOT EXISTS payment (
    payment_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    order_id TEXT NOT NULL,
    payment_date DATE NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT NOT NULL
);''')

# Create the product table
cursor.execute('''CREATE TABLE IF NOT EXISTS product (
    product_id TEXT PRIMARY KEY,
    category_id TEXT NOT NULL,
    product_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    quantity INTEGER NOT NULL
);''')

# Create the reviews table
cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
    review_id TEXT PRIMARY KEY,
    product_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    rating INTEGER NOT NULL
);''')

# Create the users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    mobile_no TEXT NOT NULL,
    billing_address TEXT NOT NULL
);''')

cursor.execute("INSERT INTO address (user_id, street_address, city, state, pin_code, country) VALUES ('1001', '123 Elm Street', 'New York', 'NY', 10001, 'USA');")

cursor.execute("INSERT INTO address (user_id, street_address, city, state, pin_code, country) VALUES ('1002', '456 Oak Avenue', 'Los Angeles', 'CA', 90001, 'USA');")

cursor.execute("SELECT * FROM address")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Commit the changes
conn.commit()

# Fetch and print data from the table


# Close the cursor and connection
cursor.close()
conn.close()
