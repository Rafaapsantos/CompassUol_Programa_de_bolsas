# Lista de 20 animais
animais = ['Leão', 'Zebra', 'Girafa', 'Elefante', 'Rinoceronte', 'Hipopótamo', 'Crocodilo', 'Tigre', 'Onça', 'Guepardo', 'Cachorro', 'Gato', 'Cavalo', 'Vaca', 'Ovelha', 'Cabra', 'Galinha', 'Pato', 'Ganso', 'Peru']

# Ordena a lista em ordem crescente
animais.sort()

# Imprime um nome em cada linha
[print(animal) for animal in animais]

# Salva a lista em um arquivo csv
with open("animais.csv", 'w', encoding='utf-8') as file:
    for animal in animais:
        file.write(f"{animal}\n")