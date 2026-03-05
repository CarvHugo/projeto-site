"""def adicionar_produto(nome, categoria, preco):
    print('~' * 30)
    print('Menu Principal'.center(30))
    print('~' * 30)
    cursor.execute(f"""#NSERT INTO produtos (nome, categoria, preco)
    #VALUES
    #('{nome}', '{categoria}', {preco})
    #"""
    #)

#Utilizados para fatiar a lista de tuplas.
#x = 0   #Index para selecionar o elemento da lista.
#y = 0   #Index para selecionar o elemento da tupla.


"""for produto in range(len(produtos)):
    if produto in produtos:
        print('Pulando... Produto já adicionado na lista.')
    else:
        adicionar_produto(
            produtos[x][y],
            produtos[x][y+1],
            produtos[x][y+2])
        x += 1  #Permite que a cada adição, prossiga pelos elementos da lista ao longo de seu comprimento.
   
conexao.commit()
conexao.close()

print("Banco criado com sucesso!")"""