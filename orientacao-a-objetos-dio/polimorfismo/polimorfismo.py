# A palavra polimorfismo significa ter muitas formas.
# Em programação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.

# Polimorfismo com herança:
# Mesmo método com comportamento diferente.
# Na herança, a classe filha herda os métodos da classe pai. No entanto, é possível modificar um método em uma classe filha herdada da 
# classe pai Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

# Exemplo
class Passaro:
    def voar(self):
        print('Voando...')
    
class Pardal(Passaro):
    def voar(self):
        return super().voar()
        
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar.')
        
def plano_de_voo(passaro):
    passaro.voar()

pardal = Pardal()
avestruz = Avestruz()
plano_de_voo(pardal)
plano_de_voo(avestruz)