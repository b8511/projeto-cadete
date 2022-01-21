import requests

def CoingeckoAPI_list():
    lista_coins = requests.get("https://api.coingecko.com/api/v3/coins/list/")
    dic_coins = lista_coins.json()
    return dic_coins