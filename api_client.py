import requests
from time import sleep

def obter_lista_do_cardapio():
    resposta = requests.get("http://127.0.0.1:8000/produtos")

    if resposta.status_code == 200:
        produtos = resposta.json()
        
        print(f'{"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
        sleep(0.03)
        
        for item in produtos:
            print(f'{item["id"]:<5} {item["nome"]:<26} {item["categoria"]:<15} {item["preco"]:<10}')
            sleep(0.03)
            
        print('-' * 58)
        
    else:
        print("Ocorreu um erro ao buscar os produtos!")
