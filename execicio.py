'''
Escrever um algoritmo que leia um conjunto de números inteiros você deverá exibir somente os número ímpares. A leitura do valor 0 (zero) indica que o código terminou. 
'''

while True:
    numero = int(input("Digite um numero: "))

    if numero % 2 != 0:
        print (" Seu numero é: ",numero)


    if numero == 0:
        print("Sair")0

        break