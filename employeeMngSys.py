#Employee management System Using Python and SQL

#Import sql connector 
from os import system
import mysql.connector
import re

#making database
connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="employee")
myCursor = connection.cursor()
#myCursor.execute("CREATE DATABASE Employee")
#myCursor.execute("CREATE TABLE empdata (Id INT(11) PRIMARY KEY, Name VARCHAR(1000), Email_Id TEXT(1000),Phone_no INT(11), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(20))")\

#Regular expression to validate email
regex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#regular expression to validate a phone
Pattern = re.compile("(0|54?[7-9][0-9]{9}")
#Function to add employee

def Add_Employ():
    print("{:>60}".format("-->> Add Employee Record<<--"))
    Id = input("Enter Employee ID: ")
    if(check_employee_id(Id)== True):
        print("Employee ID Already Exists. Try again")
        press = input("Press any key to continue...")
        menu()
    #--------------------------------------------------------#
    Name = input("Enter Employee Name: ")
    if(check_employee_name(Name)== True):
        print("Employee Already Exists. Try again")
        press = input("Press any key to continue...")
        menu()
     #--------------------------------------------------------#
    Email_Id = input("Enter Employee Email: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employ()
     #--------------------------------------------------------#
    Phone_no = input("Enter Employee Phone No: ")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
     #--------------------------------------------------------#
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

#Check to see if the employee exists
def check_employee_name(employee_name):
    sql = 'SELECT * FROM empdata WHERE Name=%s'
    c = connection.cursor(buffered= True)
    data = (employee_name, )
    c.execute(sql, data)
    r = c.rowcount
    match r:
        case 1:
            return True
        case _:
            return False
    
def check_employee_id(Id):
    sql = 'SELECT * FROM empdata WHERE Id=%s'
    c = connection.cursor(buffered= True)
    data = (Id, )
    c.execute(sql, data)
    r = c.rowcount
    match r:
        case 1:
            return True
        case _:
            return False
    
def Display_Employee():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    # query to select all rows from Employee (empdata) Table
    sql = 'select * from empdata'
    c = connection.cursor()
    c.execute(sql)
    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()
#//////////////////////////////////////////////////////////////////////////////////////    
def Update_Employee():
    print("{:>60}".format("-->> Update Employee Record <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee_id(Id)== False):
        print("Employee ID Already exists. Try again...")
        press = input("Press any key to continue...")
        menu()
    else:
        Email_Id = input("Enter Employee email ID: ")
        Phone_no = input("Enter Employee Phone No: ")
        Address = input("Enter Employee Address: ")
        #Updating the employee's data 
        sql = 'UPDATE empdata SET Email_Id = %s, Phone_No = %s, Address = %s WHERE Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = connection.cursor()
        c.execute(sql, data)

        #Commit method
        connection.commit()
        print("Employee Updated Successfully")
        press = input("Press any key to continue...")
        menu()
#////////////////////////////////////////////////////////////////////////////////////////
def Promote_Employee():
    print("{:>60}".format("-->> Promote Employee Record <<--"))
    Id = input("Enter Employee Id: ")
    if (check_employee_id(Id)== False):
        print("Employee ID Already exists. Try again...")
        press = input("Press any key to continue...")
        menu()
    else:
        Amount = int(input("Enter increased salary amount: "))
        sql = 'SELECT Salary FROM empdata WHERE Id = %s'
        data = (Id,)
        c = connection.cursor()
        c.execute(sql, data)
        rail = c.fetchone()
        types = rail[0]+Amount
        sql = 'UPDATE empdata SET Salary = %s WHERE Id = %s'
        draw = (types,Id)
        sql = c.execute(sql,draw)
        connection.commit()
        print('Employee Salary Increased: Promoted')
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
        case 2:
            system("cls")
            Display_Employee()
        case 3:
            system("cls")
            Update_Employee()
        case 4:
            system("cls")
            Promote_Employee()
        case 7:
            system("cls")
            print("{:>60}".format("Have a nice day!"))
            exit(0)
        case _:
            print("invalid choice")
            press = input("Press any key to continue...")
            menu()
            

    

#Call menu function
menu()