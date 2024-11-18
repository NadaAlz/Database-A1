from tkinter import *


import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "bank community"
)

mycursor = mydb.cursor()

#Creating database

#mycursor.execute("CREATE DATABASE Community")

#creating tables

#mycursor.execute("CREATE TABLE building (name VARCHAR(50), floors INTEGER(200))")

#mycursor.execute("SHOW TABLES")


#for tb in mycursor:
 #   print(tb)

 #Inserting values

#sqlFormula = "INSERT INTO building (name, floors) VALUES (%s, %s)"
#building1 = ("Qamar1",45)

#mycursor.execute(sqlFormula, building1)

#mydb.commit()

#Selecting data

#mycursor.execute("SELECT name FROM building")

#yresult = mycursor.fetchall()

#for row in myresult:
 #  print(row)


# Updating a record
#update_query = "UPDATE building SET floors = %s WHERE name = %s"
#data_to_update = (50, "Qamar1")  # Update floors to 50 for building 'Qamar1'

#mycursor.execute(update_query, data_to_update)
#mydb.commit()

# Deleting a record
#delete_query = "DELETE FROM building WHERE name = %s"
#data_to_delete = ("Qamar1",)

#mycursor.execute(delete_query, data_to_delete)
#mydb.commit()

#sqlFormula = "INSERT INTO States (State_ID, StateName) VALUES (%s, %s)"

#aestates = [("DU", "Dubai"), ("AD", "AbuDhabi")]

#mycursor.executemany(sqlFormula, aestates)

#mydb.commit()

def insert_state():
    State_ID = state_id_entry.get()
    StateName = state_name_entry.get()

    try:
        # SQL query to insert data
        sql = "INSERT INTO States (state_id, state_name) VALUES (%s, %s)"
        values = (State_ID, StateName)  # Corrected to use variables from the input fields
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
Label(root, text="State_ID:").grid(row=0, column=0, padx=10, pady=10)
state_id_entry = Entry(root)
state_id_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="StateName:").grid(row=1, column=0, padx=10, pady=10)
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