primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
dados_completos = []

for i, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {primeirosNomes} {sobreNomes} está com {idades} anos")
