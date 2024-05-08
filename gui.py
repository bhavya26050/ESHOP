import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  phone TEXT NOT NULL)''')
    conn.commit()
    return conn, cursor

# Function to close the database connection
def close_db(conn):
    conn.close()

# Function to add a new record to the database
def add_record():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
    if name and email and phone:
        try:
            conn, cursor = connect_db()
            cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()
            messagebox.showinfo("Success", "Record added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            close_db(conn)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Database Editor")

# Create labels and entry fields for input
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Create a button to add a new record
add_button = tk.Button(root, text="Add Record", command=add_record)
add_button.pack()

# Start the GUI main loop
root.mainloop()
