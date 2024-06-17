caminho = 'arquivos\\arquivo.txt'

with open(caminho, 'w') as arquivo:
    arquivo.write('Estamos manipulando o arquivo.\n')
    arquivo.write('Manipulando\n')
    arquivo.writelines(('Ola\n', 'mundo\n'))
    arquivo.close()
    
with open(caminho, 'r') as arquivo:
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())