# EXECICIO 

def resultado(valor):

    if valor % 2 == 0: 
        return "Par"
    else:
        return "Impar"
    
valor = int(input("\nDigite um valor: "))

print(f"\nO número da variavel valor é {resultado(valor)}\n\n")


# PROFESSOR 
print("-" * 50)

def verificarParimpar():
    resposta = int(input("\nInforme um valor: "))

    if resposta % 2 == 0: 
        return "Par"
    else:
        return "Impar"
    
print(f"\nO valor digitado é {verificarParimpar()}")