# apend - insere um elemento no final da lista
# insert - inclui um elemento em um determinado indice == l2.insert(0, 'banana')
# pop- deleta o ultimo elemento da lista
# del - deleta um elemento em um determinado indice == del(l2[0])
# range


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Aaaaah isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Muito bem, a letra {letra} existe na palavra secreta.')

    else:
        print(f'Poxa, a letra {letra} não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Muito bem, você ganhou! A palavra era {secreto_temporario}')
        break

    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
