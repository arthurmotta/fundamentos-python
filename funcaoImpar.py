#Escreva uma função em Python que some todos os números ímpares de 1 até um dado N.
# O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado dessa soma.

# 1. Determinar o valor de N
# 2. Percorrer todo o intervalo, considerando que números são ímpares.
# 3. Se o número for ímpar, adicioná-lo a uma soma parcial
# 4. Uma vez percorrido o intervalo, informe o valor da soma.

n = int(input("Informe o valor de N: "))
soma = 0
for x in range(1, n+1):
    #Nessa versão estamos considerando todos os números
    if(x % 2 != 0):
        soma = soma + x

print(soma)

##################################################################################################################################################################

n = int(input("Informe o valor de N: "))
soma = 0
for x in range(1, n+1, 2):
    #Nessa versão, só estamos considerando os números ímpares, graças ao terceiro parâmetro da função range()
    soma += x

print(soma)

#################################################################################################################################################################

n = int(input("Informe o valor de N: "))
soma = 0
x = 0

while x <= 90:
    if x % 2 != 0:
        soma +=x
    x += 1

print(soma)

#################################################################################################################################################################

#Usando a fórmula de Pascal | Sn = n(a1 + an) / 2

valor = int(input("Informe o valor de N: "))

termos = (1 + valor) / 2
termos = round(termos) #Arredondando 

print(termos)
