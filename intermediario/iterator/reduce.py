# Faz a redução de um iterável em um valor real
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# SEM reduce
total = 0
for p in produtos:
    total += p['preco']
print(round(total, 2))

# COM reduce:
def funcao_do_reduce(total, produto):
    return total + produto['preco']
    
total = reduce(funcao_do_reduce, produtos, 0)
print(round(total, 2))

# Também posso utilizar lambda
total = reduce(lambda t, p : t + p['preco'], produtos, 0)
print(round(total, 2))