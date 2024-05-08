# try tenta executar um bloco de código
try: 
    a = float(input('Insira o dividendo: '))
    b = float(input('Insira o divisor: '))
    print(round(a/b, 2)) # Realiza a divisão e arredonda para 2 casas decimais
    
# except captura uma exceção, ou seja, um erro específico
except ZeroDivisionError:
    print('Não é possível dividir por 0.')
except ValueError:
    print('Não foi possível converter o valor digitado para o tipo float.')