valores = []  # criando uma lista vazia

for item in range(10,14):
    valores.append(item)

print(valores)


# Preenchendo uma lista com dados dinamicos

valores2 = []  # Outra variavel  

while True:
    numero = int(input("Informe um valor numerico qualquer - zero para encerrar: "))

    if numero == 0:
        break  # encerra o sistema
    else:
        valores2.append(numero)


print("\nPrograma encerrado\n")

print(valores2)


# EXECICIO

while True:
    numero = int(input("Vc quer apagar um item da lista? \n1 - sim \n2 - para encerrar\n\nDigite uma opção: "))

    if   numero == 2:
        break  # encerra o sistema
    elif numero == 1:
        valores2.pop()
    
    print(valores2)


print("\nPrograma encerrado\n")

print(valores2)

