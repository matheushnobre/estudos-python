# Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto 
# (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

# Exemplo
class Estudante:
    escola = 'DIO' # Variável de classe
    
    def __init__(self, nome, matricula):
        # Variáveis de instância
        self.nome = nome 
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f'{self.nome} ({self.matricula}) - {self.escola}'
    
mat = Estudante('Matheus', '009784')
gus = Estudante('Gustavo', '120899')
print('Estudantes', mat, gus, sep='\n')

# Modificando variável de instância (única por objeto)
mat.matricula = '202363'
print('\nEstudantes', mat, gus, sep='\n')

# Modificando variável de classe (única para todos os objetos)
Estudante.escola = 'IFAM'
print('\nEstudantes', mat, gus, sep='\n')