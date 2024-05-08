generator = (n for n in range(10))
for n in generator:
    print(n, end=' ')

# Generator ocupa menos espaço na memória
# Entretanto, não é possível acessar um índice específico
# Também não será possível verificar seu tamanho
# Ele é similar ao iterator, foi criado para navegar sequencialmente
# É uma função que pausa