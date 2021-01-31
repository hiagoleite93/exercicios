"""
Iniciar com letra, pode conter numeros, separar _, letras minúsculas
"""

import math
nome = 'Luiz Otávio'
idade = 32
altura = 1.80
peso = 75
e_maior = idade > 18
imc = peso/(math.pow(altura, 2))
imc_1 = (f'{imc:.2f}')


print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior de idade? ', e_maior)
print(imc_1)

print(nome, 'tem', idade, 'anos de idade e tem', imc_1, 'de IMC.')

'''
#formatar
nome = 'Otavio'
sobrenome = 'Miranda'
nome_formatado = '{0:#^50} {1:@^50}' .format(nome, sobrenome)
print(nome_formatado)
print(nome.lower()) - tudo minusculo
print(nome.upper()) - tudo maiusculo
print(nome.title()) - Primeiras letas maiusculas
'''
