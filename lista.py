# criando uma lista

numeros = [3, 5, 8, 10, 14]

#print(type(lista))

print(numeros)

numeros[2] = 15  # alterando o valor do indice 2 


# Exibir todos os numeros 

for item in numeros:
    print(item)


# Inserindo valores na lista

numeros.append(23)

print(numeros)


#Adicionando item em qualquer lugar

numeros.insert(2,90) # iremos inserir o valor 90 no indice 2

print(numeros)


#removendo item da lista

numeros.pop()  #removendo item do final da lista
print(numeros)


numeros.pop(4)  #removendo item da lista
print(numeros)


 