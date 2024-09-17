# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Matheus', 'Henrique')
# p1.nome = 'Matheus'
# p1.sobrenome = 'Henrique'

p2 = Pessoa('Carlos', 'Alcaraz')
# p2.nome = 'Carlos'
# p2.sobrenome = 'Alcaraz'

print(p1.nome, p1.sobrenome, sep=' ')
print(p2.nome, p2.sobrenome, sep=' ')

print(p1.__dict__)
