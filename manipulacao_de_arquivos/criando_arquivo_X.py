# Trabalhando com o modo:
'''
'x' -> Cria arquivo e exibe erro caso exista
'''
"""
arquivo = open("legumes.txt","x") # abrir arquivo


arquivo.write("Berinjela\n")

arquivo.write("Alface\n")


arquivo.close()  # fechando arquivo
"""
try:
    arquivo = open("legumes.txt","x") # abrir arquivo


    arquivo.write("Berinjela\n")

    arquivo.write("Alface\n")


    arquivo.close()  # fechando arquivo
except Exception:
    print("Não foi possivel criar o arquivo, ele já existe!")