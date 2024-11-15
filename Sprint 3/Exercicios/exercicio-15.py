class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
            self.ligada = True
            return self.ligada

    def desliga(self):
        self.ligada = False
        return self.ligada
        
        
    def esta_ligada(self):
        return self.ligada
        

lampada = Lampada(True)

lampada.liga()
print(f'A lâmpada está ligada? {lampada.esta_ligada()}')

lampada.desliga()
print(f'A lâmpada ainda está ligada? {lampada.esta_ligada()}')