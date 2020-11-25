def contaPalavra (texto):
    y = texto.split()
    print(y)
    contador = {}
    for x in y:
        if x in contador:
            contador[x] += 1
        else:
            contador[x] = 1
    print(contador)
    print(contador['safira'])
    for z in contador:
        print('A palavra {:10} aparece {} vezes'.format(z, contador[z]))



def saida(arquivo):
    entrada = open(arquivo, 'a')
    entrada.write('esta é a primeira linha.\n')
    entrada.write('esta é a segundas linha. ')
    entrada.write('\n usando o format para adiconar inteiros como:{}'.format(12))
    entrada.close()


entrada = open('bovino.txt', 'r', encoding="utf-8")
conteudo = entrada.read().lower()
entrada.close()
tabela = str.maketrans('!,.?;', ' '*5)

lista = conteudo.translate(tabela).split()
print(lista)

contador = {}
for item in lista:
    if item in contador:
        contador[item] += 1
    else:
        contador[item] = 1
lista01 = str(contador)
listaTexto = contador.items()
lista01.split()
print(contador)

saida = open('resultadoBovino.txt', 'w', encoding="utf-8")
saida.writelines(str(contador))
saida.close()

'''abrir = open('bovino.txt', 'r')
conteudo = abrir.read().lower().split()
abrir.close()
saida = open('resultadoBovino.txt', 'a')
list = []

i = 0
for item in conteudo:
    cont = conteudo.count(item)
    saida.write(item +' '+ str(cont)+'\n')
    while item in conteudo:
        conteudo.remove(item)'''





