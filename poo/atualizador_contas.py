
from conta import Conta


class AtualizadorContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def selic(self):
        return self._selic

    @selic.setter
    def selic(self, selic):
        self._selic = selic

    @property
    def saldo_total(self):
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self, saldo_total):
        self._saldo_total = saldo_total

    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta.saldo))
        self._saldo_total += conta.atualiza(self._selic)
        print("Saldo Final: {}".format(self._saldo_total))

if __name__ == '__main__':
    c = Conta('123-4', 'Wendel', 1500.0, 500)

    adc = AtualizadorContas(0.01)

    adc.roda(c)

    adc
    
    