from itertools import zip_longest

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

soma = [sum(l) for l in list(zip(l1, l2))]
print(soma)

# Solução mais adequada
soma = [x + y for x, y in zip(l1, l2)]
print(soma)

# Caso queira usar os valores de todas as listas:
soma = [x + y for x, y in zip_longest(l1, l2, fillvalue=0)]
print(soma)