# Como já vimos, programação é prática! Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e reforçar ainda mais seu aprendizado e o conteúdo da vez são listas, blocos de repetição e try except. Bora praticar?
### Exercícios

# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
numeros = []
for i in range(1,11):
    numeros.append(i)

# Lista com quatro nomes;
nomes = ['João','Maria','Lucas','Ana']

# Lista com o ano que você nasceu e o ano atual.
ano_nascimento_atual = [2001,2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
lista = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
for i in lista:
    print(i)
print()

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for n in range(10):
    if n%2==1:
        soma += n
print(soma)
print()

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
i = len(numeros) - 1
while i>=0:
    print(numeros[i])
    i-=1
print()

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
for attempt in range(10): # limita o numero de vezes que o codigo pode tentar novamente depois de falhar
    try:
        numero_escolhido = int(input('Escolha um número: '))
        for i in range(0,11):
            print('{} x {} = {}'.format(i, numero_escolhido, i*numero_escolhido))
    except:
        print('Houve um erro. Tente novamente.')
    else: # se nao houverem erros
        break # sai do for

print()
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista = [1, 23, '25', 2, None, 321, 5, 6, 'a?', 908]
soma = 0
convertidos = []
invalidos = []

for i in lista:
    try:
        soma += i
    except:
        try:
            soma += int(i)
            convertidos.append(i)
        except:
            invalidos.append(i)
print('A soma é {}. Os itens {} foram convertidos para int durante o calculo, e os itens {} não foram somados.'.format(soma,convertidos,invalidos))
print()

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_media = [1,6,9,5,9.5]
soma = 0
for i in lista_media:
    soma += i

try:
    print('A média é {}'.format(soma/len(lista_media)))
except ZeroDivisionError:
    print('A lista está vazia.')