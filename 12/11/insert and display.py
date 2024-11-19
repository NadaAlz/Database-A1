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


# Function to insert data into the database
def insert_state():
    State_ID = state_id_entry.get()
    StateName = state_name_entry.get()

    try:
        # SQL query to insert data
        sql = "INSERT INTO States (state_id, state_name) VALUES (%s, %s)"
        values = (State_ID, StateName)
        mycursor.execute(sql, values)
        mydb.commit()
        status_label.config(text="State added successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

    # Clear the input fields
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

# Add the Insert button
insert_button = Button(root, text="Insert State", command=insert_state)
insert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Add a status label for feedback
status_label = Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI application
root.mainloop()
