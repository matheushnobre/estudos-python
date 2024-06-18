tarefas = []
tarefas_desfazer = []

def listar(tarefas):
    if not tarefas:
        print('Não há nenhuma tarefa na lista de tarefas\n')
        return
    
    print('LISTA DE TAREFAS')
    print(*tarefas, sep='\n')
    print()
    
def desfazer(tarefas, tarefas_desfazer):
    if not tarefas:
        print('Não há nenhuma tarefa na lista de tarefas\n')
        return

    tarefas_desfazer.append(tarefas.pop())
    print('Desfeito\n')

def refazer(tarefas, tarefas_desfazer):
    if not tarefas_desfazer:
        print('Não há nenhuma tarefa na área de transferências\n')
        return

    tarefas.append(tarefas_desfazer.pop())
    print('Refeito\n')
    
def adicionar(tarefa, tarefas, tarefas_desfazer):
    tarefas.append(tarefa)
    tarefas_desfazer.clear()
    print('Tarefa adicionada\n')

while True:
    print("Comandos: listar, desfazer, refazer, sair")
    opcao = input('Digite uma tarefa ou comando: ')
    
    if opcao == 'listar':
        listar(tarefas)
        
    elif opcao == 'desfazer':
        desfazer(tarefas, tarefas_desfazer)
            
    elif opcao == 'refazer':
        refazer(tarefas, tarefas_desfazer)
        
    elif opcao == 'sair':
        exit()
        
    else:
        adicionar(opcao, tarefas, tarefas_desfazer)