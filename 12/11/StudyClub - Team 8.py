import mysql.connector  # we import the MySQL connector library to connect and interact with the MySQL database
import tkinter as tk  # Tkinter for GUI development
from tkinter import ttk, messagebox

# These codes are used to establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", # We specify the hostname of the database server, which is here is the local machine
    user="root", # We specify the username to log into the database, which is the default 'root'
    passwd="", # We provided the password for our database user, we did not use a password so we left it empty
    database="studyclub" # We specified the name of the database to connect to, which is our "studyclub" database
)
# This is the cursor object for executing SQL queries and showing results
mycursor = mydb.cursor()


# Function to view a record by ID
def view_record_by_id(table_name, id_column):
    def fetch_record():
        record_id = entry_id.get()
        if not record_id:
            messagebox.showwarning("Input Error", "Please enter an ID!")
            return

        sql = f"SELECT * FROM {table_name} WHERE {id_column} = %s"
        try:
            mycursor.execute(sql, (record_id,))
            record = mycursor.fetchone()
            if not record:
                messagebox.showinfo("No Record", f"No record found for ID: {record_id}")
            else:
                # Display the record in a Treeview
                tree = ttk.Treeview(view_window, columns=(1, 2, 3, 4, 5), show="headings")
                tree.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
                column_names = [desc[0] for desc in mycursor.description]
                tree["columns"] = column_names

                for col in column_names:
                    tree.heading(col, text=col)
                    tree.column(col, width=100)

                tree.insert("", tk.END, values=record)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    view_window = tk.Toplevel(root)
    view_window.title(f"View {table_name}")

    tk.Label(view_window, text="Enter ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(view_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(view_window, text="Fetch Record", command=fetch_record).grid(row=1, column=0, columnspan=2, pady=10)

# Function to update a record by ID
def update_record_by_id(table_name, id_column):
    def fetch_and_update():
        record_id = entry_id.get()
        if not record_id:
            messagebox.showwarning("Input Error", "Please enter an ID!")
            return

        sql = f"SELECT * FROM {table_name} WHERE {id_column} = %s"
        try:
            mycursor.execute(sql, (record_id,))
            record = mycursor.fetchone()
            if not record:
                messagebox.showinfo("No Record", f"No record found for ID: {record_id}")
            else:
                column_names = [desc[0] for desc in mycursor.description]

                # Open a new window for updating the record
                update_window = tk.Toplevel()
                update_window.title(f"Update {table_name}")

                update_entries = []
                for i, col_name in enumerate(column_names[1:], start=1):  # Skip primary key column
                    tk.Label(update_window, text=f"{col_name}:").grid(row=i, column=0, padx=10, pady=5)
                    entry = tk.Entry(update_window)
                    entry.grid(row=i, column=1, padx=10, pady=5)
                    entry.insert(0, record[i])  # Pre-fill the current value
                    update_entries.append((col_name, entry))

                def save_updates():
                    updates = {col_name: entry.get() for col_name, entry in update_entries}
                    update_sql = f"UPDATE {table_name} SET " + ", ".join(
                        f"{col} = %s" for col in updates.keys()
                    ) + f" WHERE {id_column} = %s"
                    update_values = list(updates.values()) + [record_id]

                    try:
                        mycursor.execute(update_sql, update_values)
                        mydb.commit()
                        messagebox.showinfo("Success", "Record updated successfully!")
                        update_window.destroy()
                        update_id_window.destroy()
                    except Exception as e:
                        messagebox.showerror("Error", str(e))

                tk.Button(update_window, text="Save", command=save_updates).grid(row=len(update_entries) + 1, column=0, columnspan=2, pady=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    update_id_window = tk.Toplevel(root)
    update_id_window.title(f"Update {table_name}")

    tk.Label(update_id_window, text="Enter ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(update_id_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(update_id_window, text="Fetch Record", command=fetch_and_update).grid(row=1, column=0, columnspan=2, pady=10)

# Function to insert a record
def insert_record(table_name, auto_increment_field=None):
    def save_record():
        # Exclude the auto-increment field from entries if specified
        values = {entry_name: entry.get() for entry_name, entry in entries.items() if entry_name != auto_increment_field}
        sql = f"INSERT INTO {table_name} (" + ", ".join(values.keys()) + ") VALUES (" + ", ".join(["%s"] * len(values)) + ")"
        try:
            mycursor.execute(sql, tuple(values.values()))
            mydb.commit()
            messagebox.showinfo("Success", f"Data inserted into {table_name} successfully!")
            insert_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create a new window for data entry
    insert_window = tk.Toplevel(root)
    insert_window.title(f"Insert {table_name}")

    # Get column names for the table
    try:
        mycursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [row[0] for row in mycursor.fetchall()]
        entries = {}
        for i, column_name in enumerate(columns, start=1):
            # Skip the auto-increment field
            if column_name == auto_increment_field:
                continue
            tk.Label(insert_window, text=f"{column_name}:").grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(insert_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[column_name] = entry

        # Add a button to save the record
        tk.Button(insert_window, text="Save", command=save_record).grid(row=len(columns), column=0, columnspan=2, pady=10)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Submenus for Insert, View, and Update
def insert_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Insert Menu")

    tk.Button(menu_window, text="Insert Tutor", width=20, command=lambda: insert_record("tutor", "TutorID")).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(menu_window, text="Insert Student", width=20, command=lambda: insert_record("student")).grid(row=1, column=0, padx=20, pady=10)
    tk.Button(menu_window, text="Insert Appointment", width=20, command=lambda: insert_record("appointment", "AppointmentID")).grid(row=2, column=0, padx=20, pady=10)

def view_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("View Menu")

    tk.Button(menu_window, text="View Tutor by ID", width=20, command=lambda: view_record_by_id("tutor", "TutorID")).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(menu_window, text="View Student by ID", width=20, command=lambda: view_record_by_id("student", "StudentID")).grid(row=1, column=0, padx=20, pady=10)
    tk.Button(menu_window, text="View Appointment by ID", width=20, command=lambda: view_record_by_id("appointment", "AppointmentID")).grid(row=2, column=0, padx=20, pady=10)

def update_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Update Menu")

    tk.Button(menu_window, text="Update Tutor by ID", width=20, command=lambda: update_record_by_id("tutor", "TutorID")).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(menu_window, text="Update Student by ID", width=20, command=lambda: update_record_by_id("student", "StudentID")).grid(row=1, column=0, padx=20, pady=10)
    tk.Button(menu_window, text="Update Appointment by ID", width=20, command=lambda: update_record_by_id("appointment", "AppointmentID")).grid(row=2, column=0, padx=20, pady=10)

# Main GUI Window
root = tk.Tk()
root.title("Study Club System")

tk.Button(root, text="Insert Data", width=20, command=insert_menu).grid(row=0, column=0, padx=20, pady=10)
tk.Button(root, text="View Data", width=20, command=view_menu).grid(row=1, column=0, padx=20, pady=10)
tk.Button(root, text="Update Data", width=20, command=update_menu).grid(row=2, column=0, padx=20, pady=10)

root.mainloop()
