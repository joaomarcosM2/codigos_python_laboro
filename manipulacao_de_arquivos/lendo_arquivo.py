# VAMOS ABRIR UM ARQUIVO

'''
'r' -> mode de leitura

'''

# abrindo um arquivo em modo leitura

arquivo = open("frutas.txt","r") # abrir arquivo


# Verificando se um arquivo pode ser lido
print(arquivo.readable())


# print(arquivo.read()) # Lendo o conteúdo de um arquivos


# Lendo apenas 1 linha do arquivo
# print(arquivo.readline())


#Lenda várias linhas
'''
resultado = arquivo.readlines()
print(resultado())
'''

resultado = arquivo.readlines()

print(resultado[3])


arquivo.close() # fechando arquivo