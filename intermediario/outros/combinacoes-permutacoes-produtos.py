# Combinations, Permutations e Product - Itertools
# Combinação: ordem não importa - iterável + tamanho do grupo
# Permutação: ordem importa
# Produto: ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    lista = list(iterator)
    print(*lista, sep='\n')
    print(f'Resultado = {len(lista)}')
    print()

pessoas = ['João', 'Joana', 'Luiz', 'Leticia']
camisetas = [['preta', 'branca'], ['p', 'm', 'g'], ['masculino', 'feminino', 'unissex'], ['dryfit', 'algodao']]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))