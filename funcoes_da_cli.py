from time import sleep
import os
import sys

def estrutura_de_menu(titulo):
    os.system('cls')
    print('-' * 58)
    sleep(0.03)
    print(titulo.center(65))
    sleep(0.03)     
    print('-' * 58)
    sleep(0.03)
    
    
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