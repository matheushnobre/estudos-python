import datetime as dt

# Métodos de classe e estáticos:
# Métodos de classe estão ligadaos à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para 
# a classe não para a instância do objeto.
# Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este 
# método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.
# Geralmente usamos o método de classe para criar métodos de fábrica.
# Geralmente usamos métodos estáticos para criar funções utilitárias.

# Exemplo
class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade
    
    @classmethod # Método de classe
    def criar_pessoa(cls, nome, ano, mes, dia):
        diaAtual, mesAtual, anoAtual = dt.date.today().day, dt.date.today().month, dt.date.today().year
        if (mesAtual > mes) or (mesAtual == mes and diaAtual >= dia):
            idade = anoAtual - ano
        else:
            idade = anoAtual - ano - 1
        return Pessoa(nome, idade)
    
    @staticmethod # Método estático
    def eh_maior_idade(idade):
        return idade >= 18
        
p = Pessoa.criar_pessoa('Matheus', 2005, 4, 12)
print(p.nome, p.idade)
print(Pessoa.eh_maior_idade(p.idade))