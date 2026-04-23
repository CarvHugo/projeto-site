from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera tudo (ok para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/produtos")
async def listar_produtos():
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, nome, categoria, preco FROM produtos;")
    produtos = cursor.fetchall()
    
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
async def cadastro_de_produtos(produto: Produto):
    produto.nome = produto.nome.strip()
    produto.categoria = produto.categoria.strip()
    
    if produto.nome != "" and produto.categoria != "" and produto.preco > 0:
        conexao = sqlite3.connect("cardapio.db")
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)", (produto.nome, produto.categoria, produto.preco))

        conexao.commit()
        conexao.close()

        return produto
    
    raise HTTPException(status_code=422, detail="Ocorreu um erro com a validação dos dados! Digite dados válidos para cadastro.")