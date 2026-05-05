from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel
from typing import Optional

from banco_de_dados import checa_existencia_da_tabela_produtos

app = FastAPI()

@app.on_event("startup")
def funcao_de_inicializacao():
    checa_existencia_da_tabela_produtos()

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

@app.delete("/produtos/{id}")
async def delecao_de_produtos(id: int):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    verificador_de_linha = cursor.fetchone()
    
    if verificador_de_linha is not None:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        
        conexao.commit()
        conexao.close()
        return {"message": f'{id} deletado!'}
    
    conexao.close()
    
    raise HTTPException(status_code=404, detail=f"Deleção falhou! O produto de ID {id} não foi encontrado.")

@app.patch("/produtos/{id}")
async def atualizar_produto(id: int, produtopatch: ProdutoPatch):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    if (produtopatch.nome, produtopatch.categoria, produtopatch.preco).count(None) == 3:
        conexao.close()
        raise HTTPException(status_code=422, detail="É necessário fornecer algum dado para atualização!")
    
    linhas_afetadas = 0
        
    if produtopatch.nome is not None:
        cursor.execute("UPDATE produtos SET nome = ? WHERE id = ?", (produtopatch.nome, id))
        linhas_afetadas += cursor.rowcount
            
    if produtopatch.categoria is not None:
        cursor.execute("UPDATE produtos SET categoria = ? WHERE id = ?", (produtopatch.categoria, id))
        linhas_afetadas += cursor.rowcount
            
    if produtopatch.preco is not None:
        cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (produtopatch.preco, id))
        linhas_afetadas += cursor.rowcount
    
    if linhas_afetadas == 0:
        conexao.close()
        raise HTTPException(status_code=404, detail=f"Erro! ID {id} não encontrado.")
    
    conexao.commit()
    conexao.close()
    
@app.get("/produtos/{id}")
async def consultar_produto(id: int):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome, categoria, preco FROM produtos WHERE id = ?;", (id,))
    produto = cursor.fetchone()
    
    if produto:
        nome, categoria, preco = produto
        dados = {}
        
        dados['Nome'] = nome
        dados['Categoria'] = categoria
        dados['Preço'] = preco
        
        return dados
    
    else:
        raise HTTPException(status_code=404, detail=f'Número de ID {id} não encontrado!')