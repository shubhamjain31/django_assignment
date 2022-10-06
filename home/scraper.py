import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import math


def scrape_website():

    query_string = [
        ('start', '1'),
        ('limit', '100'),
        ('sortBy', 'market_cap'),
        ('sortType', 'desc'),
        ('convert', 'USD'),
        ('cryptoType', 'all'),
        ('tagType', 'all'),
    ]

    base = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?"
    response = requests.get(f"{base}{urlencode(query_string)}").json()
    last_page = (int(response["data"]["totalCount"]) // 100) + 1
    all_pages = [1 if i == 1 else (i * 100) + 1 for i in range(1, last_page)]

    for page in all_pages[:1]:
        query_string = [
            ('start', str(page)),
            ('limit', '100'),
            ('sortBy', 'market_cap'),
            ('sortType', 'desc'),
            ('convert', 'USD'),
            ('cryptoType', 'all'),
            ('tagType', 'all'),
        ]
        response = requests.get(f"{base}{urlencode(query_string)}").json()

        results = [
            {
                'name':currency["name"],
                'price':round(currency["quotes"][0]["price"], 4),
                'market_cap':currency["quotes"][0]["marketCap"],
                'volume24h':currency["quotes"][0]["volume24h"],
                'circulating_supply':currency["circulatingSupply"],
                'one_hour_per':str(math.floor(currency["quotes"][0]["percentChange1h"] * 100)/100.0) +' %',
                'one_day_per':str(math.floor(currency["quotes"][0]["percentChange24h"] * 100)/100.0) +' %',
                'seven_day_per':str(math.floor(currency["quotes"][0]["percentChange7d"] * 100)/100.0) +' %',
            }
            for currency in response["data"]["cryptoCurrencyList"]
        ]
    return results