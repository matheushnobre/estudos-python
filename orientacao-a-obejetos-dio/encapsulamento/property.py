import datetime as dt

# Property
# Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos 
# como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe

# Exemplo 1
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property  # Pega um método e transforma-o em uma propriedade    
    def x(self):
        return self._x or 0
    
    @x.setter # Cria um modificador
    def x(self, value):
        self._x += value
        
    @x.deleter # Deletar 
    def x(self):
        self._x = -1
 
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

# Exemplo 2
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return dt.date.today().year - self._ano_nascimento
    
pessoa = Pessoa('Matheus', 2005)
print(f'Nome: {pessoa.nome}\nIdade: {pessoa.idade}')