class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def somar(self):
        return f'Somando: {self.x}+{self.y} = {self.x+self.y}'
    
    def subtrair(self):
        return f'Subtraindo: {self.x}-{self.y} = {self.x-self.y}'
    
calculo = Calculo(4,5)
print(calculo.somar())
print(calculo.subtrair())
