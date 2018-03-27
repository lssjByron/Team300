#StockServices.py
#class that contains methods for retrieval of data from AlphaVenture API
import requests
import json

def get_stock_history(limit=40):
	url = "https://stockserviceapiv04.mybluemix.net/api/stockhis?"+"limit=" +str(limit)
	response = requests.get(url, auth=('admin', 'password123'))
	j_data = json.loads(response.text)
	return j_data

def get_symbol_history(symbol):
	url = "https://stockserviceapiv04.mybluemix.net/api/stockhis?symbol="+symbol
	response = requests.get(url, auth=('admin', 'password123'))
	j_data = json.loads(response.text)
	return j_data

def get_symbol_info(symbol):
	url = "https://stockserviceapiv04.mybluemix.net/api/symbolinfo?symbol="+symbol
	response = requests.get(url, auth=('admin','password123'))
	j_data  = josn.loads(response.text)
	return j_data

#def get_risk_analysis(symbol,high,low):	