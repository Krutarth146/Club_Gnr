import mysql.connector


mydb = mysql.connector.connect(user = "root", password = "mysql", host = "localhost", database = "club")

if mydb.is_connected():
    print("Database Connected...")
else:
    print("Error ocuured")