from Agregacao.produto import Produto


class Carrinho_de_compra:

    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos

    def add_produtos(self, produto):
        """
        -> Adiciona um novo produto na lista produtos
        :param produto: Objeto do tipo Produto
        :return: Sem Retorno
        """
        self.__produtos.append(produto)

    def lista_produtos(self):
        """
        -> Lista todos os produtos salvos
        :return: Sem retorno
        """
        for produto in self.__produtos:
            print(f'Nome: {produto.nome} - Preço: {produto.preco}')

    def soma_total_produtos(self):
        """
        -> Soma os preços de todos os produtos
        :return: Retorna a soma de todos os preços
        """
        total = 0

        for produto in self.__produtos:
            total += produto.preco

        return total
