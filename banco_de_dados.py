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