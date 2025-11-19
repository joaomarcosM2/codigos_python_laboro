# Contagem com recursividade
'''
def contagem(numero):

    if numero <= 10:

        print(numero)

        numero = numero + 1

        contagem(numero)


# chamando a Função
contagem(1)
'''

# DE 10 à 1.

def contagem(numero):

    if numero >= 1:

        print(numero)

        numero = numero - 1

        contagem(numero)


contagem(10)