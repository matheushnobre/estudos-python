# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

# PARTIAL
aumentar_dez_por_cento = partial(aumentar_porcentagem, porcentagem=1.1)

def muda_preco(produto):
    return {**produto, 'preco': aumentar_dez_por_cento(produto['preco'])} 

# MAP
novos_produtos = list(map(muda_preco, produtos))
print_iter(novos_produtos)

# MAP com Lambda
print(
    list(map(lambda x : x * 3, [1, 2, 3, 4]))
)

# FILTER
novos_produtos = filter(
    lambda p : p['preco'] > 10, produtos
)
print_iter(novos_produtos)