

agenda = {"Maria":1234,"Pedro":4321,"joana":9876}
contato = {"nome":"Claudio", "Idade":45}     # Exemplo

print(type(agenda))  # verificar o tipo

print(agenda)

print("-" * 60)  

print(agenda["Maria"])  # mostrar o conteúdo da chave

print(f"  Nome: {contato["nome"]}  Idade: {contato['Idade']} ")  # Exemplo


# INSERINDO DADOS NA AGENDA
#FORMA 1

agenda["José"] = 145
print(agenda)


#Forma 2
agenda.update({"Claudia":2222}) # update pode inserir um novo valor
print(agenda)

agenda.update({"joana":6789})   # update pode alterar um valor já existente
print(agenda)


# EXCLUINDO DADOS DA AGENDA
#FORMA 1
agenda.pop("Pedro")
print(agenda)


##Forma 2
del agenda ["Maria"]
print(agenda)

