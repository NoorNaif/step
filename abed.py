import django
import mysql.connector
def signup():
  print("Enter firstname")
  fname=input()
  print("Enter lastname")
  lname = input()
  print("Enter username")
  uname = input()
  print("Enter password")
  passw = input()
  print("Enter email")
  email = input()
  print("Enter phone number")
  pnum = input()
  print("Enter ID")
  id = input()
  return [fname,lname,uname,passw,email,pnum,id]
mydb = mysql.connector.connect(
   host="localhost",
   user="abedj17",
   password="abedjamal123"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase ")
mycursor.execute("USE mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS info (firstname VARCHAR(255),lastname VARCHAR(255),username VARCHAR(255),password VARCHAR(255), email VARCHAR(255),phonenumber int(10),id int(10))")
info=signup()
mycursor.execute("INSERT INTO info VALUES ('{}','{}','{}','{}','{}',{},{})".format(info[0],info[1],info[2],info[3],info[4],info[5],info[6]))

mycursor.execute("SELECT * FROM info")
records=mycursor.fetchall()
for row in records:
        for i in row:
          print(i)