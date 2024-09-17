# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def saudar(self):
        return f'Oi, eu sou {self.nome}!'
        

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, codigo):
        super().__init__(nome, sobrenome)
        self.codigo = codigo
        
    def saudar(self):
        return super().saudar() + f' Meu código da loja é {self.codigo}'

c1 = Cliente('Matheus', 'Henrique', 1234)
print(c1.saudar())
