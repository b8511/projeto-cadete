import requests
import time

def CoingeckoAPI_list():
    coinfirm = requests.get("https://api.coingecko.com/api/v3/coins/list/")
    if coinfirm.status_code >= 200 and coinfirm.status_code < 299:
        lista_coins = requests.get("https://api.coingecko.com/api/v3/coins/list/")
        dic_coins = lista_coins.json()
        return dic_coins
    elif coinfirm.status_code == 429:
        time.sleep(1)
        CoingeckoAPI_list()
    else:
        print (coinfirm)
        return False