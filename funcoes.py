def velocidade(distancia, tempo):
    velocidade = distancia/tempo
    return velocidade

vel_meida = velocidade(100, 20)
print(vel_meida)

def calculadora(x, y):
    return {'soma':x+y, 'subtracao':x-y, 'multiplicacao':x*y, 'divisao':x/y}

retorno = calculadora(10, 5)
print(retorno['multiplicacao'])

def teste(arg, *args):
    print(arg)
    for a in args:
        print(a)

lista = [1,2,3]
teste('wendel', 'a','b',1)
teste('wendel', *lista)

def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

minha_funcao(nome='Wendel')
lang = {'java':'Bom', 'python':'legal'}
minha_funcao(**lang)