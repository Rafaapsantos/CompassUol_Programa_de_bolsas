lista_palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in lista_palavras:
    if i == i[::-1]:
        print(f'A palavra: {i} é um palíndromo')
    else:
        print(f'A palavra: {i} não é um palíndromo')

