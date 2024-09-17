# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
CAMINHO_ARQUIVO = 'classePessoa.json'

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
# p1 = Pessoa('Matheus', 19)
# p2 = Pessoa('Marle', 23)
# p3 = Pessoa('Gabigol', 28)

# pessoas = [p1, p2, p3]
# bd = [p.__dict__ for p in pessoas]

# with open(CAMINHO_ARQUIVO, 'w') as arquivo:
#     json.dump(bd, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    
    print(p1.__dict__, p2.__dict__, p3.__dict__, sep='\n')