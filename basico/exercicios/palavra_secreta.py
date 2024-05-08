import os

palavra_secreta = "flamengo".upper()
palavra_formatada = len(palavra_secreta) * '*'

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_inseridas = ''
erros = 0

print("Palavra secreta contém {} letras. Boa sorte!".format(len(palavra_secreta)))

while True:
    # lendo tentativa do usuário
    letra_digitada = input("Insira uma letra (o sistema não reconhece acentuação): ").upper()
    
    # verificando se o usuário realmente digitou uma letra ou se essa letra já foi digitada antes
    if len(letra_digitada) < 1:
        print("Letra não inserida.")
        continue
    elif len(letra_digitada) > 1:
        print("Você deve inserir apenas uma letra.")
        continue
    elif letra_digitada not in letras:
        print("Você deve digitar apenas letras (lembre-se que o sistema não reconhece acentuação)")
        continue
    elif letra_digitada in letras_inseridas:
        print("Você já inseriu essa letra anteriormente.")
        continue
    
    letras_inseridas += letra_digitada
    
    # verificando se a palavra secreta contém a letra digitada
    if letra_digitada in palavra_secreta:
        nova_palavra_formatada = ''
        contador = 0
        # alterandoa a palavra formatada
        for letra in palavra_secreta:
            if letra == letra_digitada:
                nova_palavra_formatada += letra
            elif palavra_formatada[contador] != '*':
                nova_palavra_formatada += palavra_formatada[contador]
            else:
                nova_palavra_formatada += '*'
            contador += 1
        palavra_formatada = nova_palavra_formatada
        os.system('cls')
        print("A letra digitada está presente na palavra digitada\nQuantidade de erros: {}\nPalavra: {}\n".format(erros, palavra_formatada))
    else:
        erros += 1
        os.system('cls')
        print("A palavra secreta não contém a letra digitada.\nQuantidade de erros: {}\nPalavra: {}\n".format(erros, palavra_formatada))
    
    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print("PARABÉNS, VOCÊ ACERTOU! A palavra secreta era {}.".format(palavra_secreta))
        break
    elif erros >= 5:
        os.system('cls')
        print("Você atingiu o limite de erros e infelizmente perdeu o jogo. A palavra secreta era {}.".format(palavra_secreta))
        break
