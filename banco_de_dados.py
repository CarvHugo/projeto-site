import sqlite3

def garantir_tabela_produtos():
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL
    );
    """)
    
    conexao.commit()
    conexao.close()

def buscar_produtos():
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, nome, categoria, preco FROM produtos;")
    produtos = cursor.fetchall()
    
    conexao.close()
    
    return produtos

def cadastra_produtos(nome, categoria, preco):
    nome = nome.strip()
    categoria = categoria.strip()
    
    if nome != "" and categoria != "" and preco > 0:
        conexao = sqlite3.connect("cardapio.db")
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)", (nome, categoria, preco))

        conexao.commit()
        conexao.close()

        return nome, categoria, preco
    
def tenta_delecao(id):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    verificador_de_linha = cursor.fetchone()
    print(verificador_de_linha)

    if verificador_de_linha is not None:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        
        conexao.commit()
        conexao.close()
        return {"message": f'{id} deletado!'}
    
    conexao.close()
    return None


def consulta_produto(id):
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
    
    return None

def atualiza_produto(id, nome=None, categoria=None, preco=None):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    informacoes_dos_produtos = (nome, categoria, preco)
    
    if informacoes_dos_produtos.count(None) == 3:
        conexao.close()
        return None
    
    linhas_afetadas = 0
    
    variavel_da_query_sql = ["nome", "categoria", "preco"]
        
    for contador, dado in enumerate(informacoes_dos_produtos):
        try:
            if dado is not None:
                cursor.execute("UPDATE produtos SET ? = ? WHERE id = ?", (variavel_da_query_sql[contador], dado, id))
                linhas_afetadas += cursor.rowcount
        
        except:
            continue
    

    if linhas_afetadas == 0:
        conexao.close()
        return 404
    
    conexao.commit()
    conexao.close()