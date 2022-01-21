import requests
import time

"""
[Criar uma classe]
Este tipo de lógica convem sempre estar contextualizada em Classes.
Regra geral:
Para qualquer função:
-Se tem um contexto de negócio bem definido -> Agrupa as funções desse contexto de negócio dentro duma classe.
-Se não tem um contexto de negócio bem definido -> Move a função para um modulo (é o nome que se dá a files com código python) mais genérico (normalmente helpers.py).

*Há outras razões para criar classes, nomeadamente:
-Contextualizar o estado dum objecto.
-Criar hierarquias/relações
-Etc...

[Naming convention]
Na convenção de nomenclatura do Python, os nomes das funções devem sempre seguir a convenção snake_case (coingecko_api).
Em contrapartida, classes devem sempre seguir a convenção CamelCase (CoingeckoAPI).

[Outas Notas]
1. Visto que tanto esta API call como a API call dos preços são feitas à API do coingecko, convem contextualizá-las às 2 dentro da mesma classe.
Dessa maneira tens uma classe unica, simples, que alguém que use o teu código pode chamar, para interagir com o Coingecko.
*A excepção há regra seria se precisases de implementar centenas de API calls diferentes da API do coingecko, dessa maneira o teu código 
escalava para milhares e milhares de linhas, e nesse caso mais concreto era preferivel dividir entre várias classes/files.

2. É boa practice dividires o teu código entre várias pastas.
Neste momento tens uma unica pasta com todo o código. Uma vez que vais continuar a criar mais código, mais tarde ou mais cedo ias ter problemas de organização.
O ideal é teres uma pasta dedicada a APIs externas, e lá dentro teres o file coingecko.py, que contem este mesmo código.

"""
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
