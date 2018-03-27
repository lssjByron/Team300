from rest_framework import serializers
from .models import Stocks

class StockSerializer(serializers.ModelSerializer):

	date = serializers.DateField(format=None, input_formats=None)
	class Meta:
		model = Stocks
		fields = ('date','symbol','open','close','low','high','volume')