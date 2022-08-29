#Employee management System Using Python and SQL

#Import sql connector 

import mysql.connector

#making database
connection = mysql.connector.connect(host="localhost", user="root", password="")
myCursor = connection.cursor()

myCursor.execute("CREATE DATABASE Employee")