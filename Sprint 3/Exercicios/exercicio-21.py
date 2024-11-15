class Passaro: 
    def voar(self):
        print('Voando...')

    def emitir_som(self):
        pass



class Pato(Passaro):
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome} emitindo som... \nQuack Quack')

    
class Pardal(Passaro):
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome} emitindo som...\nPiu Piu')

    

pato = Pato('Pato')
print(pato.nome)
pato.voar()
pato.emitir_som()

pardal = Pardal('Pardal')
print(pardal.nome)
pardal.voar()
pardal.emitir_som()
