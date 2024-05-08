nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

str_idade = input("Digite sua idade: ")
int_idade = int(str_idade)

if int_idade >= 18:
    print("Você é maior de idade.")
    entrada = input("Digite se você deseja 'entrar' ou 'sair' do sistema: ")
    if entrada == "entrar":
        print("Logado.")
    elif entrada == "sair":
        print("Tchau!")
    else:
        print("Opção inválida. Tchau!")
else:
    print("Você é menor de idade. Tchau!")


