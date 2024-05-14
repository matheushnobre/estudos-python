# Funções decoradoras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradorras em outras funções
# Decoradores são Syntax Sugar (açúcar sintático)

def decora(funcao):
    def interna(*args):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args)
        return resultado
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parâmetro deve ser uma String')
    
@decora
def inverte_string(string):
    return string[::-1]

@decora
def concatenando(*strings):
    return ' '.join(strings)

invertida = inverte_string('Matheus')
concatenada = concatenando('Matheus', 'Henrique', 'Vieira', 'Ramos', 'Nobre')
print(invertida, concatenada, sep='\n')

# A linha abaixo lançaria a exceção
# concatenada = concatenando('Matheus', 2, 'Henrique', 'Vieira', 'Ramos', 'Nobre')