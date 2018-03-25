
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings #Emerson added
from stocking.forms import SignUpForm #Emerson
from stocking.forms import SubmitStocks #Emerson
from stocking.serializer import StockSerializer #Emerson
import requests #Emerson added
#from django.http import HttpResponse

# def home(request):
def home(request):
    return render(request, 'stocks/home.html')

# 	return render(request,'stocks/home.html')
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {"form":form})

def stockHistory(request):
	print("here")
	url = "https://stockserviceapiv04.mybluemix.net/api/stockhis?limit=40"
	response = requests.get(url, auth=('admin', 'password123'))
	json = response.json()
	test = json[0]
	serializer = StockSerializer(data=test)
	if serializer.is_valid():
		print("koko")
		embed = serializer.save()
		return render(request, 'stocks/home2.html', {
			'symbol': json['symbol'],
			'date': json['date'],
			'open': json['open'],
			'close': json['close'],
			'high': json['high'],
			'low': json['low'],
			'volume': json['volume']
			})
	else:
		print (serializer.errors)
		#print(json[0])
		history_result = json
		#if 'symbol' in history_result:
		#	print("yea")
		#	history_result[0] = history_result.volume
		return render(request, 'stocks/home2.html', {
			'history_result': history_result
			
			# 'open': json['open'],
			# 'close': json['close'],
			# 'high': json['high'],
			# 'low': json['low'],
			# 'volume': json['volume']
			})




