def calculadora():
    nota1 = float(input('Digite sua nota de linguagens: '))
    nota2 = float(input('Digite sua nota de naturezas: '))
    nota3 = float(input('Digite sua nota de matemática: '))
    nota4 = float(input('Digite sua nota de humanas: '))
    nota5 = float(input('Digite sua nota de redação: '))

    pesoCN = int(input('Digite o peso de natureza: '))
    pesol = int(input('Digite o peso de linguagens: '))
    pesom = int(input('Digite o peso de matemática: '))
    pesoh = int(input('Digite o peso de humanas: '))
    pesor = int(input('Digite o peso de redação: '))

    total_pesos = pesoCN + pesor + pesoh + pesom + pesol

    media = ((nota1 * pesol) + (nota2 * pesoCN) + (nota3 * pesom) + (nota4 * pesoh) + (nota5 * pesor)) / total_pesos

    bonificacao = float(input('digite a bonificação: '))

    if bonificacao > 0.01:
        media_bonificacao = media + (media*bonificacao)
        print(media_bonificacao)

    else:
        print(media)


calculadora()
