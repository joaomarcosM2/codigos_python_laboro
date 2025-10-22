agenda = dict() # iniciatizando um discionario

while True:
    print("\nAgenda Eletronnica\n")
    print("1- Inserir dados na agenda")
    print("2- Excluir dados da agenda")
    print("3- Sair do sitema")
    resposta = int(input("Qual sua escolha: "))

    if resposta == 1:

        nome = input("\nQual o nome do contato: ")         #pass é ultilizado para não precisar codificar nada por enquanto

        agenda[nome] = int(input(f"\nQual o numero de {nome}: "))

        print("\nContato inserido com sucesso!")
        print(agenda)

    elif resposta == 2:       
        print(agenda)

        escolha = input("\nQual o nome do contato para excluir: ")

        # Verificando se o contato existe antes de excluir.
        if escolha in agenda:       
            del agenda[escolha] 

            print("Dada excluido com sucesso!")
            print(agenda)

        else:
            print(f"O contato {escolha} não existe na agenda!")


    elif resposta == 3:
        print("Sistema Encerrado")
        break