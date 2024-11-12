import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "community"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE building (name VARCHAR(50), floors INTEGER(200))")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)