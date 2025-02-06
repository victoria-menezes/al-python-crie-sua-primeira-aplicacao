import os

### VARIAVEIS
restaurantes = ['Pizzaria', 'Sushi Central']



### FUNCOES
## Funcoes tecnicas
def exibir_nome_app():
    # Formatacao feita com 'fsymbols'
    # Aspas triplhas mantem a formatacao do texto
    print(""" 
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

os_usuario = 'Windows'

def exibir_opcoes():
    # Menu para cadastrar restaurantes
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def limpar_console(os_atual = 'Windows'):
    match os_atual:
        case 'MacOS':
            os.system('clear') # MACOS
        case _:
            os.system('cls') # WINDOWS

def nova_pagina(titulo = 'Nova página'):
    limpar_console(os_usuario)
    print('{}\n'.format(titulo))

def voltar_tela_principal():
    input('\nDigite ENTER para voltar ao menu principal ')
    main()

def encerrar_app():
    nova_pagina('Encerrando app..')

def opcao_invalida():
    print('\nOpção inválida\n')
    voltar_tela_principal()


## Funcoes restaurante
def cadastrar_restaurante():
    nova_pagina('Cadastro de novos restaurantes')
    
    nome_restaurante = input('O nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    
    print('')
    print('{} cadastrado com sucesso'.format(nome_restaurante))
    voltar_tela_principal()

def listar_restaurante():
    nova_pagina('Listando os restaurantes')

    for r in restaurantes:
        print('.{}'.format(r))
    voltar_tela_principal()

def ativar_restaurante():
    pass


## Funcao menu
def escolher_opcao():
    # Input: Receber informacao do usuario

    # opcao_escolhida = input('Escolha uma opção: ') --- se deixar assim, ela vai retornar como string, nao int
    # Jeitos de garantir que ele seja um int:
    # opcao escolhida = int(opcao_escolhida) --- converte o string armazenado em um int
    # OU, converter na hora do input:
    try: #tente rodas esse codigo, e se nao conseguir...
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('')
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except: #...rode esse.
        opcao_invalida()


## Funcao MAIN
def main():
    limpar_console(os_usuario)
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

# Indica que esse e o codigo principal, nao um que sera importado por outros
if __name__ == '__main__':
    main()