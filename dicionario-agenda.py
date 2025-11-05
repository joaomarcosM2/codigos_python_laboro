agenda = dict() # iniciatizando um discionario


# Função Menu
def menu():
    print("\nAgenda Eletronnica\n")
    print("1- Inserir dados na agenda")
    print("2- Excluir dados da agenda")
    print("3- Consultar todos os dados da agenda")
    print("4- Sair do sitema")


#Função inserir dados 
def inserir():
    try: #  tratamento de erros 
            
        nome = input("\nQual o nome do contato: ")         #pass é ultilizado para não precisar codificar nada por enquanto
        agenda[nome] = int(input(f"\nQual o numero de {nome}: "))

        print("\nContato inserido com sucesso!")
        print(agenda)

    except Exception:
        print("\nOperação inválida. contato não salvo.")


#Função excluir dados 
def excluir(escolha):
    
    # Verificando se o contato existe antes de excluir.
    if escolha in agenda:       
        del agenda[escolha] 

        print("Dada excluido com sucesso!")
        print(agenda)

    else:
        print(f"O contato {escolha} não existe na agenda!")


#Função consultar dados 
def consultar():
    
    #ACESSANDO TANTO A CHAVE QUANTO VALOR
    for chave, valores in agenda.items(): 
        print(f"{chave} : {valores}")



while True:
     

    menu()

    resposta = int(input("Qual sua escolha: "))

    if resposta == 1:

        inserir()


    elif resposta == 2:       
        print(agenda)

        escolha = input("\nQual o nome do contato para excluir: ")

        excluir(escolha)

    elif resposta == 3:    
           
        print("\nDados da agenda:")

        consultar()


    elif resposta == 4:
        print("Sistema Encerrado")
        break