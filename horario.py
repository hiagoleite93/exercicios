horario = input('Digite um horario: ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Digite um horario de 0-23')

    else:
        if horario <= 11:
            print(f'Bom dia, são {horario} horas')

        elif horario <= 18:
            print(f'Boa tarde, são {horario} horas')

        else:
            print(f'Boa noite, são {horario} horas')

else:
    print('Digite um horario de 0-23')

