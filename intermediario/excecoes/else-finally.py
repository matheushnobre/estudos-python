# Try tenta executar um bloco de código
try:
    print('Abrindo arquivo')
    print(8/0)
# Except trata exceções
except ZeroDivisionError:
    print('Ímpossível dividir por zero.')
# Else será executado caso não ocorra nenhuma exceção
else:
    print('Não ocorreu nenhum erro')
# O finally SEMPRE será executado
finally: 
    print('Fechando arquivo')