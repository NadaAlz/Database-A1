import mysql.connector
from tkinter import Tk, Label, Entry, Button, END


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

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


#mycursor.execute("CREATE TABLE building (name VARCHAR(50), floors INTEGER(200))")


#mycursor.execute("SHOW TABLES")




#for tb in mycursor:
  # print(tb)

 #Inserting values

#sqlFormula = "INSERT INTO building (name, floors) VALUES (%s, %s)"
#building1 = ("Qamar1",45)

#sqlFormula1 = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#customer1 = ("Nada", "Muhasinah 1")


#mycursor.execute(sqlFormula, building1)

#mycursor.execute(sqlFormula1, customer1)
#mydb.commit()

#Selecting data

#mycursor.execute("SELECT * FROM customers")


#myresult = mycursor.fetchall()

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




