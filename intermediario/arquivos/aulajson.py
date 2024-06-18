import json

pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Nobre',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.84,
    'numeros_preferidos': (12, 28, 10),
    'dev': True,
    'nada': None,
}

with open('.\\intermediario\\arquivos\\json.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('.\\intermediario\\arquivos\\json.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
