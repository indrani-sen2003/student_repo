from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(Request):
	return HttpResponse("<h1><font color='Green'> We are at Regenesys ,one of the most top business schools</font></h1>")
def student_home(Request):
	return HttpResponse("<h1>We are going to display students records</h1>")

