lista_compras = []

while True:
    opcao = input("\n1.Inserir 2.Apagar 3.Listar 4.Sair\nSelecione uma opção: ")

    if opcao == '1':
        produto = input("Insira o produto: ")
        lista_compras.append(produto)
        print("Produto adicionado com sucesso.")
        
    elif opcao == '2':
        indice_str = input("Insira o índice do produto: ")
        try:
            indice = int(indice_str)
            del lista_compras[indice]
            print("Produto removido com sucesso.")
        except ValueError:
            print("Por favor, digite um valor inteiro")
        except IndexError:
            print("Índice não existe")
        except Exception:
            print("Erro desconhecido.")
        
    elif opcao == '3':
        if len(lista_compras) == 0:
            print("Nada para listar")
        for i, item in enumerate(lista_compras):
            print(i, item)
            
    elif opcao == '4':
        break
    
    else:
        print("Opção inválida.")