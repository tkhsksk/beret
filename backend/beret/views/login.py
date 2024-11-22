from django.shortcuts import render, redirect # redirectを追記
from beret.forms import UserForm # UserFormをimport
from beret.models import User

def index(request):
	return render(request, "login/index.html")