import _sqlite3
import sqlite3
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
 # Create your views here.
 # def login(request):
 #     return redirect(request,'STEP/register')
#return render(request,'STEP/login.html')
global user
global select
user=''
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except :
        print("error")

    return conn

def loginView(request):
	conn=create_connection("mydb.db")
	cur=conn.cursor()
	if request.method=='POST':
		a = request.POST['select1']
		username1 = request.POST['username']
		password1 = request.POST['password']
		if a == '2':
			cur.execute("SELECT username, password FROM TeacherDetails")
		if a == '3':
			cur.execute("SELECT username, password FROM StudentDetails")
		if a == '4':
			cur.execute("SELECT username, password FROM AdminDetails")

		data = cur.fetchall()
		found = False
		data2 = (dict(data))
		conn.close()
		if username1 in data2.keys() and password1 == str(int(data2[username1])):
			user = username1
			found = True

		if found:
			return render(request, "STEP/profile.html")
		else:
			messages.error(request, 'Wrong username or password', extra_tags='safe')
			return render(request, 'STEP/login.html')
	else:
		return render(request, 'STEP/login.html')

def registerView(request):
	conn = create_connection("mydb.db")
	cur = conn.cursor()
	if request.method == 'POST':
		#username1 = request.POST['username']
		password1 = request.POST['password']
		username1 = request.POST['username']
		firstname1 = request.POST['firstname']
		lastname1 = request.POST['lastname']
		email1 = request.POST['email']
		id1 = request.POST['id']
		subject1 = request.POST['subject']
		phonenumber1 = request.POST['phonenumber']
		a = request.POST['select1']
		if a == '2':
			cur.execute("SELECT username, password FROM TeacherDetails")
		if a == '3':
			cur.execute("SELECT username, password FROM StudentDetails")
		data = cur.fetchall()
		found = False
		data2 = (dict(data))
		#if username1 not in data2.keys():
		cur = conn.cursor()
		if a == '2':
			cur.execute("INSERT INTO TeacherDetails VALUES( " + "'" + password1 + "'" + " , " + "'" + username1 + "'" + " , " + "'" + firstname1 + "'" + " , " + "'" + lastname1 + "'" + " , " + "'" + email1 + "'" + " , " + id1 + " , " + "'" + subject1 + "'" + "," + phonenumber1 + " )")
		if a == '3':
			cur.execute("INSERT INTO StudentDetails VALUES( " + "'" + password1 + "'" + " , " + "'" + username1 + "'" + " , " + "'" + firstname1 + "'" + " , " + "'" + lastname1 + "'" + " , " + "'" + email1 + "'" + " , " + id1 + " , " + "'" + subject1 + "'" + "," + phonenumber1 + " )")
		#print(str)
		#cur.execute(str)
		conn.commit()
	conn.close()
	return render(request,'STEP/register.html')

def profileVeiw(request):
	if user!='':
	 	return render(request,'STEP/profile.html')