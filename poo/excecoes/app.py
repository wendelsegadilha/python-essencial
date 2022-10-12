class MinhaException(RuntimeError):
    pass

class Calculadora():
    def dividir(self, valor1, valor2):
        try:
            return valor1 / valor2
        except:
            raise MinhaException("Divisao por zero, invalida")

if __name__ == '__main__':
    calc = Calculadora()
    calc.dividir(5, 0)