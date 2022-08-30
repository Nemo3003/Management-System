#Employee management System Using Python and SQL

#Import sql connector 
from os import system
import mysql.connector

#making database
connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="employee")
myCursor = connection.cursor()
#myCursor.execute("CREATE DATABASE Employee")
#myCursor.execute("CREATE TABLE empdata (Id INT(11) PRIMARY KEY, Name VARCHAR(1000), Email_Id TEXT(1000),Phone_no INT(11), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(20))")\

#Function to add employee

def Add_Employ():
    print("{:>60}".format("-->> Add Employee Record<<--"))
    Id = input("Enter Employee ID: ")
    Name = input("Enter Employee Name: ")
    Email_Id = input("Enter Employee Email: ")
    Phone_no = input("Enter Employee Phone No: ")
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post,Salary)
    
    #Deliver their data to the database
    sql = 'INSERT INTO empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = connection.cursor()

    #executing the sql query
    c.execute(sql, data)
    #fetching the data
    data = c.fetchall()
    #Commiting  to make changes
    connection.commit()
    print("New Employee added successfully!")
    press = input("Press any key to continue...")
    menu()
#Menu Function to display 
def menu():
    system("cls")
    print("{:>60}".format("*****************************************"))
    print("{:>60}".format("-->> EMPLOYEE MANAGEMENT SYSTEM <<--"))
    print("{:>60}".format("*****************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit")
    print("{:>60}".format("-->> Choice Options : [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            system("cls")
            Add_Employ()
        case _:
            print("invalid choice")
            press = input("Press any key to continue...")
            menu()
            

    

#Call menu function
menu()