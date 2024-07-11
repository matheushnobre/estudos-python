from mdc import mdc

class Fraction:
    # Construtor da classe
    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise ValueError('Valores incompatíveis')
        comum = mdc(num, den)
        self.num = num//comum
        self.den = den//comum
        
    # Métodos get
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
        
    # Retorna o objeto em formato de string
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    
    # Método para somar frações
    def __add__(self, f):
        novonum = self.num * f.den + self.den * f.num
        novoden = self.den * f.den
        return Fraction(novonum, novoden)

    # Método para subtrair frações    
    def __sub__(self, f):
        novonum = self.num * f.den - self.den * f.num
        novoden = self.den * f.den
        return Fraction(novonum, novoden)
    
    # Método para multiplicar frações
    def __mul__(self, f):
        novonum = self.num * f.num
        novoden = self.den * f.den
        return Fraction(novonum, novoden)
    
    # Método para dividir frações
    def __truediv__(self, f):
        novonum = self.num * f.den
        novoden = self.den * f.num
        return Fraction(novonum, novoden)
    
    # Método para verificar se duas frações são iguais
    def __eq__(self, f):
        return self.num * f.den == self.den * f.num
        
    # Método para verificar se duas frações são diferentes
    def __ne__(self, f):
        return self.num * f.den != self.den * f.num
    
    # Método para verificar se a fração a é maior que a fração b
    def __gt__(self, f):
        return self.num * f.den > self.den * f.num
    
    # Método para verificar se a fração a é maior ou igual a b
    def __ge__(self, f):
        return self.num * f.den >= self.den * f.num
    
    # Método para verificar se a fração a é menor que b
    def __lt__(self, f):
        return self.num * f.den < self.den * f.num
    
    # Método para verificar se a fração a é menor ou igual a b
    def __le__(self, f):
        return self.num * f.den <= self.den * f.num