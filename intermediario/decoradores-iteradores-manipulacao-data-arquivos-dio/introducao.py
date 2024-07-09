# Passagem de funções
def mensagem(nome):
    print('executando mensagem')
    return f'Oi, {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá! Tudo bem com você, {nome}?'

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)

# print(executar(mensagem, 'Matheus'))
# print(executar(mensagem_longa, 'Matheus'))

# Inner Function
def principal():
    print('executando a função principal')
    
    def funcao_interna():
        print('executando a função interna')
        
    def funcao_interna_2():
        print('executando a 2º função interna')
        
    funcao_interna()
    funcao_interna_2()
    
# principal()

# Retornando função
def calculadora(operacao):
    def soma(a, b):
        return a+b
    
    def subtracao(a, b):
        return a-b
    
    def multiplicacao(a, b):
        return a*b
    
    def divisao(a, b):
        return a/b
    
    match operacao:
        case '+': return soma
        case '-': return subtracao
        case '*': return multiplicacao
        case '/': return divisao
        case _: raise TypeError
        
# print(calculadora('+')(6, 3))
# print(calculadora('-')(6, 3))
# print(calculadora('*')(6, 3))
# print(calculadora('/')(6, 3))