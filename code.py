import requests
import time
from API_coins_grabber import CoingeckoAPI_list 
from API_prices_grabber import CoingeckoAPI_prices

dicionario_de_coins = CoingeckoAPI_list()
if dicionario_de_coins:
    for coin in dicionario_de_coins:
        time.sleep(0.3)
        valor_de_moeda = CoingeckoAPI_prices(coin)
        if valor_de_moeda == False:
            break
        else:
            print(coin["name"] + " : %s $" %(str(valor_de_moeda)))

