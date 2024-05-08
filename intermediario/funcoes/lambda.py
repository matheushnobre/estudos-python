nomes = [
    {'nome': 'Matheus', 'sobrenome': 'Nobre'},
    {'nome': 'Gustavo', 'sobrenome': 'Santos'},
    {'nome': 'Léo', 'sobrenome': 'Mendonça'},
    {'nome': 'Yasmin', 'sobrenome': 'Santos'}
]

nomes.sort(key = lambda nome : nome['nome'])

for nome in nomes:
    print(nome)