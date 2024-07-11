class Veiculo:
    def __init__(self, cor, placa, nrodas):
        self.cor = cor
        self.placa = placa
        self.nrodas = nrodas
        
    def ligar_motor(self):
        print('Ligando o motor...')
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class Motocicleta(Veiculo):
    def __init__(self, cor, placa, nrodas=2):
        super().__init__(cor, placa, nrodas)

class Carro(Veiculo):
    def __init__(self, cor, placa, nrodas=4):
        super().__init__(cor, placa, nrodas)

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nrodas=8, carregado=False):
        super().__init__(cor, placa, nrodas)
        self.carregado = carregado
        
    def carregar(self):
        print('Carregando caminhão...')
        self.carregado = True
        
    def descarregar(self):
        print('Descarregando caminhão...')
        self.carregado = False
        
    def esta_carregado(self):
        print('Está carregado') if self.carregado else print('Não está carregado')
        

moto = Motocicleta('vermelho', 'ABC1234')
carro = Carro('preto', 'MAT2024')
caminhao = Caminhao('azul', 'FRA2015')

print(moto)
print(carro)
print(caminhao)

caminhao.ligar_motor()
caminhao.esta_carregado()
caminhao.carregar()
caminhao.esta_carregado()
caminhao.descarregar()
caminhao.esta_carregado()