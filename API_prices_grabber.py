import requests
import time

def CoingeckoAPI_prices(dicionario):
    for key in dicionario:
        data_de_preco = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=%s&vs_currencies=usd" %(key["id"])).json()
        if isinstance(data_de_preco[key["id"]]["usd"],float):
            print (key["name"] + " : " + str(data_de_preco[key["id"]]["usd"]) + "$ \n")
        else:
            print (data_de_preco)
        time.sleep(0)