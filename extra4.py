# Como já vimos, programação é prática! Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e
# reforçar ainda mais seu aprendizado e o conteúdo da vez são dicionarios. Bora praticar?
import os
os.system('cls')

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dados_pessoais = {
    'nome': 'João Silva',
    'idade': 27,
    'estado': 'SP',
    'cidade': 'São Vicente'
}

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
dados_pessoais['idade'] += 1

# Adicione um campo de profissão para essa pessoa;
dados_pessoais['profissão'] = 'Motorista'


# Remova um item do dicionário.
del dados_pessoais['estado']

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros = {}
for i in range(1,6):
    numeros[i] = i*i
# SOLUCAO FORNECIDA:
# numeros_quadrados = {x: x**2 for x in range(1, 6)}

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
if 'estado civil' in dados_pessoais:
    print('O estado civil de {} é {}'.format(dados_pessoais['nome'], dados_pessoais['estado civil']))
else:
    print('O estado civil de {} não está cadastrado.'.format(dados_pessoais['nome']))


# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem = {}
palavras = frase.split() # cria um array com as palavras
for p in palavras:
    contagem[p] = contagem.get(p, 0) + 1
    # get: retorna valor da chave, e se a chave nao existir, retorna um valor default (0)