frase = 'o rato roeu a roupa do rei de roma' #iterável
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

#iteração
input_usuario = input('Qual letra deseja colocar em maiuscula? ')
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_frase += input_usuario.upper()

    else:
        nova_frase += letra

    contador += 1

print(nova_frase)