perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
        },
    'Pergunta2': {
        'pergunta': 'Quanto é 5*5?',
        'respostas': {'a': '10', 'b': '40', 'c': '25',},
        'resposta_certa': 'c',
        },
}

print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print()
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuário = input('Sua resposta: ')
    if resposta_usuário == pv['resposta_certa']:
        print('Parabéns, você acertou essa pergunta')
        respostas_certas += 1
    else:
        print('Você errou.')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

if respostas_certas > 1:
    print(f'Você acertou {respostas_certas} respostas.')
else:
    print(f'Você acertou {respostas_certas} resposta.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')