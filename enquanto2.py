# Forma Condicional
'''
senha = 123 # inicializando a viriavel

while senha != 1234:
    senha = int(input("Enforme a sua senha: "))

print("Obrigado por usar o sistema!!!")
'''

# Forma Condicional 2

tentativas = 3

while True:

    senha = input("Enforme a sua senha: ")
 
    if senha == "aluno2" and tentativas > 0:

        print("Senha correta!!!")

        break # este comando irá incerrar o while.


    if tentativas > 0:

        tentativas -= 1 # está diminuindo as tentativas

    if tentativas <= 0:
         
         print("Sem tentativas, só lamento")
         break # este comando irá incerrar o while.
