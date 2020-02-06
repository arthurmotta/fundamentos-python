# Faça uma função em Python que receba do usuário a idade de uma pessoa em anos,
# meses, e dias e retorne essa idade expressa em dias. Considere que todos os anos tem 365 dias.

anos = int(input("Informe o valor de anos: "))
meses = int(input("Informe o valor de meses: "))
dias = int(input("Informe o valor de dias: "))

# Convertendo os anos para dias:

dias += anos * 365
dias += meses * 30
print(dias)

################################################################################################################################################################################

#Só pelo número de dias

dias = int(input("Digite o número de dias"))

anos = dias // 365
dias = dias % 365
meses = dias // 30
if meses >= 12:
    anos +=1
    meses -= 12
dias = dias % 30

print(f"{anos} anos, {meses} meses, e {dias} dias")