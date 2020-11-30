import django
import mysql.connector
from mysql.connector import cursor


def OldUser():
  cursor.execute("SELECT * FROM Users")
  Users = cursor.fetchall()
  oldusername = input("Username: ")
  oldpassword = input("Password: ")

  if oldusername and oldpassword == Users:
    print("Login was successfully!")
  elif oldusername and oldpassword != Users:
    print("Something was wrong, log in you again")

