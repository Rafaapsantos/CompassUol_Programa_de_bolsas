lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nova= []

def funcao_potencia(num) :
    return num**2

def my_map(list, f) :
    for i in list:
        lista_nova.append(f(i))

my_map(lista, funcao_potencia)

print(lista_nova)