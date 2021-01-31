cpf = input('CPF: ')

if cpf.isdigit() and len(cpf) == 11:
    print('Analisando o CPF...')
else:
    print('ERROR')

cpf_novo = cpf[:-2]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(cpf_novo[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)


        if d > 9:
            d = 0
        total = 0
        cpf_novo += str(d)

seq = cpf_novo == str(cpf_novo[0]) * len(cpf)
if cpf == cpf_novo and not seq:
    print('Valido')
else:
    print('Inválido')










