
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings #Emerson added
from stocking.forms import SignUpForm #Emerson
from stocking.forms import SubmitStocks #Emerson
from stocking.serializer import StockSerializer #Emerson
import requests #Emerson added
import json #Emerson added
import StockServices #Emerson added
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
	# url = "https://stockserviceapiv04.mybluemix.net/api/stockhis?limit=40"
	# response = requests.get(url, auth=('admin', 'password123'))
	j_data = StockServices.get_stock_history() #make call to a StockServices method to retrieve history
	dict_of_dicts = {}
	for i in range(0,len(j_data)):
		new_dict = {}
		new_dict['volume'] = j_data[i]['volume']
		new_dict['date'] = j_data[i]['date']
		new_dict['open'] = j_data[i]['open']
		new_dict['close'] = j_data[i]['close']
		new_dict['high'] = j_data[i]['high']
		new_dict['low'] = j_data[i]['low']
		dict_of_dicts[j_data[i]['symbol']] = new_dict

	#right now the serialization process is being skipped.
	serializer = StockSerializer(data=dict_of_dicts)
	if serializer.is_valid():
		print("koko")
		stock = serializer.save()
		return render(request, 'stocks/home2.html', {
			'symbol': dict_of_dicts['symbol'],
			'date': j_data[0]['date'],
			'open': j_data[0]['open'],
			'close': j_data[0]['close'],
			'high': j_data[0]['high'],
			'low': j_data[0]['low'],
			'volume': j_data[0]['volume']
			})
	else:
		print (serializer.errors)
		stock_history = dict_of_dicts
		return render(request, 'stocks/home2.html', {'stock_history':stock_history})

#include 'symbol' in url that is added to urls.py
def symbolHistory(request, symbol):
	
	j_data = StockServices.get_symbol_history(symbol)
	dict_of_dicts = {}

	#correct what`s below for this method.
	for i in range(0,len(j_data)):
		new_dict = {}
		new_dict['volume'] = j_data[i]['volume']
		new_dict['date'] = j_data[i]['date']
		new_dict['open'] = j_data[i]['open']
		new_dict['close'] = j_data[i]['close']
		new_dict['high'] = j_data[i]['high']
		new_dict['low'] = j_data[i]['low']
		dict_of_dicts[j_data[i]['symbol']] = new_dict

	symbol_history = dict_of_dicts

	return render(request, 'stocks/home2.html',{'symbol_history':symbol_history})

#include 'symbol' in url that is added to urls.py
def symbolInfo(request,symbol):
	j_data = StockServices.get_symbol_info(symbol)
	dict_of_dicts = {}

	#correct what`s below for this method.
	for i in range(0,len(j_data)):
		new_dict = {}
		new_dict['volume'] = j_data[i]['volume']
		new_dict['date'] = j_data[i]['date']
		new_dict['open'] = j_data[i]['open']
		new_dict['close'] = j_data[i]['close']
		new_dict['high'] = j_data[i]['high']
		new_dict['low'] = j_data[i]['low']
		dict_of_dicts[j_data[i]['symbol']] = new_dict	

	symbol_info = dict_of_dicts

	return render(request, 'stocks/home2.html',{'symbol_info': symbol_info})


#def riskAnalysis():


