class Produto:

    def __init__(self, nome, categoria, preco) -> None:
        self.__nome = nome
        self.__categoria = categoria
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def __str__(self) -> str:
        return "Nome: {} - Categoria: {} - Preco: {}".format(self.__nome, self.__categoria, self.__preco)


