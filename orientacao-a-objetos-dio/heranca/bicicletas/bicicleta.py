class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print(f'{self.modelo} buzinando...')
    
    def parar(self):
        print('Parando bicicleta')
        
    def correr(self):
        print('Bicicleta correndo...')
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
        
b1 = Bicicleta('Vermelho', 'Caloi', 2024, '750.00')
print(b1)
b1.buzinar()
Bicicleta.buzinar(b1)