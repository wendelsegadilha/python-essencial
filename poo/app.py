from conta import Conta;
from cliente import Cliente;

cliente1 = Cliente('Wendel', 'Segadilha', '12345678930')
cliente2 = Cliente('Venes', 'Lopes', '14785236978')

conta1 = Conta('123-7', cliente1, 500.0)
conta2 = Conta('951-3', cliente2, 1150.0, 500)

conta1.deposita(100)
conta1.extrato()
conta1.saca(50)
conta1.extrato()
conta1.transfere_para(conta2, 250)
conta1.extrato()

conta1.historico.imprime()

conta2.historico.imprime()