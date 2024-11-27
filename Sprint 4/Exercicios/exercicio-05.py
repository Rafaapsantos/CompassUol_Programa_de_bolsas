linhas = []

with open('estudantes.csv') as data:
    for i in data:
        linhas.append(i.strip().split(','))

def nome(linha):
    return linha[0]

def notas(linha):
    return sorted(map(int, linha[1:]), reverse=True)[:3]

def media(linha):
    return round(sum(notas(linha)) / 3, 2)

for i in sorted(linhas, key=lambda x: x[0]):
    print(f'Nome: {nome(i)} Notas: {notas(i)} Média: {media(i)}')