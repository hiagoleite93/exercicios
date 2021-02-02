import random

numero_sistema = random.randint(1, 20)
digitadas = []

chances = 10

while True:
    if chances <= 0:
        print('Você perdeu.')
        break

    numero_jogador = int(input('Digite um número de 1-20: '))

    if numero_jogador > 100:
        print('Assim não vale, digite um número de 1 a 20')
        continue

    digitadas.append(numero_jogador)

    if numero_jogador < numero_sistema:
        print('Quase lá, chute um número mais alto!')


    elif numero_jogador > numero_sistema:
        print('Quaaase, chute um número mais baixo')


    else:
        print(f'Parabéns, você acertou, o número era: {numero_sistema}')

    if numero_jogador != numero_sistema:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
