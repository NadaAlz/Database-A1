import mysql.connector
from tkinter import Tk, Label, Entry, Button, END

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bank community"
)

mycursor = mydb.cursor()

import mysql.connector
from tkinter import Tk, Label, Entry, Button, END

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bank community"
)

mycursor = mydb.cursor()

import mysql.connector
from tkinter import Tk, Label, Entry, Button, Text, END

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bank community"
)

mycursor = mydb.cursor()


# Function to insert data into the States table
def insert_state():
    State_ID = state_id_entry.get()
    StateName = state_name_entry.get()

    try:
        sql = "INSERT INTO States (State_ID, StateName) VALUES (%s, %s)"
        values = (State_ID, StateName)
        mycursor.execute(sql, values)
        mydb.commit()
        status_label.config(text="State added successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

    state_id_entry.delete(0, END)
    state_name_entry.delete(0, END)


# Function to display all records in the States table
def display_states():
    try:
        sql = "SELECT * FROM States"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        display_box.delete("1.0", END)  # Clear the text box
        for row in results:
            display_box.insert(END, f"State_ID: {row[0]}, StateName: {row[1]}\n")
    except Exception as e:
        display_box.insert(END, f"Error: {e}\n")


# Function to update data in the States table
def update_state():
    State_ID = state_id_entry.get()
    StateName = state_name_entry.get()

    try:
        sql = "UPDATE States SET StateName = %s WHERE State_ID = %s"
        values = (StateName, State_ID)
        mycursor.execute(sql, values)
        mydb.commit()
        status_label.config(text="State updated successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

    state_id_entry.delete(0, END)
    state_name_entry.delete(0, END)




# Create the GUI window
root = Tk()
root.title("State Information")

# Add labels and entry fields
Label(root, text="State ID:").grid(row=0, column=0, padx=10, pady=10)
state_id_entry = Entry(root)
state_id_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="State Name:").grid(row=1, column=0, padx=10, pady=10)
state_name_entry = Entry(root)
state_name_entry.grid(row=1, column=1, padx=10, pady=10)

# Add buttons for operations
insert_button = Button(root, text="Insert State", command=insert_state)
insert_button.grid(row=2, column=0, pady=10)

update_button = Button(root, text="Update State", command=update_state)
update_button.grid(row=2, column=1, pady=10)

display_button = Button(root, text="Display States", command=display_states)
display_button.grid(row=3, column=0, pady=10)


# Add a text box to display records
display_box = Text(root, width=50, height=15)
display_box.grid(row=4, column=0, columnspan=2, pady=10)

# Add a status label for feedback
status_label = Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI application
root.mainloop()

