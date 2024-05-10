class Cliente():
    def __init__(self, nome, endereco):
        self._endereco = endereco
        self._nome = nome
        self._senha = '1234'
        self._contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    @property    
    def nome(self):
        return self._nome
    
    @property    
    def endereco(self):
        return self._endereco
    
    @property    
    def contas(self):
        return self._contas
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter  
    def senha(self, nova_senha):
        self._senha = nova_senha
    
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, endereco)
        self._data_nascimento = data_nascimento
        self._cpf = cpf
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
        
    @property    
    def cpf(self):
        return self._cpf
    
    def __str__(self):
        return f'Nome: {self.nome}, cpf: {self.cpf}, nascimento: {self.data_nascimento}, endereço: {self.endereco}'
    
class PessoaJuridica(Cliente):
    def __init__(self, nome, cnpj, endereco):
        super().__init__(nome, endereco)
        self._cnpj = cnpj
    
    @property    
    def cnpj(self):
        return self._cnpj
    
    def __str__(self):
        return f'Nome: {self.nome}, cnpj: {self.cnpj}, endereço: {self.endereco}'
