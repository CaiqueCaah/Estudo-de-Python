# PALAVRA RESERVADA DEF INFORMA QUE É UMA FUNÇÃO
# PARA DOCUMENTAR A FUNÇÃO APENAS COLOCAR 3 ASPAS DUPLAS"""

def mostra_linha():
    """
    -> Mostra uma linha com 40 traços
    :return: Sem retorno
    """
    print("-" * 40 )


def mensagem(msg):
    """
    -> Mostra uma mensagem
    :param msg: Mensagem passada pelo usuario
    :return: Sem retorno
    """
    mostra_linha()
    print(msg)
    mostra_linha()


msg = str("Mensgem para aparecer na tela !")

mostra_linha()
print("\t\t\tCurso de Python")
mostra_linha()

mensagem(msg)

# MOSTRA A DOCUMENTAÇÂO DO METODO
help(mensagem)
