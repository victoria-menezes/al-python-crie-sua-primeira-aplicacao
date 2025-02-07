import os

### VARIAVEIS
restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa','ativo':False},
    {'nome':'Pizzaria Super', 'categoria':'Pizza','ativo':True},
    {'nome':'Cantina', 'categoria':'Italiana','ativo':False}
    ]

os_usuario = 'Windows'



### FUNCOES


## Funcoes tecnicas
def exibir_nome_app():
    """Exibe o nome formatado do aplicativo."""
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

def exibir_opcoes():
    """Exibe um menu enumerado de opções."""
    
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar / Desativar restaurantes')
    print('4. Sair\n')

def limpar_console(os_atual = 'Windows'):
    """Limpa o console.
    
    Parameters
    ----------
    os_atual : str, default: 'Windows'
    """
    match os_atual:
        case 'MacOS':
            os.system('clear') # MACOS
        case _:
            os.system('cls') # WINDOWS

def linha(texto, simbolo = '='):
    """Gera uma linha de extensão variável de acordo com o texto dado.
    
    Parameters
    ----------
    texto : str
    simbolo : str, default: '='
    """
    print(len(texto)*simbolo)

def nova_pagina(titulo = 'Nova página'):
    """Limpa o console e escreve o título da página nova.
    
    Parameters
    ----------
    titulo : str, default: 'Nova página'
    """
    limpar_console(os_usuario)
    
    linha(titulo)
    print('{}'.format(titulo))
    linha(titulo)
    print()

def voltar_tela_principal():
    """Volta o aplicativo ao menu inicial."""
    input('\nDigite ENTER para voltar ao menu principal ')
    main()

def encerrar_app():
    """Limpa o console e encerra o aplicativo."""
    nova_pagina('Encerrando app...')

def opcao_invalida():
    """Mostra uma mensagem de erro, e volta para o menu principal."""
    print('\nOpção inválida')
    voltar_tela_principal()


## Funcoes restaurante
def cadastrar_restaurante():
    """Cadastro de um novo registro na lista de restaurantes."""
    nova_pagina('Cadastro de novos restaurantes')
    
    nome_restaurante = input('O nome do restaurante: ')
    categoria = input('A categoria do restaurante {}: '.format(nome_restaurante))

    dict_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dict_restaurante)
    
    print('')
    print('{} cadastrado com sucesso'.format(nome_restaurante))
    voltar_tela_principal()

def listar_restaurante():
    """Escreve uma lista de todos os restaurantes registrados, sua categoria e estado de ativação."""
    nova_pagina('Listando os restaurantes')

    cabecalho = '{} {} {}'.format("Nome".ljust(21), "Categoria".ljust(20), "Status")
    print(cabecalho)
    linha(cabecalho)
    for r in restaurantes:
        nome_restaurante = r['nome']
        categoria = r['categoria']
        ativacao = 'Ativado' if r['ativo'] else 'Desativado'
        print('.{} {} {}'.format(nome_restaurante.ljust(20), categoria.ljust(20), ativacao))
    
    voltar_tela_principal()

def toggle_restaurante():
    """Deixa um restaurante ativo inativo, e vice-versa."""
    nova_pagina("Atualizar restaurantes")
    nome_restaurante = input('Digite o nome do restaurante que deve ser atualizado: ')
    
    for r in restaurantes:
        encontrado = False
        if nome_restaurante == r['nome']:
            r['ativo'] = not r['ativo']
            print('O restaurante {} foi ativado.'.format(nome_restaurante) if r['ativo'] else 'O restaurante {} foi desativado.'.format(nome_restaurante))
            encontrado = True
            voltar_tela_principal()
            break
    if not encontrado:
        opcao_invalida()


## Funcao menu
def escolher_opcao():
    """Pede ao usuário escolher uma das opções do menu, e aciona as funções equivalentes à escolha feita."""
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
            toggle_restaurante()
        elif opcao_escolhida == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except Exception as e: #...rode esse.
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