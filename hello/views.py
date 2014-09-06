# Create your views here.
from django.shortcuts import render_to_response	
from django.template import RequestContext
from models import Authn
import datetime

def index(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		uname = request.POST['uname']
		email = request.POST['email']
		password = request.POST['password']

		authen = Authn(fname = fname)
		authen.lname = lname
		authen.uname = uname
		authen.email = email
		authen.password = password
	       	authen.lastlogin = datetime.datetime.now() 
       		authen.save()
		template = "main.html"	
	
	elif request.method == 'GET':
		template = "hello.html"

	return render_to_response(template,context_instance=RequestContext(request))

def signIn(request):
	if request.method == 'GET':
		uname = request.GET['uname']
		password = request.GET['password']
		
		user = Authn.objects(uname = uname).first()
		i = 0
		while user:
			if user.password == password:
				return render_to_response("main.html")	
			elif user.password != password:
				return render_to_response("hello.html")
			i = i + 1
			user = Authn.objects(uname = uname)[i]
		
	return render_to_response("hello.html")
