class Pessoa:
    ano = 2023 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_bebe(cls, nome):
        return cls(nome, 0)
        
p1 = Pessoa('Matheus', 19)
Pessoa.metodo_de_classe()
p2 = Pessoa.criar_bebe('Giorgian Gabriel')
print(p2.nome, p2.idade)