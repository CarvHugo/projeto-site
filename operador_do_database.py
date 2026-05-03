import os
from time import sleep
import sys
from api_client import obter_lista_do_cardapio, cadastrar_produto, deletar_produto, atualizar_produto, consultar_produto
from funcoes_da_cli import estrutura_de_menu, mostrar_opcoes, retornar

opcoes_menu_principal = [
    'Ver alimentos cadastrados',
    'Cadastrar novo alimento.',
    'Deletar registro.',
    'Editar registro.',
    'Informações.',
    'Sair do sistema.'
]

opcoes_menu_edicao = [
    'Editar preço.',
    'Editar nome.',
    'Editar categoria.'
]

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
            
            if 1 > escolha or escolha > 6:
                os.system('cls')
                erro_menu = '\033[31mEscolha um número inteiro válido de "1" a "6".\033[m'
        
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
                resultado = obter_lista_do_cardapio()
                if isinstance(resultado, list):
                    print(f'{"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
                    sleep(0.03)
            
                    for item in resultado:
                        print(f'{item["id"]:<5} {item["nome"]:<26} {item["categoria"]:<15} {item["preco"]:<10}')
                        sleep(0.03)
                        
                    print('-' * 58)
                    sleep(0.03)
                else:
                    print(resultado)
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
                        
                        if preco_alimento <= 0:
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
                            resultado = cadastrar_produto(nome_alimento, categoria_alimento, preco_alimento)
                            print(resultado)
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
                        sleep(0.03)
                    tela_delecao()
                
                    if erro_delecao:
                        print(erro_delecao)
                        sleep(0.03)
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
                    sleep(0.03)       
                    
                    
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
                            resultado = deletar_produto(numero_id)
                            print(resultado)
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
                                    sleep(0.03)
                                    print('ou')
                                    sleep(0.03)
                                    print('\033[34mPressione ENTER para voltar\033[m')
                                    sleep(0.03)
                                    print('-' * 58)
                                    sleep(0.03)
                                tela_preco()
                                
                                if erro_preco:
                                    print(erro_preco)
                                    sleep(0.03)
                                    erro_preco = ''
                        
                                try:
                                    numero_id = input('ID ou ENTER: ').strip()
                                    
                                    if numero_id == '':
                                        os.system('cls')
                                        retornar()
                                        break
                                    
                                    numero_id = int(numero_id)
                                                                    
                                except ValueError:
                                    erro_preco = '\033[31mDigite apenas o ID desejado ou ENTER\033[m'
                                    continue
                                
                                except KeyboardInterrupt:
                                    os.system('cls')
                                    print('O usuário encerrou o programa de forma manual.')
                                    sys.exit()
                                    
                                else:
                                    resultado_da_consulta = consultar_produto(numero_id)
                                    
                                    if isinstance(resultado_da_consulta, str):
                                        erro_preco = resultado_da_consulta
                                        continue
                                    erro_preco = ''
                            
                                while True:
                                    estrutura_de_menu('\033[33mEDIÇÃO DE PREÇO\033[m')
                                    tela_preco()
                                    if isinstance(resultado_da_consulta, dict):
                                        print(f'ID: {numero_id}')
                                        sleep(0.03)
                                        print(f"Nome: {resultado_da_consulta['Nome']}")
                                        sleep(0.03)
                                        print(f"Preço atual: R${resultado_da_consulta['Preço']:.2f}")
                                    if erro_preco:
                                        sleep(0.03)
                                        print(erro_preco)
                                        erro_preco = ''
                                        sleep(0.03)
                                    
                                    try:
                                        novo_preco = str(input('Novo preço: R$')).replace(',', '.')
                                        
                                        if novo_preco == '':
                                            break
                                        
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
                                        atualizacao_confirmada = atualizar_produto(id=numero_id, preco=novo_preco)
                                        print(atualizacao_confirmada)
                                        retornar('manualmente')
                                        break
                                break
                        
                        erro_nome = ''
                        if escolha_edicao == 2:
                            while True:
                                estrutura_de_menu('\033[33mEDIÇÃO DE NOME\033[m')
                                def tela_nome():
                                    print('\033[34mPara editar o nome, digite o número ID do alimento\033[m')
                                    sleep(0.03)
                                    print('ou')
                                    sleep(0.03)
                                    print('\033[34mPressione ENTER para voltar\033[m')
                                    sleep(0.03)
                                    print('-' * 58)
                                    sleep(0.03)
                                tela_nome()
                                
                                if erro_nome:
                                    print(erro_nome)
                                    erro_nome = ''
                                    sleep(0.03)
                        
                                try:
                                    numero_id = input('ID ou ENTER: ').strip()
                                    
                                    if numero_id == '':
                                        os.system('cls')
                                        retornar()
                                        break
                                    
                                    numero_id = int(numero_id)
                                                                    
                                except ValueError:
                                    erro_nome = '\033[31mDigite apenas o ID desejado ou ENTER\033[m'
                                    continue
                                
                                except KeyboardInterrupt:
                                    os.system('cls')
                                    print('O usuário encerrou o programa de forma manual.')
                                    sys.exit()
                                    
                                else:
                                    resultado_da_consulta = consultar_produto(numero_id)
                                    
                                    if isinstance(resultado_da_consulta, str):
                                        erro_nome = resultado_da_consulta
                                        continue
                                    erro_nome = ''
                            
                                while True:
                                    estrutura_de_menu('\033[33mEDIÇÃO DE NOME\033[m')
                                    tela_nome()
                                    if isinstance(resultado_da_consulta, dict):
                                        print(f'ID: {numero_id}')
                                        sleep(0.03)
                                        print(f"Nome atual: {resultado_da_consulta['Nome']}")
                                    if erro_nome:
                                        sleep(0.03)
                                        print(erro_nome)
                                        erro_nome = ''
                                        sleep(0.03)
                                    
                                    try:
                                        novo_nome = input('Novo nome: ')
                                        
                                        if novo_nome == '':
                                            break
                                    
                                        if not novo_nome.isalpha():
                                            raise ValueError
                                    
                                    except ValueError:
                                        erro_nome = '\033[31mDigite apenas caracteres alfabéticos!\033[m'
                                        continue

                                    except KeyboardInterrupt:
                                        os.system('cls')
                                        print('O usuário encerrou o programa de forma manual.')
                                        sys.exit()
                                    
                                    else:
                                        atualizacao_confirmada = atualizar_produto(id=numero_id, nome=novo_nome)
                                        print(atualizacao_confirmada)
                                        retornar('manualmente')
                                        break
                                break
                        
                        erro_categoria = ''
                        if escolha_edicao == 3:
                            while True:
                                estrutura_de_menu('\033[33mEDIÇÃO DE CATEGORIA\033[m')
                                def tela_categoria():
                                    print('\033[34mPara editar a categoria, digite o número ID do alimento\033[m')
                                    sleep(0.03)
                                    print('ou')
                                    sleep(0.03)
                                    print('\033[34mPressione ENTER para voltar\033[m')
                                    sleep(0.03)
                                    print('-' * 58)
                                    sleep(0.03)
                                tela_categoria()
                                
                                if erro_categoria:
                                    print(erro_categoria)
                                    erro_categoria = ''
                                    sleep(0.03)
                        
                                try:
                                    numero_id = input('ID ou ENTER: ').strip()
                                    
                                    if numero_id == '':
                                        os.system('cls')
                                        retornar()
                                        break
                                    
                                    numero_id = int(numero_id)
                                                                    
                                except ValueError:
                                    erro_categoria = '\033[31mDigite apenas o ID desejado ou ENTER\033[m'
                                    continue
                                
                                except KeyboardInterrupt:
                                    os.system('cls')
                                    print('O usuário encerrou o programa de forma manual.')
                                    sys.exit()
                                    
                                else:
                                    resultado_da_consulta = consultar_produto(numero_id)
                                    
                                    if isinstance(resultado_da_consulta, str):
                                        erro_categoria = resultado_da_consulta
                                        continue
                                    erro_categoria = ''
                            
                                while True:
                                    estrutura_de_menu('\033[33mEDIÇÃO DE CATEGORIA\033[m')
                                    tela_categoria()
                                    if isinstance(resultado_da_consulta, dict):
                                        print(f'ID: {numero_id}')
                                        sleep(0.03)
                                        print(f"Alimento: {resultado_da_consulta['Nome']}")
                                        sleep(0.03)
                                        print(f"Categoria atual: {resultado_da_consulta['Categoria']}")
                                        sleep(0.03)
                                    if erro_categoria:
                                        print(erro_categoria)
                                        erro_categoria = ''
                                        sleep(0.03)
                                    
                                    try:
                                        nova_categoria = input('Nova categoria: ')
                                        
                                        if nova_categoria == '':
                                            break
                                    
                                        if not nova_categoria.isalpha():
                                            raise ValueError
                                        
                                    except ValueError:
                                        erro_categoria = '\033[31mDigite apenas caracteres alfabéticos!\033[m'

                                    except KeyboardInterrupt:
                                        os.system('cls')
                                        print('O usuário encerrou o programa de forma manual.')
                                        sys.exit()
                                    
                                    else:
                                        atualizacao_confirmada = atualizar_produto(id=numero_id, categoria=nova_categoria)
                                        print(atualizacao_confirmada)
                                        retornar('manualmente')
                                        break
                                break
                            
            elif escolha == 5:
                estrutura_de_menu('\033[33mINFORMAÇÕES DO PROGRAMA\033[m')
                print('Sistema de cardápio virtual feito para agilizar a sua')
                sleep(0.03)
                print('logística empresarial.')
                sleep(0.03)
                print('\nDesenvolvido por Hugo Carvalho')
                sleep(0.03)
                print('\nE-mail: hugoncarv@gmail.com')
                sleep(0.03)
                print('Telefone (também WhatsApp): +55(21)97401-2985')
                sleep(0.03)
                retornar('manualmente')
                
            elif escolha == 6:
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