# Função que irá somar valores
'''
def soma_ate(valor):

    # Caso base: se 'valor' for igual 1 devolve 1

    if valor == 1:

        return 1
    
    # caso recursivo: n + soma dos anteriores
    return valor + soma_ate(valor - 1)


# chamando a Função - exemplos

print(soma_ate(3))
'''


# ----------------------------------------

def soma_ate(valor):

    print(f"Entrando na soma_ate({valor})")

    if valor == 1:

        print("-> base! Retornando 1")

        return 1
    
   
    resultado = valor + soma_ate(valor - 1)
    print(f"<- Retornando {valor} + .... = {resultado}")

    return resultado

# chamando a Função - exemplos

print(soma_ate(3))