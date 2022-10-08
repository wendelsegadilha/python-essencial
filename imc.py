peso =  int(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura**altura)

"""
Menos do que 18,5	Abaixo do peso
Entre 18,5 e 24,9	Peso normal
Entre 25 e 29,9	Sobrepeso
Entre 30 e 34,9	Obesidade grau 1
Entre 35 e 39,9	Obesidade grau 2
Mais do que 40	Obesidade grau 3
"""

if imc < 18.5:
    print("Seu IMC é {:.2f} e você está abaixo do peso".format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print("Seu IMC é {:.2f} e seu Peso está normal".format(imc))
elif imc >= 25 and imc <= 29.9:
    print("Seu IMC é {:.2f} e você está com sobrepeso".format(imc))
elif imc >= 30 and imc <= 34.9:
    print("Seu IMC é {:.2f} e você está com obesidade grau 1".format(imc))
elif imc >= 35 and imc <= 39.9:
    print("Seu IMC é {:.2f} e você está com obesidade grau 2".format(imc))
else:
    print("Seu IMC é {:.2f} e você está com obesidade grau 3".format(imc))






