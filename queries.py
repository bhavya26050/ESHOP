import sqlite3

# Function to connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    return conn, cursor

# Function to close the database connection
def close_db(conn):
    conn.close()

# Joins
def perform_joins(cursor):
    # Inner Join between orders and users tables
    query = '''
    SELECT * FROM orders 
    INNER JOIN users ON orders.user_id = users.user_id
    '''
    cursor.execute(query)
    print("Inner Join between orders and users tables:")
    print(cursor.fetchall())

    # Left Join between product and categories tables
    query = '''
    SELECT * FROM product 
    LEFT JOIN categories ON product.category_id = categories.category_id
    '''
    cursor.execute(query)
    print("\nLeft Join between product and categories tables:")
    print(cursor.fetchall())

    # Right Join between reviews and product tables
    query = '''
    SELECT * FROM reviews 
    RIGHT JOIN product ON reviews.product_id = product.product_id
    '''
    cursor.execute(query)
    print("\nRight Join between reviews and product tables:")
    print(cursor.fetchall())

    # Full Outer Join between payment and users tables
    query = '''
    SELECT * FROM payment 
    LEFT JOIN users ON payment.user_id = users.user_id
    UNION
    SELECT * FROM payment 
    RIGHT JOIN users ON payment.user_id = users.user_id
    '''
    cursor.execute(query)
    print("\nFull Outer Join between payment and users tables:")
    print(cursor.fetchall())

    # Self Join on users table
    query = '''
    SELECT * FROM users u1
    INNER JOIN users u2 ON u1.email = u2.email AND u1.user_id <> u2.user_id
    '''
    cursor.execute(query)
    print("\nSelf Join on users table:")
    print(cursor.fetchall())

# Subqueries
def perform_subqueries(cursor):
    # Subquery to find orders with a total amount greater than the average amount
    query = '''
    SELECT * FROM orders 
    WHERE amount > (SELECT AVG(amount) FROM orders)
    '''
    cursor.execute(query)
    print("\nSubquery to find orders with a total amount greater than the average amount:")
    print(cursor.fetchall())

    # Subquery to find products with a quantity greater than the average quantity in their category
    query = '''
    SELECT * FROM product 
    WHERE quantity > (SELECT AVG(quantity) FROM product WHERE category_id = product.category_id)
    '''
    cursor.execute(query)
    print("\nSubquery to find products with a quantity greater than the average quantity in their category:")
    print(cursor.fetchall())

    # Subquery to find users who have placed at least two orders
    query = '''
    SELECT * FROM users 
    WHERE user_id IN (SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(*) >= 2)
    '''
    cursor.execute(query)
    print("\nSubquery to find users who have placed at least two orders:")
    print(cursor.fetchall())

    # Subquery to find categories with more than 10 products
    query = '''
    SELECT * FROM categories 
    WHERE category_id IN (SELECT category_id FROM product GROUP BY category_id HAVING COUNT(*) > 10)
    '''
    cursor.execute(query)
    print("\nSubquery to find categories with more than 10 products:")
    print(cursor.fetchall())

    # Subquery to find orders with a quantity greater than the average quantity in the product's category
    query = '''
    SELECT * FROM orders 
    WHERE quantity > (SELECT AVG(quantity) FROM product WHERE product_id = orders.product_id)
    '''
    cursor.execute(query)
    print("\nSubquery to find orders with a quantity greater than the average quantity in the product's category:")
    print(cursor.fetchall())

def main():
    conn, cursor = connect_db()

    # Perform Joins
    print("Performing Joins:")
    perform_joins(cursor)

    # Perform Subqueries
    print("\nPerforming Subqueries:")
    perform_subqueries(cursor)

    close_db(conn)

if __name__ == "__main__":
    main()
