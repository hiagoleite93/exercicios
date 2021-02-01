nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))
ano_Atual = 2021
ano_Nascimento = ano_Atual-idade
imc = peso/altura**2

print(f'{nome} tem {idade} nasceu em {ano_Nascimento} e seu IMC é {imc:.2f}.')



