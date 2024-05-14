# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    return [(lista1[i], lista2[i]) for i in range(min(len(l1), len(l2)))]
    
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))

# Ou... função pronta do Python
print(zip(l1, l2)) # Retorna um iterator
print(list(zip(l1, l2)))

from itertools import zip_longest
print(list(zip_longest(l1, l2, fillvalue='NULO')))