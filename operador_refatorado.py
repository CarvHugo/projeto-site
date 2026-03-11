import sqlite3
import os
from time import sleep

conexao = sqlite3.connect("cardapio.db")
cursor = conexao.cursor()

def estrutura_de_menu(titulo):
    print('-' * 58)
    sleep(0.03)
    print(titulo.center(65))
    sleep(0.03)
    
    if titulo not in ('\033[33mMENU PRINCIPAL\033[m', '\033[33mNOVO CADASTRO\033[m', '\033[33mALIMENTOS CADASTRADOS\033[m'):
        print('-' * 58)
        sleep(0.03)
        print('ou')
        sleep(0.03)
        print('\033[34mPressione ENTER para voltar\033[m')
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
    
def mostrar_opcoes(opcoes):
    for numero, opcao in enumerate(opcoes):
        print(f'\033[33m{numero + 1}\033[m - \033[34m{opcao}\033[m')
        sleep(0.03)
    print('-' * 58)
    
    
def retornar(voltar=''):
    while voltar == 'manualmente':
        voltar = str(input('\033[34mPressione ENTER para voltar \033[m'))
        os.system('cls')
    
    while voltar not in ('manualmente', ''):
        voltar = str(input('\033[31mDigite apenas ENTER para voltar\033[m'))
        os.system('cls')
        
    for ciclo in range(2):
                for pontos in range(4):
                    print('\rVoltando' + '.' * pontos, end='', flush=True)
                    sleep(0.03)
                os.system('cls')

def listagem():
    erro = ''
    while True:
        estrutura_de_menu('\033[33mMENU PRINCIPAL\033[m')
        mostrar_opcoes(opcoes_menu_principal)
        
        if erro:
            print(erro)
        
        erro = ''

        try:
            escolha = int(input('\033[32mSua Opção: \033[m'))
            
            if 1 > escolha or escolha > 5:
                os.system('cls')
                erro = '\033[31mEscolha um número inteiro válido de "1" a "5".\033[m'
        
        except ValueError:
            os.system('cls')
            erro = '\033[31mDigite um número inteiro!\033[m'
        
        except KeyboardInterrupt:
            os.system('cls')
            print('O usuário encerrou o programa de forma manual.')
            break
        
        else:
            if escolha == 1:
                os.system('cls')
                estrutura_de_menu('\033[33mALIMENTOS CADASTRADOS\033[m')
                cursor.execute("""SELECT * FROM produtos;""")
                rows = cursor.fetchall()
                print(f' {"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
                for id, nome, categoria, preco in rows:
                    print(f' {id:<5} {nome:<26} {categoria:<15}R$ {preco:<10.2f}')
                    sleep(0.03)
                print('-' * 58)
                retornar('manualmente')

listagem()