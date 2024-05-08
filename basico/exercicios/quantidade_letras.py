caracteres_permitidos = "abcdefghijklmnopqrstuvwxyz"
letra_mais_repetida = ''
qtd_aparece = 0

frase = input("Digite uma frase (por favor, não utilize acentuação): ").lower()

for letra_atual in frase:
    letra_atual.lower()
    
    if letra_atual not in caracteres_permitidos:
        continue
        
    apareceu = frase.count(letra_atual)
    
    if apareceu > qtd_aparece:
        letra_mais_repetida = letra_atual
        qtd_aparece = apareceu
    
print("A letra mais frequente foi '{}', aparecendo um total de {} vezes".format(letra_mais_repetida, qtd_aparece))