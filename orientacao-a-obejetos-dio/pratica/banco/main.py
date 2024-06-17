from cliente import PessoaFisica, PessoaJuridica
from conta import ContaCorrente
from dados import ListaClientes
from metodos_terminal import limpar, pausar, sair, separador, confirmar

clientes = ListaClientes()
menu_principal = 12*'-'+' MENU '+12*'-'+'''
1. Cadastrar cliente
2. Listar clientes
3. Cadastrar conta
4. Acessar área do cliente
5. Sair
'''+30*'-'+'\nSelecione uma opção: '
    
menu_cliente = 12*'-'+' MENU '+12*'-'+'''
1. Visualizar minhas contas
2. Acessar minha conta
3. Alterar senha
4. Página inicial
5. Sair
'''+30*'-'+'\nSelecione uma opção: '
    
menu_conta = 12*'-'+' MENU '+12*'-'+'''
1. Visualizar extrato
2. Sacar
3. Depositar
4. Transferir
5. Voltar
6. Sair
'''+30*'-'+'\nSelecione uma opção: '
    
def main():  
    while True:
        limpar()
        opcao = input(menu_principal)
        limpar()
        match(opcao):
            case '1': cadastrar_cliente()
            case '2': listar_clientes()
            case '3': cadastrar_conta()
            case '4': acessar_area_cliente()
            case '5': sair()
           
def area_cliente(cliente):
    while True:
        limpar()
        print(cliente)
        opcao = input(menu_cliente)
        limpar()
        match(opcao):
            case '1': visualizar_contas(cliente)
            case '2': acessar_minha_conta(cliente)
            case '3': alterar_senha(cliente)
            case '4': break
            case '5': sair()
             
def acesso_conta(conta):
    while True:
        limpar()
        print(conta)
        opcao = input(menu_conta)
        limpar()
        match(opcao):
            case '1': visualizar_extrato(conta)
            case '2': sacar()
            case '3': depositar()
            case '4': transferir()
            case '5': break
            case '6': sair()

def cadastrar_cliente():
    while True:
        print('Cadastro de cliente')
        separador()
        print('1. Cadastro de Pessoa Física\n2. Cadastro de Pessoa Jurídica\n3. Página Inicial')
        separador()
        opcao = input('Selecione uma opção: ')
        limpar()
        match(opcao):
            case '1':
                nome = input('Insira o nome: ')
                cpf = input('Insira o cpf: ')
                nascimento = input('Insira a data de nascimento: ')
                endereco = input('Insira o endereço: ')
                cliente = PessoaFisica(nome, cpf, nascimento, endereco)
                clientes.adicionar(cliente)
                separador()
                print(f'{nome.upper()} cadastrado com sucesso!')
                pausar(1)
                break
            case '2':
                nome = input('Insira o nome: ')
                cnpj = input('Insira o cnpj: ')
                endereco = input('Insira o endereço: ')
                cliente = PessoaJuridica(nome, cnpj, endereco)
                clientes.adicionar(cliente)
                separador()
                print(f'{nome.upper()} cadastrado com sucesso!')
                pausar(1)
                break
            case '3':
                break
            case _:
                print('Insira um opção válida.')

def listar_clientes():
    global clientes
    print('Lista de clientes cadastrados no sistema:')
    separador()
    print(clientes.listar_clientes())
    confirmar()
        
def cadastrar_conta():
    while True:
        print('Cadastro de conta')
        separador()
        print('1. Criação de Conta Corrente\n2. Criação de Conta Poupança\n3. Página Inicial')
        separador()
        opcao = input('Selecione uma opção: ')
        limpar()
        match(opcao):
            case '1':
                num_cliente = input('Insira o CPF ou CNPJ do cliente: ')
                cliente = clientes.retornar_cliente_cadastro(num_cliente)
                if cliente == -1:
                    limpar()
                    print('Cliente não existe em nossa base de dados. Por favor, cadastre-o: ')
                    cadastrar_cliente()
                    break
                limite_padrao = input("Cliente irá utilizar condições padrões de limite? Digite 'S' em caso afirmativo. Qualquer outra tecla caso deseje configurar os limites. ").upper()
                if limite_padrao == 'S':
                    conta = ContaCorrente(cliente)
                    limpar()
                    print('Conta criada com sucesso!')
                    print('Informações', conta, sep='\n')
                    confirmar()
                else:
                    while True:
                        limite = input('Insira o limite diário de saque: R$')
                        try:
                            limite = float(limite)
                            break
                        except ValueError:
                            limpar()
                            print('Valor inválido.')
                    
                    while True:
                        limite_saques = input('Insira o limite diário de quantidade de saques: ')
                        try:
                            limite_saques = int(limite_saques)
                            break
                        except ValueError:
                            limpar()
                            print('Valor inválido.')                        
                    
                    conta = ContaCorrente(cliente, limite, limite_saques)
                    limpar()
                    print('Conta criada com sucesso!')
                    print('Informações', conta, sep='\n')
                    confirmar()
                break     
                
            case '2':
                limpar()
                print('Funcionalidade ainda não adicionada ao sistema. Volte em breve!')
                confirmar()
                break
            case '3':
                break
            case _:
                separador()
                print('Insira um opção válida.')
                
def acessar_area_cliente():
    num_cliente = input('Insira o CPF ou CNPJ do cliente: ')
    cliente = clientes.retornar_cliente_cadastro(num_cliente)
    if cliente == -1:
        limpar()
        print('Cliente não existe em nossa base de dados. Por favor, cadastre-o: ')
        cadastrar_cliente()
    else:
        senha = input(f'Olá, {cliente.nome}! Digite sua senha: ')
        if senha == cliente.senha:
            print('Acessando conta...')
            pausar(1)
            area_cliente(cliente)
        else:
            limpar()
            print('Senha incorreta!')
            acessar_area_cliente()
  
def visualizar_contas(cliente):
    contas = cliente.contas
    print(f'Cliente: {cliente}')
    separador()
    if len(contas) == 0:
        print('Você não possui nenhuma conta cadastrada!')
    for conta in contas:
        print(conta)
        separador()
    confirmar()
    
def acessar_minha_conta(cliente):
    contas = cliente.contas
    if len(contas) == 0:
        print('Você não possui nenhuma conta cadastrada!')
        confirmar()
    else:
        print('Suas contas: ')
        separador()
        for conta in contas:
            print(conta)
            separador()
        numero_conta = input('Insira o número da conta que deseja acessar: ')
        try:
            numero_conta = int(numero_conta)
        except ValueError:
            limpar()
            print('Digite um valor válido.')
            acessar_minha_conta(cliente)
        conta_acessada = None
        for conta in contas:
            if conta.numero == numero_conta:
                conta_acessada = conta
        if conta_acessada == None:
            limpar()
            print('Você não possui essa conta.')
            acessar_minha_conta(cliente)
        else:
            acesso_conta(conta)
    
def alterar_senha(cliente):
    nova_senha = input('Insira sua nova senha: ')
    cliente.senha = nova_senha
    print('Senha alterada com sucesso!')
    pausar(1)
      
def visualizar_extrato(conta):
    pass

def sacar(conta):
    pass

def depositar(conta):
    pass

def transferir(conta):
    print('Funcionalidade ainda não adicionada ao sistema. Por favor, volte em breve.')
          
main()