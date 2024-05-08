nome = input("Digite o seu nome: ")

print("Olá, {}!".format(nome.upper()))
print("Seu nome invertido é {}.".format(nome[::-1].upper()))
    
if ' ' in nome:
     print("Seu nome contém espaço(s).")
else:
    print("Seu nome não contém nenhum espaço.")
    
print("Seu nome contém {} letras.".format(len(nome) - nome.count(' ')))
print("A primeira letra do seu nome é {}, enquanto a última letra é {}.".format(nome[0].upper(), nome[-1].upper()))
