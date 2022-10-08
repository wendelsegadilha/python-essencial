def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular":titular, "saldo":saldo, "limite":limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

conta1 = cria_conta('123-7', 'Joao', 500.0, 1000.0)

deposita(conta1, 100.0)
extrato(conta1)
saca(conta1, 50)
extrato(conta1)