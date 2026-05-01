import requests
from requests.exceptions import ConnectionError, RequestException

def obter_lista_do_cardapio():
    try:
        resposta = requests.get("http://127.0.0.1:8000/produtos")

    except ConnectionError:
        return (f'\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')

    except RequestException:
        return(f'\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        produtos = resposta.json()
        
        return produtos
    
    else:    
        return(f'\033[31mOcorreu um erro ao buscar os produtos!\033[m. HTTP {resposta.status_code}')

def cadastrar_produto(nome, categoria, preco):
    url_base = "http://127.0.0.1:8000"
    
    try:
    
        resposta = requests.post(
            url_base + "/produtos",
            
            json={
                "nome": nome,
                "categoria": categoria,
                "preco": preco
            }
        )
    
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return(f'\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        return (f'\033[32mProduto cadastrado com sucesso no banco de dados! HTTP {resposta.status_code}\033[m')
    
    else:
        return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')
    
def deletar_produto(id: int):
    url_base = "http://127.0.0.1:8000"
    
    try:
        resposta = requests.delete(f'{url_base}/produtos/{id}')
        
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return ('\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        return (f'\033[32mProduto deletado com sucesso! HTTP {resposta.status_code}\033[m')
    
    else:
        if resposta.status_code == 404:
            detalhe_da_resposta = resposta.json()['detail']
            return f'\033[31m{detalhe_da_resposta}\033[m'
        
        return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')
    
def atualizar_produto(id=None, nome=None, categoria=None, preco=None):
    url_base = "http://127.0.0.1:8000"
    
    dados = {}
    
    if nome is not None:
        dados['nome'] = nome
        
    if categoria is not None:
        dados['categoria'] = categoria
        
    if preco is not None:
        dados['preco'] = preco 
    
    try:
        resposta = requests.patch(
        f'{url_base}/produtos/{id}', json=dados)   
    
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return ('\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200,300):
        return (f"\033[32mProduto atualizado com sucesso! HTTP {resposta.status_code}\033[m")
    
    elif resposta.status_code in (404, 422):
        detalhe_da_resposta = resposta.json()['detail']
        return (f'\033[31m{detalhe_da_resposta}\033[m')
    
    return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')

def consultar_produto(id):
    url_base = "http://127.0.0.1:8000"
    
    try:
        resposta = requests.get(f'{url_base}/produtos/{id}')
        
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return ('\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in (200, 300):
        produto = resposta.json()
        
        return produto
    
    elif resposta.status_code == 404:
        resposta = resposta.json()
        resposta = resposta['detail']
        
        return (f'\033[31m{resposta}\033[m')