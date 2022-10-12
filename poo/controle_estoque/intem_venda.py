from webbrowser import get


class ItemVenda:

    def __init__(self, produto, quantidade, preco) -> None:
        self.__produto = produto
        self.__quantidade = quantidade
        self.__preco = preco

    def get_produto(self):
        return self.__produto

    def get_quantidade(self):
        return self.__quantidade

    def get_preco(self):
        return self.__preco
