from dados import Historico
from transacoes import Saque

class Conta:
    prox_numero = 0
    def __init__(self, cliente):
        self._saldo = 0
        self._numero = Conta.gerar_numero()
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
        cliente.contas.append(self)
        
    @classmethod    
    def gerar_numero(cls):
        cls.prox_numero += 1
        return cls.prox_numero
    
    @classmethod
    def nova_conta(cls, cliente):
        return cls(cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
         return self._cliente
     
    @property 
    def historico(self):
         return self._historico
     
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('\nOperação falhou! Você não tem saldo suficiente.')
        
        elif valor > 0:
            self.saldo -= valor
            print('\nSaque realizado com sucesso!')
            
        else:
            print('\nOperação falhou! O valor informado é inválido.')

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('\nDepósito realizado com sucesso!')
        
        else:
            print('\nOperação falhou! O valor informado é inválido.')
            return False

        return True
    
    def __str__(self):
        return f'Agência: {self.agencia}\nNúmero: {self.numero}\nTitular: {self.cliente.nome}'
                
class ContaCorrente(Conta):
    def __init__(self, cliente, limite=500, limite_saques=3):
        super().__init__(cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        
        excedeu_limite = valor > self._limite 
        excedeu_saques = numero_saques > self._limite_saques
        
        if excedeu_saques:
            print('\nOperação falhou! Número máximo de saques excedido.')
        
        elif excedeu_limite:
            print('\nOperação falhou! Número máximo de saques excedido.')
       
        else:
            return super().sacar(valor)   
        
        return False