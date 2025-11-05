# Função | modo 1 - sem parâmetro e sem retorno

def menu():
    print("\n\n--- MENU DO SISTEMA ---")
    print("1 - Consutar ")
    print("2 - Inserir ")
    print("3 - Excluir \n")


#Chamando a função
menu()


# Função | modo 2 - com parâmetro e sem retorno

def somar(num1, num2):

    print(f"A soma é {num1 + num2}")

#chamando 
somar(4, 5)


# Função | modo 3 - sem parâmetro e com retorno

def dobro():
     
     valor = int(input("informa um valor numero: "))

     return valor * 2

#Chamando a função

''' print(dobro())

    print(f"O dobor é {dobro()}")  '''

print(f"O dobro é {dobro()}")


# Função | modo 4 - com parâmetro e com retorno
'''
def triplo(valor):
    return valor * 3 '''

def triplo(valor):

    resposta = valor * 3

    return resposta 

print(f"\nO triplo do valor é {triplo(8)}\n")


#Chamando a função com um valor dinâmico

numero = int(input("Informe um valor: "))

print(f"O triplo do valor é {triplo(numero)}")
