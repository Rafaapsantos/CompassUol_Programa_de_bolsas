numeros = "1,3,4,6,10,76"
lista_numeros = numeros.split(',')
lista_numeros = [int(i) for i in lista_numeros]
soma = 0

for i in lista_numeros: 
    if i: 
        soma += i

print(soma)



