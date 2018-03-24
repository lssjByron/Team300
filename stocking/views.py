
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from stocking.forms import SignUpForm
#from django.http import HttpResponse

# def home(request):
def home(request):
    return render(request, 'stocks/home.html')