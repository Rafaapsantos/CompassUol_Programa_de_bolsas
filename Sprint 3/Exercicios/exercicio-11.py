import json 

abre_arquivo = open('person.json')

with abre_arquivo as arquivo:
    le_arquivo = json.load(arquivo)

print(le_arquivo)