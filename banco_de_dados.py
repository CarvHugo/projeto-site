import sqlite3

def checa_existencia_da_tabela_produtos():
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