
'''
# É um bloco de tratamento de erros 
try:

    valor = int(input("Informe um valor numérico: "))

    print(f"\nO numero digitado foi {valor}")

except ValueError:
    print("Coisa feia, tentando colocar texto no locar de numero")
'''
'''
except Exception:   # Erros genericos 
    print("Coisa feia, tentando colocar texto no locar de numero")
'''

try:

    valor = int(input("Informe um valor numérico: "))

    print(f"\nO numero digitado foi {valor}")

except Exception as erro:   # colocando o erro na variavel "erro"

    print(f"Coisa feia, tentando colocar texto no locar de numer.\n\nO erro foi: {erro}\n\n")
