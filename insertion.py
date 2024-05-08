import sqlite3


def connect_db():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    return conn, cursor


def close_db(conn):
    conn.close()


def insert_data(conn, cursor):
    
    cursor.execute("INSERT INTO address VALUES ('1', '123 Street', 'City', 'State', 12345, 'Country')")
    cursor.execute("INSERT INTO address VALUES ('2', '456 Avenue', 'Town', 'Province', 54321, 'Nation')")

    # Insert into categories table
    cursor.execute("INSERT INTO categories VALUES ('1', 'Electronics')")
    cursor.execute("INSERT INTO categories VALUES ('2', 'Clothing')")

    # Insert into orders table
    cursor.execute("INSERT INTO orders VALUES ('1', '101', '201', 2, '2024-03-25')")
    cursor.execute("INSERT INTO orders VALUES ('2', '102', '202', 3, '2024-03-26')")

    # Insert into payment table
    cursor.execute("INSERT INTO payment VALUES ('1', '201', '1', '2024-03-25', 100.00, 'Credit Card')")
    cursor.execute("INSERT INTO payment VALUES ('2', '202', '2', '2024-03-26', 150.00, 'PayPal')")

    # Insert into product table
    cursor.execute("INSERT INTO product VALUES ('101', '1', 'Laptop', 800, 10)")
    cursor.execute("INSERT INTO product VALUES ('102', '2', 'T-Shirt', 20, 50)")

    # Insert into reviews table
    cursor.execute("INSERT INTO reviews VALUES ('1', '101', '1', 5)")
    cursor.execute("INSERT INTO reviews VALUES ('2', '102', '2', 4)")

    # Insert into users table
    cursor.execute("INSERT INTO users VALUES ('201', 'John Doe', 'john.doe@example.com', '1234567890', 'Billing Address 1')")
    cursor.execute("INSERT INTO users VALUES ('202', 'Jane Smith', 'jane.smith@example.com', '9876543210', 'Billing Address 2')")

    conn.commit()
    print("Data inserted successfully!")

def main():
    conn, cursor = connect_db()

    # Insert data into tables
    insert_data(conn, cursor)

    close_db(conn)

if __name__ == "__main__":
    main()
