from datetime import datetime
from historico import Historico;

class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = datetime.today()
        self.historico = Historico()
        print("Conta {} criada em {}".format(self.numero, self.data_abertura))
    
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True
    
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para a conta {}".format(valor, destino.numero))
            return True
        else:
            return False

    def extrato(self):
        print("EXTRATO: ")
        print("numero: {} \nsaldo: {} \ntitular: {} \ncpf: {}".format(self.numero, self.saldo, self.titular.nome, self.titular.cpf))
        self.historico.transacoes.append("tirou o extrato em {}".format(datetime.today()))

    