bibloteca = {}

entrada_saida = True
while  entrada_saida == True:

    print("\n=== MINHA BIBLIOTECA PESSOAL ===")

    print("-" * 32)
    print("\n1. Adicionar livro\n2. Consultar livro\n3. Atualizar páginas\n4. Remover livro\n5. Listar todos os livros\n6. Contar livros\n7. Sair\n")
    print("-" * 32)

    opcao = 0

    try:   
        opcao = int(input("|> Digite uma opção: "))

    except Exception as erro:  

        print(f"\n\nATENÇÃO!!!\n\nMESSAGEM DO SEU DEV JÙNIOR:\nCoisa feia, tentando colocar texto no locar de numero.\n\nO erro foi: {erro}\n\n")


    if  opcao == 1:   # Adicionar livro
                       
        nome = input("\n|> Digite o nome do livro: ")         
        bibloteca[nome] = int(input(f"\n|> Digite o número de páginas do '{nome}': "))

        print("\n  #  Livro adicionado com sucesso!  \n")


    elif opcao == 2:   # Consultar livro

        print("\n\n=== CONSULTAR LIVROS ===\n")
        nome = input("\n|> Digite o nome do livro: ")         

        if nome in bibloteca:

            for chave, valores in bibloteca.items():

                if nome == chave:

                    print(f"\n  #  O livro '{nome}' tem {valores} páginas!\n")

        else:
            print("\n  #  O nome do livro não existe.")


    elif opcao == 3:   # Atualizar páginas
        print("\n\n=== ATUALIZAÇÃO DE LIVROS ===\n")
        nome = input("\n|> Digite o nome do livro: ")         

        if nome in bibloteca:
            bibloteca[nome] = int(input(f"\n|> Digite o novo número de páginas do '{nome}': "))

            print("\n  #  Livro atualizado com sucesso! \n")
        else:
            print("\n  #  O nome do livro não existe.")
  

    elif opcao == 4:   # Remover livro
        
        print("\n\n===  REMOVER LIVROS ===\n")
        nome = input("\n|> Digite o nome do livro para remoção: ")     

        if nome in bibloteca:
           del bibloteca[nome]

           print("\n  #  Livro removido com sucesso! \n")          
        else:
           print("\n  #  O nome do livro não existe.")


    elif opcao == 5:   # Listar todos os livros
        print("\n\n=== LIVROS NA BIBLIOTECA ===\n\n")

        for chave, valores in bibloteca.items(): 
            print(f"- {chave}: {valores} páginas\n")

  
    elif opcao == 6:   # Contar livros
        print("\n\n=== QUANTEDADE DE LIVROS  ===\n")

        quantidade = len(bibloteca)        
        print(f"  #  A quantidade de livros existentes na biblioteca é {quantidade}!\n")


    elif opcao == 7:   # Sair
        print("\n  #  Obrigado por visitar a nossa biblioteca, até mais tarde!\n\n")
        break
