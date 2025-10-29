bibloteca = {}

entrada_saida = True
while  entrada_saida == True:

    print("\n=== MINHA BIBLIOTECA PESSOAL ===\n")

    print("\n1. Adicionar livro\n2. Consultar livro\n3. Atualizar páginas\n4. Remover livro\n5. Listar todos os livros\n6. Contar livros\n7. Sair\n")

    opcao = int(input("Digite uma opção: "))

    if  opcao == 1:
           
        nome = input("\nDigite o nome do livro: ")         
        bibloteca[nome] = int(input(f"\nDigite o número de páginas do'{nome}': "))

        print("Livro adicionado com sucesso!")

    elif opcao == 2:

        nome = input("\nDigite o nome do livro: ")         

        if nome in bibloteca:
            bibloteca[nome] = int(input(f"\nDigite o novo número de páginas do '{nome}': "))
        else:
            print("O nome do livro não existe.")


    elif opcao == 3:
        print()
  
    elif opcao == 4:
        print()
  
    elif opcao == 5:
        print()
  
    elif opcao == 6:
        print()
  



    elif opcao == 7:
        print("Sair")
        break
