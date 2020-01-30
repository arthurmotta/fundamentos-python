import random

def ler_cpf(tamanho):
    cpf = input(f"Informe os {tamanho} digitos do CPF: ")
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')

    if(len(cpf) != tamanho):
        print(f"Tamanho da entrada errado. Utilize {tamanho} dígitos.")
        return ler_cpf(tamanho)                      #Usando recursividade (Chamando uma função dentro dela mesma) O return é usada para voltar ao valor original
    else:
        return list(cpf)
#Fim da definição da função ler_cpf()

def digito_verificador(cpf, digito):                     #Verifica os dois ultimos numeros
    soma = 0
    termo_peso = 10

    if(digito == 1):
        termo_peso = 10
    elif(digito == 2):
        termo_peso == 11

    for i in range(len(cpf)):
        soma += int(cpf[i]) * (termo_peso - i)

    modulo11 = soma % 11

    if(modulo11 < 2):
        return str(0)
    else:
        return str(11 - modulo11)

#Funcoes que ficaram em desuso

#def primeiro_verificador(cpf):                     #Verifica o primeiro dos dois ultimos numeros
#    soma = 0                                          
#    for i in range(len(cpf)):
#        soma += int(cpf[i]) * (10 - i)
#
#    modulo11 = soma % 11
#
#    if(modulo11 < 2):
#        return str(0)
#    else:
#        return str(11 - modulo11)
#
#def segundo_verificador(cpf):                         #Verifica o segundo dos dois ultimos numeros
#    soma = 0                                          
#    for i in range(len(cpf)):
#        soma += int(cpf[i]) * (11 - i)
#
#    modulo11 = soma % 11
#
#    if(modulo11 < 2):
#        return str(0)
#    else:
#        return str(11 - modulo11)

def formatar_cpf(cpf):
    cpf.insert(3, '.')
    cpf.insert(7, '.')
    cpf.insert(11, '-')
    cpf_formatado = ' '
    for numero in cpf:
        cpf_formatado = cpf_formatado + numero
    return cpf_formatado

def gerar_cpf():
    cpf = []
    for i in range(9):
        numero = random.randint(0,9)
        cpf.append(str(numero))

    cpf.append(digito_verificador(cpf, 1))
    cpf.append(digito_verificador(cpf, 2))
    print(formatar_cpf(cpf))

def validar_cpf():
    cpf = ler_cpf(11)
    cpf_validacao = cpf[:9]

    cpf_validacao.append(digito_verificador(cpf_validacao, 1))
    cpf_validacao.append(digito_verificador(cpf_validacao, 2))

    if cpf_validacao == cpf:
        print("CPF válido.")
    else:
        print("CPF inválido!")

gerar_cpf()


