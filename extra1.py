'''
A função print() desempenha um papel fundamental para imprimir texto e variáveis no console ou em outro local de saída.
Ao longo das diferentes versões do Python, a sintaxe e os recursos dessa função evoluíram, oferecendo diversas maneiras de formatar e exibir mensagens.

Para praticar essa função, criamos a seguir uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.
Bora praticar então?
'''
### Exercícios

#1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura.\n')

#2 - Imprima a frase: 'Meu nome é {nome} e tenho {idade} anos', em que nome e idade precisam ser valores armazenados em variáveis.
nome = 'Victoria'
idade = 23
print(f'Meu nome é {nome} e tenho {idade} anos.\n')

#OU: print('Meu nome é {} e tenho {} anos.'.format(nome,idade))
#OU: print('Meu nome é %s e tenho %i anos.'%(nome,idade))

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
#A
#L
#U
#R
#A
print('A','L','U','R','A',sep='\n')

#4 - Imprima a frase: 'O valor arredondado de pi é: {pi_arredondado}' em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')

#OU: print('O valor arredondado de pi é: {:.2f}'.format(pi))

