
#GRAVANDO EM ARQUIVO
arquivo = open('file.txt', 'w')

arquivo.write('Wendel ')
arquivo.write('Alves')

arquivo = open('file.txt', 'a')
arquivo.write('\nVenes Lopes')

arquivo.close

#LENDO ARQUIVOS
arquivo_ler = open('file2.txt', 'r')
for linha in arquivo_ler:
    print(linha.strip())

arquivo_ler.close()


arquivo_ler = open('file2.txt', 'r')
print(arquivo_ler.readlines())
arquivo_ler.close()

arquivo_ler = open('file2.txt', 'r')
print(arquivo_ler.read())
arquivo_ler.close()

with open('file2.txt') as arquivo:
    for linha in arquivo:
        print(linha.strip())


