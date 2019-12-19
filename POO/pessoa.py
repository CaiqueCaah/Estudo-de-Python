# ENCAPSULAMENTO
# PARA COLOCAR UM ATRIBUTO PRIVADO É NECESSARIO COLOCAR '_' ANTES DO ATRIBUTO
# PARA UM PRIVADO SIMPLES APENAS 1 '_'
# PARA PRIVADO MAIS FORTE 2 '__'
# PARA VERIFICAR OS DADOS TERÁ QUE FAZER (OBJETO._NOMEDACLASSE__NOMEATRIBUTO)
from random import randint


class Pessoa:

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.__nome = nome
        self.__idade = idade
        self.__comendo = comendo
        self.__falando = falando

    @staticmethod
    def gera_id():
        """
        -> Metodo estatico
        :return: returna um id
        """
        rand = randint(10000, 19999)
        return rand

    # GETTER
    @property
    def nome(self):
        """
        -> GETTER
        @property é a anotação para criação dos getters e setters
        O nome do metodo tem que ser o mesmo do atributo
        :return: returna o nome
        """
        return self.__nome

    # SETTER
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
