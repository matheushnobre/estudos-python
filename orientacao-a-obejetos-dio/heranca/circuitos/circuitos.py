class LogicGate:
    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Digite a entrada do Pino A para a porta "+self.getName()+": "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Digite a entrada do Pino B para a porta "+self.getName()+": "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Erro: NÃO HÁ PINO LIVRE")

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a==1 and b==1 else 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a ==1 or b==1 else 0

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Digite a entrada do Pino para a porta "+self.getName()+": "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Erro: NÃO HÁ PINO LIVRE")

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        return 0 if self.getPin() else 1
    
class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):
        g1 = AndGate(self.name)
        g2 = NotGate(self.name)
        c = Connector(g1, g2)
        return g2.getOutput()
    
class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):
        g1 = OrGate(self.name)
        g2 = NotGate(self.name)
        c = Connector(g1, g2)
        return g2.getOutput()
    
class XorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a!=b else 0

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def main():
    g1 = AndGate('G1')
    g2 = OrGate('G2')
    c1 = Connector(g1, g2)
    print(g2.getOutput())
        
main()