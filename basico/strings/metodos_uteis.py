# Letras maíusculas e minúsculas
curso = 'pYtHon'
print('')
print(curso.upper()) # Converte todas as letras para maíúsculo
print(curso.lower()) # Converte todas as letras para minúsculo
print(curso.title()) # Converte todas as letras para minúscula, com exceção da 1º, que fica em maiúsculo

# Eliminando espaços em branco
curso = '    Python  '
print('')
print(curso.strip()) # Elimina espaços em branco
print(curso.lstrip()) # Elimina espaços em branco da esquerda
print(curso.rstrip()) # Elimina espaços em branco da direita

# Junções e centralização
curso = 'Python'
print('')
print(curso.center(10, '#')) # Centraliza a string e adiciona caracteres
print(curso.center(10)) # Centraliza a string sem a adição de caracteres
print(".".join(curso)) # Adiciona um caractere entre cada caractere da String