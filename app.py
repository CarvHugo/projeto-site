import sqlite3

conexao = sqlite3.connect("cardápio.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL
);
""")

produtos = [
    ("Pizza Margherita", "Pizza", 68.0),
    ("Refrigerante", "Bebida", 8.0),
    ("Lasanha", "Massa", 32.0)
]

while True:
    print('~' * 30)
    print('Menu Principal'.center(30))
    print('~' * 30)
    print('[ 1 ] Adicionar produto')
    print('[ 2 ] Ver lista de produtos')
    print('[ 3 ] Excluir registro')
    print('[ 4 ] Sair do programa')
    opcao = int(input('Sua escolha: '))
    if opcao == 1:
        def adicionar_produto(nome, categoria, preco):
            nome = (input('Digite o nome do produto: '))
            confirmacao = input('Confirma? [S/N] ')[0]
            cursor.execute(f"""INSERT INTO produtos (nome, categoria, preco)
            VALUES
            ('{nome}', '{categoria}', {preco})""")