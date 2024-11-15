class Pessoa():
    def __init__(self, id, *nome):
        self.id = id
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_novo):
        self.__nome = nome_novo

pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
