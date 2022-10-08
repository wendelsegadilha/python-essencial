class Historico:
    def __init__(self):
        self.transacoes = []
    
    def imprime(self):
        print("TRANSACOES: ")
        for t in self.transacoes:
            print('-', t)