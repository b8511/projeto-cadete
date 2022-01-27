import requests
import time
from API_mediators.exceptions import CoinNotFoundError
from API_mediators.exceptions import ServerError
from API_mediators.exceptions import NoValueError


class CoingeckoAPI ():
    def __init__ (self):
        pass
    def coingecko_api_prices(coin_id):
        price_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd" .format(coin_id = coin_id))
        if price_data.status_code >= 200 and price_data.status_code < 299 :
            price_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd" .format(coin_id = coin_id)).json()
            if not "usd" in price_data[coin_id]:
                raise NoValueError 
            else:
                return (price_data[coin_id]["usd"])   #print
        elif price_data.status_code == 429:              
            raise ServerError
        elif price_data.status_code >= 400 and price_data.status_code < 500:
            raise CoinNotFoundError             
        elif price_data.status_code >= 500:
            raise ServerError

             

    def coingecko_api_list():
        coinfirm = requests.get("https://api.coingecko.com/api/v3/coins/list/")
        if coinfirm.status_code >= 200 and coinfirm.status_code < 299:
            coins_list = requests.get("https://api.coingecko.com/api/v3/coins/list/")
            dic_coins = coins_list.json()
            return dic_coins
        elif coinfirm.status_code == 429:
            time.sleep(1)
            CoingeckoAPI.coingecko_api_list()
        else:
            print (coinfirm)
            return False
