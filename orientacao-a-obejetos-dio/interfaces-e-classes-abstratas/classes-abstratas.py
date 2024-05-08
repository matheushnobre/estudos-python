from abc import ABC, abstractmethod, abstractproperty

# Interfaces definem o que uma classe deve fazer e não como.
# O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para crair contratos. Classes abstratas não podem ser instanciadas.

# ABC
# Por padrão, o Python não oferece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas e o nome 
# desse módulo é ABC. O ABC funciona decorando métodos da classe base como asbtratos e, em seguida, registrando classes concretas como 
# implementações da base abstrata. Um método se torna abstrato quando decorado com @abstractmethod.

# Exemplo
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        
    def desligar(self):
        print('Desligando a TV...')
        
    @property
    def marca(self):
        return 'AOC'
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o ar-condicionado...')
        
    def desligar(self):
        print('Desligando o ar-condicionado...')

    @property
    def marca(self):
        return 'LG'
    
ctv = ControleTV()
ctv.ligar()
ctv.desligar()
print(ctv.marca)

car = ControleArCondicionado()
car.ligar()
car.desligar()
print(car.marca)