import sqlite3
import os
from time import sleep

conexao = sqlite3.connect("cardapio.db")
cursor = conexao.cursor()

def listagem():
    while True:
        print('-' * 58)
        sleep(0.03)
        print('\033[33mMENU PRINCIPAL\033[m'.center(65))
        sleep(0.03)
        print('-' * 58)
        sleep(0.03)
        opcoes = ['Ver alimentos cadastrados.',
                  'Cadastrar novo alimento.',
                  'Deletar registro.',
                  'Editar registro.',
                  'Sair do sistema.']
        
        def retornar(voltar=''):
            while voltar not in ('V', 'v'):
                    voltar = str(input('\033[34mDigite v para voltar: \033[m'))
                    os.system('cls')
            
            for ciclo in range(2):
                for pontos in range(4):
                    print('\rVoltando' + '.' * pontos, end='', flush=True)
                    sleep(0.03)
                os.system('cls')
            
        for numero, opcao in enumerate(opcoes):
            print(f'\033[33m{numero + 1}\033[m - \033[34m{opcao}\033[m')
            sleep(0.03)
        print('-' * 58)

        try:
            escolha = int(input('\033[32mSua Opção: \033[m'))
            if 1 > escolha or escolha > 5:
                os.system('cls')
                print('\033[31mEscolha um valor inteiro válido de "1" a "5".\033[m')
        
        except ValueError:
            os.system('cls')
            print('\033[31mDigite um número inteiro!\033[m')
        
        except KeyboardInterrupt:
            os.system('cls')
            print('O usuário encerrou o programa de forma manual.')
            break
        
        else:
            if escolha == 1:
                os.system('cls')
                print('-' * 58)
                sleep(0.03)
                print('\033[33mALIMENTOS CADASTRADOS\033[m'.center(65))
                sleep(0.03)
                print('-' * 58)
                sleep(0.03)
                cursor.execute("""SELECT * FROM produtos""")
                rows = cursor.fetchall()
                print(f' {"ID":<5} {"Nome":<26} {"Categoria":<15} {"Preço":<10}')
                for id, nome, categoria, preco in rows:
                    print(f' {id:<5} {nome:<26} {categoria:<15}R$ {preco:<10.2f}')
                    sleep(0.03)
                print('-' * 58)
                retornar()

            elif escolha == 2:
                def tela_cadastro():
                    os.system('cls')
                    print('-' * 58)
                    sleep(0.03)
                    print('\033[33mNOVO CADASTRO\033[m'.center(65))
                    sleep(0.03)
                    print('-' * 58)
                tela_cadastro()
                while True:
                    try:
                        nome_alimento = str(input('Nome: '))
                        if not nome_alimento.replace(' ','').isalpha():
                            raise ValueError
                    
                    except ValueError:
                        tela_cadastro()
                        sleep(0.03)
                        print('\033[31mDigite um nome com caracteres alfabéticos!\033[m')
                        sleep(0.03)
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                    
                    else:
                        tela_cadastro()
                        sleep(0.03)
                        print(f'Nome: {nome_alimento}')
                        sleep(0.03)
                        break
                
                while True:
                    try:
                        categoria_alimento = str(input('Categoria: '))
                        if categoria_alimento.isnumeric():
                            raise ValueError
                    except ValueError:
                        tela_cadastro()
                        sleep(0.03)
                        print(f'Nome: {nome_alimento}')
                        sleep(0.03)
                        print('\033[31mDigite uma categoria com caracteres alfabéticos!\033[m')
                        sleep(0.03)
                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                    else:
                        tela_cadastro()
                        sleep(0.03)
                        print(f'Nome: {nome_alimento}')
                        sleep(0.03)
                        print(f'Categoria: {categoria_alimento}')
                        sleep(0.03)
                        break
                
                while True:
                    try:
                        preco_alimento = str(input('Preço R$: ')).replace(',', '.')
                        preco_alimento = float(preco_alimento)
                    
                    except ValueError:
                        tela_cadastro()
                        print(f'Nome: {nome_alimento}')
                        sleep(0.03)
                        print(f'Categoria: {categoria_alimento}')
                        sleep(0.03)
                        print('\033[31mDigite apenas números!\033[m')
                        sleep(0.03)
                    
                    except KeyboardInterrupt:
                        os.system('cls')
                        print('O usuário encerrou o programa de forma manual.')
                    
                    else:
                        tela_cadastro()
                        def informacoes_produto():
                            sleep(0.03)
                            print(f'Nome: {nome_alimento}')
                            sleep(0.03)
                            print(f'Categoria: {categoria_alimento}')
                            sleep(0.03)
                            print(f'Preço R$: {preco_alimento}')
                            sleep(0.03)
                        informacoes_produto()
                        break
                
                confirmacao = ''
                while confirmacao not in ('S', 's', 'N', 'n'):
                    tela_cadastro()
                    informacoes_produto()
                    if confirmacao not in ('', 'S', 's', 'N', 'n'):
                        print('\033[31mDigite apenas s ou n!\033[m')
                    confirmacao = str(input('Você confirma? [S/N] '))
                    if confirmacao in ('N', 'n'):
                        escolha = 1
                        os.system('cls')
                        retornar('v')
                    elif confirmacao in ('S', 's'):
                        cursor.execute(f"""INSERT INTO produtos (nome, categoria, preco)
                        VALUES
                        ('{nome_alimento}', '{categoria_alimento}', {preco_alimento})"""
                        )       
                        conexao.commit()
                        sleep(0.03)
                        print('\033[32mBanco de dados atualizado com sucesso!\033[m')
                        sleep(0.03)
                        retornar()

            elif escolha == 3:
                def tela_delecao():
                    os.system('cls')
                    print('-' * 58)
                    sleep(0.03)
                    print(f'\033[31mDELEÇÃO DE REGISTROS\033[m'.center(65))
                    sleep(0.03)
                    print('-' * 58)
                    sleep(0.03)
                    print('\033[33mPara deletar um registro da tabela, digite o número ID do \nalimento desejado.\033[m')
                    sleep(0.03)
                    print('\nou')
                    sleep(0.03)
                    print('\n\033[34mDigite v para voltar ao MENU PRINCIPAL.\033[m')
                    sleep(0.03)
                tela_delecao()
                
                numero_id = str(input('\nID: '))
                if numero_id.isnumeric():
                    numero_id = int(numero_id)
                    cursor.execute(f"""DELETE FROM produtos WHERE id = {numero_id};""")
                    conexao.commit()
                    print('\n\033[32mProduto deletado!\033[m')
                    retornar()
                
                elif numero_id.isalpha() and numero_id in ('V','v'):
                    os.system('cls')
                    retornar(numero_id)
                
                else:
                    while not numero_id == 'v' and not numero_id.isnumeric():
                        os.system('cls')
                        tela_delecao()
                        sleep(0.03)
                        print('\033[31mEntrada inválida! Digite apenas o número ID ou v.\033[m')
                        numero_id = str(input('ID: '))
                        
                        if numero_id in ('V', 'v'):
                            os.system('cls')
                            retornar(numero_id)
                        
                        else:
                            if numero_id.isnumeric():
                                numero_id = int(numero_id)
                                cursor.execute(f"""DELETE FROM produtos WHERE id = {numero_id};""")
                                conexao.commit()
                                print('\n\033[32mProduto deletado!\033[m')
                                retornar()
                                numero_id = str(numero_id)

            elif escolha == 4:
                os.system('cls')
                print('-' * 58)
                sleep(0.03)
                print('\033[33mEDIÇÃO DE REGISTROS\033[m'.center(65))
                sleep(0.03)
                print('-' * 58)
                sleep(0.03)

                opcoes_edicao = [
                    'Editar preço.',
                    'Editar categoria.',
                    'Editar nome.'
                          ]
                for numero, opcao in enumerate(opcoes_edicao):
                    print(f'\033[33m{numero + 1}\033[m - \033[34m{opcao}\033[m')
                    sleep(0.03)
                print('\nou')
                sleep(0.03)
                print('\n\033[34mDigite v para voltar.\033[m')
                sleep(0.03)
                print('-' * 58)
                sleep(0.03)
                escolha_2 = int(input('\033[32mSua opção: \033[m'))
            
            elif escolha == 5:
                os.system('cls')
                print('-' * 58)
                sleep(0.03)
                for ciclo in range(6):
                    for pontos in range(4):
                        print('\r\033[34mSaindo do sistema' + '.\033[m' * pontos, end='', flush=True)
                        sleep(0.07)
                print('\r\033[34mSaindo do sistema... Até logo!\033[m')
                sleep(0.7)
                print('-' * 58)
                break