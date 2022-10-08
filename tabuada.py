numero = int(input('Informe um número inteiro: '))

print("TABUADA COM WHILE")
cont = 1
while(cont <= 10):
    print("{} x {} = {}".format(cont, numero, (cont * numero)))
    cont += 1


print("TABUADA COM FOR")
for c in range(0, 15):
    if(c > 10):
        break
    print("{} x {} = {}".format(c, numero, (c * numero)))
