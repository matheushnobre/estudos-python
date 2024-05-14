# Variáveis livres + nonlocal

def concatenar(string_inicial):
    valor_final = string_inicial
    def concatenar_ao_valor(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return concatenar_ao_valor

c = concatenar('a')
print(c('b'))
print(c('c'))
final = c()
print(final)