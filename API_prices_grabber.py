import requests
import time

def CoingeckoAPI_prices(coin):
    data_de_preco = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=%s&vs_currencies=usd" %(coin["id"]))
    if data_de_preco.status_code >= 200 and data_de_preco.status_code < 299 :
        data_de_preco = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=%s&vs_currencies=usd" %(coin["id"])).json()
        return (data_de_preco[coin["id"]]["usd"])
    elif data_de_preco.status_code == 429:
        time.sleep(1)
        CoingeckoAPI_prices(coin)
    # elif data_de_preco.status_code >= 400 and data_de_preco.status_code < 500:
    #    raise CoinNotFoundError
    # elif data_de_preco.status_code >= 500:
    #    raise ServerError
    #
    # Apagar else abaixo
    else:
        print (data_de_preco)
        return False
    

# class CoinNotFoundError(Exception):
#     pass

# class ServerError(Exception):
#     pass
