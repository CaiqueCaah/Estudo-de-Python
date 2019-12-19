class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.preco = preco
