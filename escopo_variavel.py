valor = 50

'''
def mensagem():
    print(f"Exibindo a váriavel valor: {valor}")


# chamando a Função
mensagem()
'''


def mensagem():

    global valor # Declara que estamos usando a variável que esta fora da função (global)

    print(f"Exibindo a váriavel valor: {valor}")

    valor = valor + 10

    print(f"Valor da váriavel atualizada: {valor}")

# chamando a Função
mensagem()