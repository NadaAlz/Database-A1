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
