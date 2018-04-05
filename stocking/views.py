
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings #Emerson added
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

def stockHistory(request, symbol='',high='',low=''):
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
		#risk_data = StockServices.get_risk_analysis(j_data[i]['symbol'],new_dict['high'],new_dict['low'])
		#new_dict['rickMeasure'] = risk_data[0]['rickMeasure']
		dict_of_dicts[j_data[i]['symbol']] = new_dict
	stock_history = dict_of_dicts     
	return render(request, 'stocks/home.html', {'stock_history':stock_history})

#include 'symbol' in url that is added to urls.py
def symbolHistory(request,symbol):
	j_data = StockServices.get_symbol_history(symbol)
	dict_of_dicts = {}
	#print(j_data)
	print("length: ",len(j_data))
	#correct what`s below for this method.
	for i in range(0,len(j_data)):
		print(i)
		new_dict = {}
		new_dict['volume'] = j_data[i]['volume']
		new_dict['date'] = j_data[i]['date']
		new_dict['open'] = j_data[i]['open']
		new_dict['close'] = j_data[i]['close']
		new_dict['high'] = j_data[i]['high']
		new_dict['low'] = j_data[i]['low']
		dict_of_dicts[j_data[i]['date']] = new_dict
	print("yopy")
	symbol_history = dict_of_dicts
	#print(symbol_history)
	return render(request, 'stocks/home3.html',{'symbol_history':symbol_history}) #<------------changed here

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

	return render(request, 'stocks/home.html',{'symbol_info': symbol_info})


def riskAnalysis(request,symbol,high,low):
	j_data = StockServices.get_risk_analysis(symbol,high,low)
	dict_of_dicts = {}
	for i in range(0,len(j_data)):
		new_dict = {}
		new_dict['rickMeasure'] = j_data[i]['rickMeasure']
		new_dict['riskFactorsDescription'] = j_data[i]['riskFactorsDescription']
		new_dict['symbolInfo'] = j_data[i]['symbolInfo']
		#ticker_symbol
		#company_name
		new_dict['symbolInfo'] = j_data[i]['symbolInfo'][0]['company_name']
		#gics_sector
		#gics_sub_industry
		#address
		#cik
		#riskMetric
		dict_of_dicts[j_data[i]['rickMeasure']] = new_dict
	risk_analysis = dict_of_dicts
	return render(request,'stocks/home.html',{'risk_analysis':risk_analysis})
