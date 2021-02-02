import random

frases = ['Isso mesmo, ótima escolha',
          'Muito bem, vá em frente',
          'Não acredito que você pensou nisso.',
          'Acho melhor não',
          'Sério? Tinha pensado nisso também',
          'Ok, faça isso mesmo',
          'Não, isso é uma decisão errada',
          'Espero que esteja certo disso, pois acho q não é o melhor a se fazer.',
          'Não era melhor deixar para depois?',
          'Ok, tudo certo.',
          'Tem certeza? Melhor não.',
          'Por mim tudo bem',
          ]

while True:
    escolha_do_boot = random.choice(frases)

    pergunta = input('Peça um conselho para mim. ')
    print(escolha_do_boot)
    print()
    continue
