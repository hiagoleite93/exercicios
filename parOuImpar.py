numero = input('Digite um número: ')
if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print('Número par')
    elif numero % 2 != 0:
        print('Numero ímpar')
else:
    print('Isso não é um número inteiro')



