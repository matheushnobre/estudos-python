from cliente import PessoaFisica, PessoaJuridica
from dados import ListaClientes

clientes = ListaClientes()

c1 = PessoaFisica('Matheus', '07198937209', '12/04/2005', 'Rua Maues')
c2 = PessoaJuridica('Garantido', '123', 'curral lindolfo')
clientes.adicionar(c1)
clientes.adicionar(c2)

cc = clientes.retornar_cliente_cadastro('07198937209')
print(cc)

cc = clientes.retornar_cliente_cadastro('123')
print(cc)

cc = clientes.retornar_cliente_cadastro('000')
print(cc)