from datetime import datetime
import re
from historico import Historico;

class Conta:

    identificador = 1

    __slot__ = ['_numero', '_titular', '_saldo', '_limite', '_data_abertura', '_historico']

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._data_abertura = datetime.today()
        self._historico = Historico()
        self.identificador = Conta.identificador
        Conta.identificador += 1
        print("Conta {} criada em {}".format(self._numero, self._data_abertura))

    @property
    def historico(self):
        return self._historico
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("saldo nao pode ser negativo")
        else:
            self._saldo = saldo
    
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

    