import requests
import time
from API_mediators.coingecko import CoingeckoAPI 
from API_mediators.exceptions import CoinNotFoundError
from API_mediators.exceptions import ServerError


"""
[Nomenclatura do código main]
Neste caso em concreto, este modulo é na verdade o modulo executável do teu projecto.
Neste momento isso não está evidente.

É good practice dares o nome de __main__.py a este tipo de modulos, para ser mais facil a outros developers
saberem que este é o modulo que é suposto ser executado.

Deves seguir o standard:
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
    
Tens aqui uma explicação:
https://realpython.com/python-main-function/ 


[Outras Notas]
Neste csao há varias razões que podem levar a que CoingeckoAPI_prices(coin) == False.
-Falhas de rede
-Erro de servidor
-Inexistencia de preço para o coin
-Etc...
E em cada um desses casos tu vais parar completamente a execução do loop.

O mais correto aqui seria do lado do coingecko seres um pouco mais verboso com os erros.
-Caso encontres um erro 404 (not found): Retornas um CoinNotFoundError.
-Caso encontres um erro 5xx (server error): Retornas um ServerError.
E nesta função, dás handle desses erros, de maneira mais explicita:
-Caso recebas um CoinNotFoundError -> Passas à frente.
-Caso recebas um ServerError -> Dás retry mais N vezes.

"""
def main():
    coins_dictionary = CoingeckoAPI.coingecko_api_list()

    for coin in coins_dictionary:
        retries = 0
        should_ignore = False
        while retries < 3 and not should_ignore:
            time.sleep(1)                                               # 1 second on hold for each try 
            try:
                coin_value = CoingeckoAPI.coingecko_api_prices(coin)    # get coin's value
            except CoinNotFoundError:                                   # jumps to the next coin
                should_ignore = True                                
            except ServerError:                                         # on server error retries three times
                retries = retries + 1
            else:
                print ("{} : {} $" .format(coin["name"],str(coin_value)))       # print it in the terminal
                break
        if retries >=3 :                                                # in case of not responding on the third time Stop fetching
            print ("Server Error")
            break        

if __name__ == "__main__":
    main()
    
