import sqlite3
import operador_do_database as ops

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

conexao.close()
ops.listagem()
