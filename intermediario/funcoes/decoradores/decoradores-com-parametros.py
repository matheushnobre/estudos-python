def gerador_decoradores(a=None, b=None, c=None):
    def gerador_funcao(func):
        def aninhada(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return aninhada
    return gerador_funcao

@gerador_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = gerador_decoradores()(lambda x, y: x * y)

print(soma(10, 5))
print(multiplica(10, 5))