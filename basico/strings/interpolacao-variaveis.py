nome, idade, profissao, linguagem = 'Matheus', 18, 'Programador', 'Python'

# 1º forma: % (não recomendado)
print('\nFormato %', 'Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem), sep='\n')

# 2º forma: método format
print('\nFormato método format', 'Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem), sep='\n')

# 3º forma: f strings (mais utilizada)
print('\nFormato f String', f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.', sep='\n')