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

def cadastrar_produto(nome, categoria, preco):
    url_base = "http://127.0.0.1:8000"
    
    resposta = requests.post(
        url_base + "/produtos",
        
        json={
            "nome": nome,
            "categoria": categoria,
            "preco": preco
        }
    )
    
    if resposta.status_code in (200,201):
        return (f'HTTP {resposta.status_code}')
    
    else:
        return (resposta.json())