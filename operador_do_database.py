import sqlite3
import os
from time import sleep
import sys

conexao = sqlite3.connect("cardapio.db")
cursor = conexao.cursor()

def estrutura_de_menu(titulo):
    os.system('cls')
    print('-' * 58)
    sleep(0.03)
    print(titulo.center(65))
    sleep(0.03)     
    print('-' * 58)
    sleep(0.03)

opcoes_menu_principal = [
    'Ver alimentos cadastrados',
    'Cadastrar novo alimento.',
    'Deletar registro.',
    'Editar registro.',
    'Sair do sistema.'
]

opcoes_menu_edicao = [
    'Editar preço.',
    'Editar nome.',
    'Editar categoria.'
]
    
def mostrar_opcoes(opcoes):
    for numero, opcao in enumerate(opcoes):
        print(f'\033[33m{numero + 1}\033[m - \033[34m{opcao}\033[m')
        sleep(0.03)
    print('-' * 58)
    
    
def retornar(voltar=''):
    while voltar == 'manualmente':
        voltar = input('\033[34mPressione ENTER para voltar \033[m')
        os.system('cls')
    
    while voltar not in ('manualmente', ''):
        voltar = input('\033[31mDigite apenas ENTER para voltar\033[m')
        os.system('cls')
        
    for ciclo in range(2):
                for pontos in range(4):
                    print('\rVoltando' + '.' * pontos, end='', flush=True)
                    sleep(0.03)
                os.system('cls')

def listagem():
    erro_menu = ''
    while True:
        estrutura_de_menu('\033[33mMENU PRINCIPAL\033[m')
        mostrar_opcoes(opcoes_menu_principal)
        
        if erro_menu:
            sleep(0.03)
            print(erro_menu)
            sleep(0.03)
        
        erro_menu = ''

        try:
            escolha = int(input('\033[32mSua Opção: \033[m'))
            
            if 1 > escolha or escolha > 5:
                os.system('cls')
                erro_menu = '\033[31mEscolha um número inteiro válido de "1" a "5".\033[m'
        
        except ValueError:
            os.system('cls')
            erro_menu = '\033[31mDigite um número inteiro!\033[m'
        
        except KeyboardInterrupt:
            os.system('cls')
            print('O usuário encerrou o programa de forma manual.')
            sys.exit()
            break
        
        else:
            if escolha == 1:
                estrutura_de_menu('\033[33mALIMENTOS CADASTRADOS\033[m')
                cursor.execute("""SELECT * FROM produtos;""")
                rows = cursor.fetchall()
                print(f' {"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
                for id, nome, categoria, preco in rows:
                    print(f' {id:<5} {nome:<26} {categoria:<15}R$ {preco:<10.2f}')
                    sleep(0.03)
                print('-' * 58)
                retornar('manualmente')
            
            elif escolha == 2:
                erro_cadastro = ''
                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    if erro_cadastro:
                        print(erro_cadastro)
                        sleep(0.03)
                        erro_cadastro = ''
                    try:
                        nome_alimento = ' '.join(input('Nome: ').split()).title()
                        if not nome_alimento.replace(' ', '').replace('-', '').isalpha():
                            raise ValueError
                    
                    except ValueError:
                        erro_cadastro = '\033[31mDigite um nome com caracteres alfabéticos!\033[m'
                        
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                    
                    else:
                        estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                        print(f'Nome: {nome_alimento}')
                        break

                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    print(f'Nome: {nome_alimento}')
                    
                    if erro_cadastro:
                        sleep(0.03)
                        print(erro_cadastro)
                        sleep(0.03)
                        erro_cadastro = ''
                    
                    try:
                        categoria_alimento = ' '.join(input('Categoria: ').split()).title()
                        if not categoria_alimento.replace(' ', '').replace('-', '').isalpha():
                            raise ValueError
                    
                    except ValueError:
                        erro_cadastro = '\033[31mDigite uma categoria com caracteres alfabéticos!\033[m'
                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                    
                    else:
                        estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                        print(f'Nome: {nome_alimento}')
                        sleep(0.03)
                        print(f'Categoria: {categoria_alimento}')
                        break
                
                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    print(f'Nome: {nome_alimento}')
                    sleep(0.03)
                    print(f'Categoria: {categoria_alimento}')
                    
                    if erro_cadastro:
                        sleep(0.03)
                        print(erro_cadastro)
                        sleep(0.03)
                        
                        erro_cadastro = ''
                    
                    try:
                        preco_alimento = str(input('Preço: R$ ')).replace(',', '.')
                        preco_alimento = float(preco_alimento)
                        
                        if preco_alimento < 0:
                            erro_cadastro = '\033[31mDigite um preço maior que zero!\033[m'
                            continue
                    
                    except ValueError:
                        erro_cadastro = '\033[31mDigite apenas números!\033[m'

                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                    
                    else:
                        estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                        def informacoes_produto():
                            sleep(0.03)
                            print(f'Nome: {nome_alimento}')
                            sleep(0.03)
                            print(f'Categoria: {categoria_alimento}')
                            sleep(0.03)
                            print(f'Preço: R$ {preco_alimento:.2f}')
                            sleep(0.03)
                        informacoes_produto()
                        break
                
                confirmacao = None
                while True:
                    estrutura_de_menu('\033[33mNOVO CADASTRO\033[m')
                    informacoes_produto()
                    
                    if confirmacao not in('S', 'N', None):
                        erro_cadastro = '\033[31mDigite apenas S ou N.\033[m'
                        print(erro_cadastro)
                        sleep(0.03)
                        erro_cadastro = ''
                        
                    try:
                        confirmacao = str(input('Você confirma? [S/N] ')).upper().strip()
                        
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                        
                    else:
                        if confirmacao == 'N':
                            os.system('cls')
                            retornar()
                            break
                        
                        elif confirmacao =='S':
                            cursor.execute(f"""INSERT INTO produtos (nome, categoria, preco)
                            VALUES
                            ('{nome_alimento}', '{categoria_alimento}', {preco_alimento});"""
                            )       
                            conexao.commit()
                            sleep(0.03)
                            print('\033[32mBanco de dados atualizado com sucesso!\033[m')
                            sleep(0.03)
                            retornar('manualmente')
                            break

            elif escolha == 3:
                erro_delecao = ''
                while True:
                    estrutura_de_menu('\033[31mDELEÇÃO DE REGISTROS\033[m')
                    def tela_delecao():
                        print('\033[33mPara deletar um registro da tabela, digite o número ID do \nalimento desejado.\033[m')
                        sleep(0.03)
                        print('\nou')
                        sleep(0.03)
                        print('\n\033[34mDigite ENTER para voltar ao MENU PRINCIPAL.\033[m')
                        sleep(0.03)
                        print('-' * 58)
                    tela_delecao()
                
                    if erro_delecao:
                        print(erro_delecao)
                        erro_delecao = ''
                    
                    try:
                        numero_id = input('ID ou ENTER: ').strip()
                        
                        if numero_id == '':
                            os.system('cls')
                            retornar()
                            break
                        
                        elif numero_id.isnumeric():
                            numero_id = int(numero_id)
                            
                        else:
                            raise ValueError
                    
                    except ValueError:
                        erro_delecao = '\033[31mDigite apenas o ID desejado ou ENTER\033[m'
                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                    
                    else:
                        cursor.execute(f"""SELECT id FROM produtos WHERE id = {numero_id};""")
                        resultado = cursor.fetchone()
                        
                        if resultado is None:
                            erro_delecao = f'\033[31mID {numero_id} não cadastrado\033[m'
                        
                        else:
                            estrutura_de_menu('\033[31mDELEÇÃO DE REGISTROS\033[m')
                            tela_delecao()
                            print(f'ID: {numero_id}')
                            break
                
                confirmacao = None            
                while True:
                    if numero_id == '':
                        break
                    estrutura_de_menu('\033[31mDELEÇÃO DE REGISTROS\033[m')
                    tela_delecao()
                    print(f'ID: {numero_id}')        
                    
                    
                    if confirmacao not in('S', 'N', None):
                        erro_delecao = '\033[31mDigite apenas S ou N.\033[m'
                        print(erro_delecao)
                        sleep(0.03)
                        erro_delecao = ''
            
                    try:
                        confirmacao = str(input('Você confirma? [S/N] ')).upper().strip()
                        
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                        
                    else:
                        if confirmacao == 'N':
                            os.system('cls')
                            retornar()
                            break
                        
                        elif confirmacao =='S': 
                            cursor.execute(f"""DELETE FROM produtos WHERE id = {numero_id};""")
                            conexao.commit()
                            print('\n\033[32mProduto deletado!\033[m')
                            retornar('manualmente')
                            break
            
            elif escolha == 4:
                erro_menu_edicao = ''
                erro_preco = ''
                while True:
                    estrutura_de_menu('\033[33mEDIÇÃO DE REGISTROS\033[m')
                    mostrar_opcoes(opcoes_menu_edicao)
                    
                    if erro_menu_edicao:
                        sleep(0.03)
                        print(erro_menu_edicao)
                        sleep(0.03)
                    
                        erro_menu_edicao = ''

                    try:
                        escolha_edicao = str(input('\033[32mSua Opção: \033[m'))
                        
                        if escolha_edicao == '':
                            os.system('cls')
                            retornar()
                            break
                            
                        
                        escolha_edicao = int(escolha_edicao)

                        if 1 > escolha_edicao or escolha_edicao > 3:
                            os.system('cls')
                            erro_menu_edicao = '\033[31mEscolha um número inteiro válido de "1" a "3".\033[m'
                        
                    
                    except ValueError:
                        os.system('cls')
                        erro_menu_edicao = '\033[31mDigite um número inteiro!\033[m'
                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                        sys.exit()
                        
                    else:
                        if escolha_edicao == 1:
                            while True:
                                estrutura_de_menu('\033[33mEDIÇÃO DE PREÇO\033[m')
                                def tela_preco():
                                    print('\033[34mPara editar o preço, digite o número ID do alimento\033[m')
                                    print('ou')
                                    print('\033[34mDigite ENTER para voltar\033[m')
                                    print('-' * 58)
                                tela_preco()
                                
                                if erro_preco:
                                    print(erro_preco)
                                    erro_preco = ''
                        
                                try:
                                    numero_id = input('ID ou ENTER: ').strip()
                                    
                                    if numero_id == '':
                                        os.system('cls')
                                        retornar()
                                        break
                                    
                                    elif numero_id.isnumeric():
                                        numero_id = int(numero_id)
                                        
                                    else:
                                        raise ValueError
                                
                                except ValueError:
                                    erro_preco = '\033[31mDigite apenas o ID desejado ou ENTER\033[m'
                                
                                except KeyboardInterrupt:
                                    os.system('cls')
                                    print('O usuário encerrou o programa de forma manual.')
                                    sys.exit()
                                    
                                else:
                                    cursor.execute(f"""
                                                   SELECT id FROM produtos WHERE id = {numero_id};
                                                   """)
                                    resultado = cursor.fetchone()
                                    if resultado != None:
                                        break
                                    erro_preco = f'\033[31mID {numero_id} não cadastrado\033[m'
                                    erro_preco = ''
                            
                                while True:
                                    estrutura_de_menu('\033[33mEDIÇÃO DE PREÇO\033[m')
                                    tela_preco()
                                    print(f'ID: {numero_id}')
                                    cursor.execute(f"""
                                                    SELECT nome, preco FROM produtos
                                                    WHERE id = {numero_id};
                                                    """)
                                    row = cursor.fetchone()
                                    nome, preco = row
                                    print(f'Alimento: {nome}\nPreço: R${preco:.2f}')
                                    if erro_preco:
                                        print(erro_preco)
                                        erro_preco = ''
                                    
                                    try:
                                        novo_preco = str(input('Novo preço: R$ ')).replace(',', '.')
                                        novo_preco = float(novo_preco)
                                        
                                        if novo_preco < 0:
                                            erro_preco = '\033[31mDigite um preço maior que zero\033[m'
                                            continue
                                    
                                    except ValueError:
                                        erro_preco = '\033[31mDigite apenas números!\033[m'

                                    except KeyboardInterrupt:
                                        os.system('cls')
                                        print('O usuário encerrou o programa de forma manual.')
                                        sys.exit()
                                    
                                    else:
                                        retornar('manualmente')
            
            elif escolha == 5:
                os.system('cls')
                print('-' * 58)
                sleep(0.03)
                for ciclo in range(6):
                    for pontos in range(4):
                        print(f'\r\033[34mSaindo do sistema{"." * pontos} \033[m', end='', flush=True)
                        sleep(0.07)
                print('\r\033[34mSaindo do sistema... Até logo!\033[m')
                sleep(0.7)
                print('-' * 58)
                break
listagem()