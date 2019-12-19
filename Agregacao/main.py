from Agregacao.carrinho import Carrinho_de_compra
from Agregacao.produto import Produto

carrinho_de_compra = Carrinho_de_compra()

camisa = Produto('Camisa polo', 99.99)
tenis = Produto('Tenis Nike', 499.99)
calca = Produto('Calça Jeans', 129.99)

carrinho_de_compra.add_produtos(camisa)
carrinho_de_compra.add_produtos(tenis)
carrinho_de_compra.add_produtos(calca)

carrinho_de_compra.lista_produtos()
print(f'A soma de todos os produtos é de {carrinho_de_compra.soma_total_produtos()}')
