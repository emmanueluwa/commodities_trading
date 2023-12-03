"""
live market prices:
 - real-time spot prices for various commodoties
 - charts with historical data to show price trends

supply and demand indicators:
 - current supply and demand conditions for each commodity
 - highlight relevant news/events affecting supply chains

historical performance
 - historical performance of commodtities to help users 
 understand past price movements
 - include interactive charts and graphs for easy analysis

comparative analysis
 - users will be allowed to compare different commodities easily
 - insights into correlations between different commodities will be 
 provided


FARMS AND FISHERY PRICES, TEXTILES AND FIBRES PRICES
"""
import requests
import os
from dotenv import load_dotenv

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

load_dotenv()

def index(request):
    url = "https://bloomberg-api.p.rapidapi.com/bloomberg/agriculture"
    
    headers = {
	"X-RapidAPI-Key": os.getenv("API_KEY"),
	"X-RapidAPI-Host": "bloomberg-api.p.rapidapi.com"
    }   

    try: 
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        
        else:
            return JsonResponse({'error': f"Error: {response.status_code}, {response.text}"}, status=500)

    except Exception as e:
        return JsonResponse({'error': f"An error occured: {str(e)}"}, status=500)



def live_market_prices():
    pass


def supply_demand():
    pass


def historic_performance():
    pass


def comparitive_analysis():
    pass
