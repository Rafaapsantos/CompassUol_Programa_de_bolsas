lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def separa_lista(lista):
    tamanho_lista = len(lista)
    divisao = tamanho_lista // 3
    primeira_lista = lista[:divisao]
    segunda_lista = lista[divisao:(2 * divisao)]
    terceira_lista = lista[(2* divisao):(3 * divisao)]
    print(primeira_lista, segunda_lista, terceira_lista)


separa_lista(lista)
    

