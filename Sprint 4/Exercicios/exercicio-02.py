def conta_vogais(texto:str)-> int:
    return len(list(filter(lambda x: x in 'aeiou', texto.lower())))
    
print(conta_vogais('RafaElA'))