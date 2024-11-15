class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor= 'Azul'):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor

    def __str__(self):
        return f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}'
    

primeiro_aviao = Aviao('BOIENG456', '1500 km/h', '400', 'Azul')  
segundo_aviao = Aviao('Embraer Praetor 600', '863km/h', '14', 'Azul')
terceiro_aviao = Aviao('Antonov An-2', '258', '12', 'Azul')

lista = []
lista.append(primeiro_aviao)
lista.append(segundo_aviao)
lista.append(terceiro_aviao)

for i in lista:
    print(i)