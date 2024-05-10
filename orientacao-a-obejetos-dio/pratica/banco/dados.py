from datetime import datetime
from cliente import PessoaFisica, PessoaJuridica

class ListaClientes:
    def __init__(self):
        self._clientes = []
        
    @property
    def clientes(self):
        return self._clientes
    
    def adicionar(self, cliente):
        self._clientes.append(cliente)
        
    def retornar_cliente_cadastro(self, cadastro):
        for cliente in self.clientes:
            if isinstance(cliente, PessoaFisica):
                if cliente.cpf == cadastro:
                    return cliente
            else:
                if cliente.cnpj == cadastro:
                    return cliente
        return -1
    
    def listar_clientes(self):
        num_cliente = 1
        if len(self.clientes) == 0:
            return 'Não há clientes cadastrados no sistema.'
        saida = ''
        for cliente in self.clientes:
            saida += (f'{num_cliente}. {cliente}\n')
            num_cliente += 1
        return saida

class Historico:
    def transacoes(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )