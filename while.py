'''x = 0
while x < 5:
    if x == 3:
        x = x + 1
        #break
        continue  # pula para o próximo laço

    print(x)
    x = x + 1

print('Acabou!')'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

else:
    print('Cheguei no else')
#o else so ocorre quando a condição for falsa.
#caso eu quebre o laço, com break, a condição não se torna falsa, por isso, não passa pelo else.