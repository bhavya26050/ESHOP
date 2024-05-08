import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def connect_db():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    return conn, cursor

    
def close_db(conn):
    conn.close()


def insert_data(table_name, values):
    try:
        conn, cursor = connect_db()
        cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?'] * len(values))})", values)
        conn.commit()
        messagebox.showinfo("Success", f"Data inserted successfully into {table_name} table!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        close_db(conn)


def update_data(table_name, primary_key, values):
    try:
        conn, cursor = connect_db()
        update_query = f"UPDATE {table_name} SET "
        update_query += ', '.join([f"{key}=? " for key in values.keys()])
        update_query += f"WHERE {primary_key}=?"
        values[primary_key] = primary_key_entry.get()
        cursor.execute(update_query, tuple(values.values()))
        conn.commit()
        messagebox.showinfo("Success", f"Data updated successfully in {table_name} table!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        close_db(conn)

# Function to handle deleting data from a table
def delete_data(table_name, primary_key):
    try:
        conn, cursor = connect_db()
        cursor.execute(f"DELETE FROM {table_name} WHERE {primary_key}=?", (primary_key_entry.get(),))
        conn.commit()
        messagebox.showinfo("Success", f"Data deleted successfully from {table_name} table!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        close_db(conn)


def select_data(table_name):
    try:
        conn, cursor = connect_db()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)  
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        close_db(conn)


def open_table_tab(table_name):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=table_name.capitalize())

 
    conn, cursor = connect_db()
    cursor.execute(f"PRAGMA table_info({table_name})")
    table_info = cursor.fetchall()
    close_db(conn)

   
    entries = {}
    for idx, column in enumerate(table_info):
        label = tk.Label(tab, text=column[1].replace('_', ' ').capitalize() + ':')
        label.grid(row=idx, column=0, padx=5, pady=5)

        entry = tk.Entry(tab)
        entry.grid(row=idx, column=1, padx=5, pady=5)
        entries[column[1]] = entry

    
    insert_button = tk.Button(tab, text="Insert Data", command=lambda: insert_data(table_name, [entry.get() for entry in entries.values()]))
    insert_button.grid(row=len(table_info), column=0, padx=5, pady=10)

    update_button = tk.Button(tab, text="Update Data", command=lambda: update_data(table_name, table_info[0][1], {key: entry.get() for key, entry in entries.items()}))
    update_button.grid(row=len(table_info), column=1, padx=5, pady=10)

    primary_key_label = tk.Label(tab, text=f"{table_info[0][1].replace('_', ' ').capitalize()} for Deletion:")
    primary_key_label.grid(row=len(table_info) + 1, column=0, padx=5, pady=5)

    global primary_key_entry
    primary_key_entry = tk.Entry(tab)
    primary_key_entry.grid(row=len(table_info) + 1, column=1, padx=5, pady=5)

    delete_button = tk.Button(tab, text="Delete Data", command=lambda: delete_data(table_name, table_info[0][1]))
    delete_button.grid(row=len(table_info) + 2, column=0, columnspan=2, padx=5, pady=10)

    select_button = tk.Button(tab, text="Select Data", command=lambda: select_data(table_name))
    select_button.grid(row=len(table_info) + 3, column=0, columnspan=2, padx=5, pady=10)

# Create the main window
root = tk.Tk()
root.title("SQLite Database GUI")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

tables = ['address', 'categories', 'orders', 'payment', 'product', 'reviews', 'users']

# Create buttons for each table on the first page
for table_name in tables:
    button = tk.Button(root, text=table_name.capitalize(), command=lambda tn=table_name: open_table_tab(tn))
    button.pack(padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
