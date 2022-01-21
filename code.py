import requests
import time
from API_coins_grabber import CoingeckoAPI_list 
from API_prices_grabber import CoingeckoAPI_prices


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

dicionario_de_coins = CoingeckoAPI_list()
if dicionario_de_coins:
    for coin in dicionario_de_coins:
        # retries = 0
        # should_ignore = False
        # while retries < 3 and not should_ignore:
        #     try:
        time.sleep(0.3)
        valor_de_moeda = CoingeckoAPI_prices(coin)
        # Comentar este if
        if valor_de_moeda == False:
            break
        else:
            print(coin["name"] + " : %s $" %(str(valor_de_moeda)))
        #     except CoinNotFoundError:
        #         should_ignore = True
        # except ServerError:
        #     retries = retries + 1

