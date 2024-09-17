class Aluno:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade
        self._notas = {}
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
        
    def adicionar_nota(self, materia, nota):
        self._notas[materia] = nota
        
    def retornar_notas(self):
        infos = f'Aluno: {self._nome}'
        for materia, nota in self._notas.items():
            infos += f'\n{materia} - {nota}'
        infos += f'\nMédia: {self.calcular_media()}'
        return infos
    
    def calcular_media(self):
        return round(sum(self._notas.values()) / len(self._notas), 2)
    
class Professor:
    def __init__(self, nome, materia) -> None:
        self._nome = nome
        self._materia = materia
        self._alunos = []
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def materia(self):
        return self._materia
    
    @materia.setter
    def materia(self, materia):
        self._materia = materia
        
    def atribuir_nota(self, aluno, nota):
        aluno.adicionar_nota(self._materia, nota)
        
class Turma:
    def __init__(self, nome, professor) -> None:
        self._nome = nome
        self._professor = professor
        self._alunos = []
        
    def cadastrar_aluno(self, aluno):
        self._alunos.append(aluno)
        
    def calcular_media_turma(self):
        soma = 0
        for aluno in self._alunos:
            soma += aluno.calcular_media()
        try:
            return soma / len(self._alunos)
        except ZeroDivisionError:
            return 0

p = Professor('Alberi', 'Matemática')
a1 = Aluno('Matheus', 17)
a2 = Aluno('Gustavo', 16)
a3 = Aluno('Luís Eduardo', 16)
turma = Turma('9º ano', p)
for aluno in [a1, a2, a3]:
    turma.cadastrar_aluno(aluno)
p.atribuir_nota(a1, 9)
p.atribuir_nota(a2, 10)
p.atribuir_nota(a3, 8)
print(turma.calcular_media_turma())