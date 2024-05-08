print(10*'-', "Calculadora de IMC", 10*'-', "\nEntre com seus dados")

nome = input("Nome: ")
altura_digitada = input("Altura: ")
peso_digitado = input("Peso: ")

try:
    altura = float(altura_digitada)
    peso = float(peso_digitado)
except:
    print("Algum valor não foi preenchido corretamente. Execute novamente o programa.")
    exit()
    
imc = peso / altura**2
classificacao = ""
if imc < 18.5:
    classificacao = "ABAIXO DO PESO"
elif imc < 24.9:
    classificacao = "PESO IDEAL (parabéns!)"
elif imc < 29.9:
    classificacao = "LEVEMENTE ACIMA DO PESO"
elif imc < 34.9:
    classificacao = "OBESIDADE GRAU 1"
elif imc < 39.9:
    classificacao = "OBESIDADE GRAU 2 (severa)"
else:
    classificacao = "OBESIDADE GRAU 3 (mórbida)"

resultado = "Ok, {}, seu IMC é {:.2f}, o que indica que você está enquadrado na seguinte faixa: {}.".format(nome, imc, classificacao)
print(resultado)