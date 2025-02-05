import os

# FUNCOES
def exibir_nome_app():
    # Formatacao feita com 'fsymbols'
    # Aspas triplhas mantem a formatacao do texto
    print(""" ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

def exibir_opcoes():
    # Menu para cadastrar restaurantes
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def encerrar_app():
    os.system('cls') # WINDOWS
    #os.system('clear') # MACOS
    print('Encerrando o app')

def escolher_opcao():
    # Input: Receber informacao do usuario

    # opcao_escolhida = input('Escolha uma opção: ') --- se deixar assim, ela vai retornar como string, nao int
    # Jeitos de garantir que ele seja um int:
    # opcao escolhida = int(opcao_escolhida) --- converte o string armazenado em um int
    # OU, converter na hora do input:
    opcao_escolhida = int(input('Escolha uma opção: '))
    
    if opcao_escolhida == 1:
        print('Cadastrar restaurante\n')
    elif opcao_escolhida == 2:
        print('Listar restaurante\n')
    elif opcao_escolhida == 3:
        print('Ativar restaurante\n')
    else:
        encerrar_app()

def main():
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

# Indica que esse e o codigo principal, nao um que sera importado por outros
if __name__ == '__main__':
    main()