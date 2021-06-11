#creating connection

import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
     print(connection)
except Error as e:
    print(e)

#creating TABLE

import mysql.connector as mysql
 
db = mysql.connect(host="localhost",user="root",password="1234567890",database=" DATA")
 
cursor = db.cursor()
 
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
sql = "CREATE TABLE EMPLOYEE_DETAILS ( F_NAME CHAR(20) NOT NULL, L_NAME CHAR(20), AGE INT, SALARY INT )"
 
cursor.execute(sql) 
db.close()

#
import sqlite3
  
conn = sqlite3.connect('pyDB.db')
c = conn.cursor()
  
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)')
  
def data_entry():
    number = 1
    name = "PYTHON"
    c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name))
    conn.commit()
  
create_table()
data_entry()
  
c.close()
conn.close()

# show databases
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567890"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

