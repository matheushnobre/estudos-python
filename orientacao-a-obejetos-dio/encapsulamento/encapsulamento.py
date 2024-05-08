# O encapusulamento descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao 
# acesso direto a variáveis e métdos e pode evitar a modificação acidental de dados. Para evitar alterações acidentes, a variável de um 
# objeto só pode ser alterada pelo método desse objeto.

# Recursos públicos e privados
# Em Python não temos palavras reservadas, porém usamos convenções no nome do recurso para definir se a variável é pública ou privada.
# Público: pode ser acessado de fora da classe
# Privado: Só pode ser acessado pela classe (por convenção, inicia-se com _).

# Exemplo
class Conta:
    def __init__(self, numAgencia, saldo=0):
        # Saldo é um atributo privado
        self._saldo = saldo
        # Numero agência é público
        self.numAgencia = numAgencia
    
    def depositar(self, valor):
        pass
        
    def sacar(self, valor):
        pass
    
    def getSaldo(self):
        pass
    