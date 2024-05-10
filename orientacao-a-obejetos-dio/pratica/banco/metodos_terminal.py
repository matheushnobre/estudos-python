import os
import time

def limpar():
    os.system('cls')
    
def pausar(tempo):
    time.sleep(tempo)
    
def sair():
    print('Saindo...')
    pausar(1)
    limpar()
    exit(0)
    
def separador():
    print(30*'-')
    
def confirmar():
    input('Pressione ENTER para confirmar')