from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

from banco_de_dados import garantir_tabela_produtos, buscar_produtos, cadastra_produtos, tenta_delecao, consulta_produto, atualiza_produto

app = FastAPI()

API_KEY = os.getenv("API_KEY")

def valida_api_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key inválida!")

@app.on_event("startup")
def inicializar_banco():
    garantir_tabela_produtos()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera tudo (ok para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float
    
    
class ProdutoPatch(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None
    preco: Optional[float] = None


@app.get("/produtos")
async def listar_produtos():
    produtos = buscar_produtos()
    
    lista_produtos = []
    
    for coluna in produtos:
        lista_produtos.append({
            "id": coluna[0],
            "nome": coluna[1],
            "categoria": coluna[2],
            "preco": coluna[3]
        })

    return lista_produtos

@app.post("/produtos")
async def cadastro_de_produtos(produto: Produto, x_api_key: str = Header()):
    valida_api_key(x_api_key)
    
    if not produto.nome or not produto.categoria or produto.preco <= 0:
        raise HTTPException(status_code=422, detail="Ocorreu um erro com a validação dos dados! Digite dados válidos para cadastro.")
    
    produto = cadastra_produtos(produto.nome, produto.categoria, produto.preco)
    
    return produto

@app.delete("/produtos/{id}")
async def delecao_de_produtos(id: int, x_api_key: str = Header()):
    valida_api_key(x_api_key)
    
    delecao = tenta_delecao(id)
    
    if delecao is None:
        raise HTTPException(status_code=404, detail=f"Deleção falhou! O produto de ID {id} não foi encontrado.")

    return delecao

@app.patch("/produtos/{id}")
async def atualizar_produto(id: int, produtopatch: ProdutoPatch, x_api_key: str = Header()):
    valida_api_key(x_api_key)
    
    atualizacao = atualiza_produto(id, produtopatch.nome, produtopatch.categoria, produtopatch.preco)
    
    if atualizacao == None:
        raise HTTPException(status_code=422, detail="É necessário fornecer algum dado para atualização!")
    
    if atualizacao == False:
        raise HTTPException(status_code=404, detail=f"Erro! ID {id} não encontrado.")

    
@app.get("/produtos/{id}")
async def consultar_produto(id: int):
    produto = consulta_produto(id)
    
    if produto is None:
        raise HTTPException(status_code=404, detail=f'Produto de ID {id} não encontrado!')
    
    return produto