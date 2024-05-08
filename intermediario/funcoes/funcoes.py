# Estrutura de uma função =
# def nome_funcao(parametro):
def saudacao(nome):
    return 'Hello, {}!'.format(nome)

# chamando a função com argumento posicional
print(saudacao("Matheus"))

# chamando a função com argumento nomeado
print(saudacao(nome="Léo"))

# ---------------------------------------------------------------------------------------------------------

# funções com quantidade ilimitada de argumentos não nomeados 
def somar(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(somar(5, 2))

# lembrando que a função de soma já está pronta no python
print(sum((2, 3, 4)))