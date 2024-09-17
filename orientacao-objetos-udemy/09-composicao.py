class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    def listar_enderecos(self):
        for e in self.enderecos:
            print(e.rua, e.numero)
    
class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero
        
cliente = Cliente('Matheus')
cliente.inserir_endereco('Rua Miami', 8643)
cliente.inserir_endereco('Rua Cisco Ramon', 392)
cliente.listar_enderecos()