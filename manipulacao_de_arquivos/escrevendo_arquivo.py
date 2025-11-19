# Trabalhando com os modos:
'''
'w' -> escreve(substitui) / cria arquivo

'a' -> adicionando final
'''

arquivo = open("frutas.txt","w") # abrir arquivo

# Verificando se um arquivo pode ser escrito
#print(arquivo.writable())

arquivo.write("Maracula\n")
arquivo.write("Acerola\n")
arquivo.write("Uva\n")
arquivo.write("Manga\n")



arquivo.close()  # fechando arquivo



# Criando outro arquivo --------------

arquivo = open("verduras.txt","w") # abrir arquivo

arquivo.write("Batata\n")
arquivo.write("Cenoura\n")
arquivo.write("Maxixe\n")
arquivo.write("Quiabo\n")

# Escrevendo várias linhas
arquivo.writelines(["Macaxeira\n","Beterraba\n"])


arquivo.close()  # fechando arquivo


