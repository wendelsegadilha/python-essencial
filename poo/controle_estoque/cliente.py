class Cliente:

    def __init__(self, nome, cpf) -> None:
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
