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
    while voltar == 'V':
        voltar = str(input('\033[34mPressione ENTER para voltar \033[m'))
        os.system('cls')
    
    for ciclo in range(2):
                for pontos in range(4):
                    print('\rVoltando' + '.' * pontos, end='', flush=True)
                    sleep(0.03)
                os.system('cls')

def listagem():
    while True:
        estrutura_de_menu('\033[33mMENU PRINCIPAL\033[m')
        mostrar_opcoes(opcoes_menu_principal)

        try:
            escolha = int(input('\033[32mSua Opção: \033[m'))
            
            while 1 > escolha or escolha > 5:
                os.system('cls')
                estrutura_de_menu('\033[33mMENU PRINCIPAL\033[m')
                mostrar_opcoes(opcoes_menu_principal)
                print('\033[31mEscolha um valor inteiro válido de "1" a "5".\033[m')
                
                try:
                    escolha = int(input('\033[32mSua Opção: \033[m'))
                    
                except ValueError:
                    os.system('cls')
                    print('\033[31mDigite um número inteiro!\033[m')
    
        except ValueError:
            os.system('cls')
            print('\033[31mDigite um número inteiro!\033[m')
        
        except KeyboardInterrupt:
            os.system('cls')
            print('O usuário encerrou o programa de forma manual.')
            break
        
        else:
            if escolha == 1:
                estrutura_de_menu('\033[33mALIMENTOS CADASTRADOS\033[m')
    
listagem()