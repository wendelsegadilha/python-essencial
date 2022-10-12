from cliente import Cliente
from produto import Produto
from intem_venda import ItemVenda
from venda import Venda

c1 = Cliente("Wendel", "12354789632")

p1 = Produto("Cadeira Gamer XTZ", "Escritorio", 1500.45)
p2 = Produto("Monitor LCD LED 32", "Lazer", 3500.00)

it1 = ItemVenda(p1, 2, 1500.45)
it2 = ItemVenda(p2, 5, 3400.00)

v1 = Venda(c1, [it1, it2])
v2 = Venda(c1, [it1, it2])
v3 = Venda(c1, [it1, it2])
v4 = Venda(c1, [it1, it2])
v5 = Venda(c1, [it1, it2])

preco_total = v1.get_preco_total()
print("Valor total da veda: {}".format(preco_total))

v1.set_desconto(10)
preco_total = v1.get_preco_total()
print('Valor total da veda com 10% de desconto: {}'.format(preco_total))

qtd_venda = Venda.get_qtd_venda()
print("Qauntidade de Vendas: {}".format(qtd_venda))

