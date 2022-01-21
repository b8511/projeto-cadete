import requests
import time
from API_coins_grabber import CoingeckoAPI_list 
from API_prices_grabber import CoingeckoAPI_prices

dicionario_de_coins = CoingeckoAPI_list()
CoingeckoAPI_prices(dicionario_de_coins)


