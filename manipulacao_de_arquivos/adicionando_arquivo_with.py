# Trabalhando com o modo:

'''
'a' -> adicionando final

    (append) adicionado conteúdo no final do arquivo

'''

# abrindo o arquivo em modo de escrita
arquivo = open("frutas.txt","a") # abrir arquivo

arquivo.write("Goiba\n")
arquivo.write("Jambo\n")
arquivo.write("Pitanga\n")


arquivo.close()  # fechando arquivo