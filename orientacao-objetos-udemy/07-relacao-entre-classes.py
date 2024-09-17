class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentasDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo.'
    
escritor = Escritor('Matheus')
caneta = FerramentasDeEscrever('Caneta Bic')
escritor.ferramenta = caneta

maquina_de_escrever = FerramentasDeEscrever('Máquina de escrever')
escritor.ferramenta = maquina_de_escrever
print(escritor.ferramenta.nome)