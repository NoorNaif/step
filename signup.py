import django
import mysql.connector
def signup():
  fname=input("Enter first name")
  lname = input("Enter last name")
  uname = input("Enter username")
  passw = input("Enter a password")
  email = input("Enter email")
  pnum = input("Enter phone number")
  id = input("enter id")
  tea= input("are you a teacher")
  sub=input("the subject you will learn is:")
  return [fname,lname,uname,passw,email,pnum,id,tea,sub]
mydb = mysql.connector.connect(
   host="localhost",
   user="noornaif",
   password="noor123"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase ")
mycursor.execute("USE mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS info (firstname VARCHAR(255),lastname VARCHAR(255),username VARCHAR(255),password VARCHAR(255), email VARCHAR(255),phonenumber int(10),id int(10))")
info=signup()
mycursor.execute("INSERT INTO info VALUES ('{}','{}','{}','{}','{}',{},{},{},{})".format(info[0],info[1],info[2],info[3],info[4],info[5],info[6]))

mycursor.execute("SELECT * FROM info")
records=mycursor.fetchall()
for row in records:
        for i in row:
          print(i)
