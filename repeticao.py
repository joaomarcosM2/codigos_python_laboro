
# Range() nao conta o valor final, ele ignora, se eu quiser exiber o valor final devo colocar ele + 1

#EXEMPLO 1
for contador in range(1, 11):
    print(contador)


print("-" * 50)

# O -1 indica que o intervalo irá de -1 em -1, isto é o passo a passo do valor inicial até o valor final.

#EXEMPLO 2
for contador in range(10,0,-1):
    print(contador,end=" ")      


print("\n")
print("-" * 50)


#EXEMPLO 3
for contador in range (0,21,2):
    print(contador, end=", ")