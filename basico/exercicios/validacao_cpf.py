def realizar_operacao_verificacao(cpf_reduzido, valor_multiplicado):
    operacao_verificacao = 0
    for digito in cpf_reduzido:
        operacao_verificacao += valor_multiplicado * int(digito)
        valor_multiplicado -= 1
    
    operacao_verificacao *= 10
    operacao_verificacao %= 11
    
    digito = operacao_verificacao if operacao_verificacao <= 9 else 0
    return digito

def verificar_primeiro_digito(cpf):
    digito = realizar_operacao_verificacao(cpf_reduzido=cpf[:9], valor_multiplicado=10)
    return True if cpf[9] == str(digito) else False

def verificar_segundo_digito(cpf):
    digito = realizar_operacao_verificacao(cpf_reduzido=cpf[:10], valor_multiplicado=11)
    return True if cpf[10] == str(digito) else False

# Pegando o cpf do usuário e formatando-o, caso necessário
cpf_completo = input("Digite seu cpf: ").replace('.', '').replace('-', '')

if len(cpf_completo) != 11 or not cpf_completo.isdecimal():
    print("{} é um CPF inválido pois não possui 11 caracteres ou algum campo inválido foi digitado.".format(cpf_completo))
elif verificar_primeiro_digito(cpf_completo) and verificar_segundo_digito(cpf_completo):
    print("{} é um CPF válido.".format(cpf_completo))
else:
    print("{} é um CPF inválido.".format(cpf_completo))