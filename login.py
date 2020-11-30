import django
import mysql.connector
from mysql.connector import cursor

def UserController():
    def __init__(self):
        mydb = mysql.connector.connect(host="localhost",
                                       user="adeem",
                                       password="1234")
        cursor = mydb.cursor()
        cursor.execute("USE mydatabase")
        self.user = None
        self.users = {}

    def Login(self, email, password):
        if email not in self.users:
            print("There is no user such as that")
        else:
            if self.user is None:
                if self.users[email].Login(password):
                    self.user = self.users[email]
                    print("The user is active")
                else:
                    print("The username or the password is wrong")
            else:
                print('There is active user')

def Service():
    def Login(self, email, password):
        self.us.Login(email, password)
def ProgramRun():
    s = Service()
    print('1.Login')
    print('')
    choice = int(input('Enter a number: '))
    while choice != 2:
        if choice == 1:
            email1 = input('Enter email: ')
            password1 = input('Enter password: ')
            s.Login(email1, password1)


