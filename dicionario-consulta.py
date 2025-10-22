alimentos = {"Arroz":5.99,"Café":14,"Feijão":7.69}

"""
Dicionario
chave: valor -> item

chave - key
valor - value
item  - item

"""

print(alimentos)


print("-" * 60) #

#ACESSANDO APENAS AS CHAVES
for chave in alimentos.keys():
    print(chave)

print("-" * 60) #

#ACESSANDO APENAS OS VALORES
for valores in alimentos.values():
    print(valores)

print("-" * 60) #

#ACESSANDO TANTO A CHAVE QUANTO VALOR
for chave, valores in alimentos.items():
    print(f"{chave} : {valores}")