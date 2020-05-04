import os
#Dicionário de Extensão de Arquivo
caminho = "/Users/arthuralmeida/Downloads/"
diretorio = os.listdir(caminho)
dic_ext = {}

for item in diretorio:
    if os.path.isfile(caminho+item): #Se o item for um arquivo e não uma extensão
        arq_ext = os.path.splitext(item) #Dar um split em seu nome e extensão
        extensao = arq_ext[1] #Guardar a extensão
        if extensao not in dic_ext: #Se a extensão não estiver no dicionário de extensões
            dic_ext[extensao] = [] #Cria-la
        dic_ext[extensao].append(item) #Adicionar o item (arquivo) no nosso dicionário de sua extensão.
