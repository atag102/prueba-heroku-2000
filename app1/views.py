from django.shortcuts import render,redirect
from django.http import HttpResponse 
from pymongo import *

def home(request):
	client=MongoClient ('mongodb://atag10:C8720413@ds221990.mlab.com:21990/amv')
	db=client.amv
	colección  =  db.pruebaConeccion
	D3={"nombre": "Zakie","Edad":45,"Apellido":"Nohra","Nacionalidad": "Livaneza"}
	colección.insert_one(D3).inserted_id
	return render(request,'app1/home.html')
