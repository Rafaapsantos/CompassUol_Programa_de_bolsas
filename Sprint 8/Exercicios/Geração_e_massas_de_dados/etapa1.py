import random

numeros = []

# Gera 250 números inteiro aleatórios entre 1 e 1000
for x in range(1,251):
    numeros.append(random.randint(0,1000))

# Reverte a lista de números
numeros.reverse()

# Imprime o resultado
print('Números com o reverse:')
print(numeros)