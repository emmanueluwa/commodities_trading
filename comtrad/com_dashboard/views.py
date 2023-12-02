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

"""

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("NGU")


def live_market_prices():
    pass


def supply_demand():
    pass


def historic_performance():
    pass


def comparitive_analysis():
    pass
