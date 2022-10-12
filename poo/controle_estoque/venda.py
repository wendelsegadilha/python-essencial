from time import sleep
from typing import Type
from webbrowser import get
from cliente import Cliente
from intem_venda import ItemVenda

class Venda:

    __quantidade_venda = 0

    def __init__(self, cliente: Type[Cliente], itens_venda) -> None:
        self.__cliente = cliente
        self.__itens_venda = itens_venda
        self.__desconto = 0.0
        Venda.__quantidade_venda += 1 

    @staticmethod
    def get_qtd_venda():
        return Venda.__quantidade_venda

    def get_cliente(self):
        return self.__cliente

    def get_itens_venda(self):
        return self.__itens_venda

    def set_desconto(self, desconto):
        self.__desconto = desconto

    def get_preco_total(self):
        return self.calcular_preco_total()

    def calcular_preco_total(self):
        preco_total = 0.0

        for it in self.__itens_venda:
            preco_total += (it.get_preco() * it.get_quantidade()) 

        if self.__desconto > 0:
            preco_total = preco_total - (preco_total * (self.__desconto/100))
            return preco_total

        return preco_total

    


