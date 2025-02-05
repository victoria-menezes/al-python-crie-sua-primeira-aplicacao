# Como já vimos, programação é prática!
# Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e reforçar ainda mais seu aprendizado e o conteúdo da vez são condicionais. Bora praticar?

### Exercícios
# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} é par.')
else:
    print(f'{num} é ímpar.')
print("")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Digite sua idade: '))
if idade <= 12:
    print('Você é criança.')
elif idade <= 18:
    print('Você é adolescente')
else:
    print('Você é adulto.')


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
usuario = 'Joao_Silva'
senha = 'd07m06'

usuario_input = input('\nDigite o usuário: ')
senha_input = input('Digite a senha: ')

if usuario == usuario_input and senha == senha_input:
    print('Acesso autorizado.')
else:
    print('Usuário ou senha incorretos.')


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

x = float(input('\nX: '))
y = float(input('Y: '))

if x>0 and y>0:
    print('O ponto está no Primeiro Quadrante.')
elif x<0 and y>0:
    print('O ponto está no Segundo Quadrante.')
elif x<0 and y<0:
    print('O ponto está no Terceiro Quadrante.')
elif x>0 and y<0:
    print('O ponto está no Quarto Quadrante.')
else:
    if x == 0 and y == 0:
        print ('O ponto está na origem.')
    elif y == 0:
        print ('O ponto está no eixo X.')
    else:
        print ('O ponto está no eixo Y.')