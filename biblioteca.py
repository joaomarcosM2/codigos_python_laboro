bibloteca = {}


def menu(opcao):    # Função Menu

    print("\n=== MINHA BIBLIOTECA PESSOAL ===")

    print("-" * 32)
    print("\n1. Adicionar livro\n2. Consultar livro\n3. Atualizar páginas\n4. Remover livro\n5. Listar todos os livros\n6. Contar livros\n7. Sair\n")
    print("-" * 32)

    
    try:   
        opcao = int(input("|> Digite uma opção: "))

        return opcao

    except Exception as erro:  

        print(f"\n\nATENÇÃO!!!\n\nMESSAGEM DO SEU DEV JÙNIOR:\nCoisa feia, tentando colocar texto no lugar de numero.\n\nO erro foi: {erro}\n\n")



def adicionar():   # Função Adicionar livro

    nome = input("\n|> Digite o nome do livro: ")        

    bibloteca[nome] = int(input(f"\n|> Digite o número de páginas do '{nome}': "))

    print("\n  #  Livro adicionado com sucesso!  \n")



def consultar():   # Função Consultar livro

        print("\n\n=== CONSULTAR LIVROS ===\n")
        nome = input("\n|> Digite o nome do livro: ")         

        if nome in bibloteca:

            for chave, valores in bibloteca.items():

                if nome == chave:

                    print(f"\n  #  O livro '{nome}' tem {valores} páginas!\n")

        else:
            print("\n  #  O nome do livro não existe.")



def atualizar():   # Função Atualizar páginas

        print("\n\n=== ATUALIZAÇÃO DE LIVROS ===\n")
        nome = input("\n|> Digite o nome do livro: ")         

        if nome in bibloteca:
            bibloteca[nome] = int(input(f"\n|> Digite o novo número de páginas do '{nome}': "))

            print("\n  #  Livro atualizado com sucesso! \n")
        else:
            print("\n  #  O nome do livro não existe.")
  



def remover():    # Fução Remover livro

        print("\n\n===  REMOVER LIVROS ===\n")
        nome = input("\n|> Digite o nome do livro para remoção: ")     

        if nome in bibloteca:
           del bibloteca[nome]

           print("\n  #  Livro removido com sucesso! \n")          
        else:
           print("\n  #  O nome do livro não existe.")



def listar():     # Função Listar todos os livros

        print("\n\n=== LIVROS NA BIBLIOTECA ===\n\n")

        for chave, valores in bibloteca.items(): 
            print(f"- {chave}: {valores} páginas\n")



def contar():     # Função Contar livros
         
        print("\n\n=== QUANTEDADE DE LIVROS  ===\n")

        quantidade = len(bibloteca)        
        print(f"  #  A quantidade de livros existentes na biblioteca é {quantidade}!\n")



def sair(entrada_saida):  # Função Sair
     
        print("\n  #  Obrigado por visitar a nossa biblioteca, até mais tarde!\n\n")
        
        return  False
        


entrada_saida = True
while  entrada_saida == True:

    opcao = 0
    
    opcao = menu(opcao)


    if  opcao == 1:    # Adicionar livro
                       
        adicionar()


    elif opcao == 2:   # Consultar livro
       
        consultar()


    elif opcao == 3:   # Atualizar páginas

        atualizar()


    elif opcao == 4:   # Remover livro
        
        remover()

       
    elif opcao == 5:   # Listar todos os livros
      
        listar()
         

    elif opcao == 6:   # Contar livros
       
        contar()


    elif opcao == 7:   # Sair

        entrada_saida = sair(entrada_saida)

  