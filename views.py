import _sqlite3
import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
# def login(request):
#     return redirect(request,'STEP/register')

def login(request):
    return render(request,'STEP/login.html')

def registerView(request):
    return render(request,'STEP/register.html')

def profileVeiw(request):
    return render(request,'STEP/profile.html')
