
def abrir(nome):
    entrada = open(nome, 'r')
    conteudo = entrada.read()
    entrada.close()
    print(conteudo)
    l = conteudo.split()
    print(l.index('?'))
    print(l)
    for x in l:
        print(x)
        if '?' in x:
            for y in x:
                print(x.find('?'))
    print(l)


def numChars(arquivo):
    arqEntrada = open(arquivo, 'r')
    contéudo = arqEntrada.read()
    arqEntrada.close()

    return len(contéudo)


def stringCount (arquivo, alvo):
    entrada = open(arquivo, 'r')
    contador = entrada.read()
    entrada.close()

    return contador.count(alvo)


def palavras (arquivo):
    entrada = open(arquivo, 'r')
    conteudo = entrada.read()
    entrada.close()
    tabela = str.maketrans('!,.?;', ' '*5)

    lista = conteudo.split()
    print(lista)
    lista = conteudo.translate(tabela)

    print(lista)

    return len(lista)


def linhas(arquivo):
    entrada = open(arquivo, 'r')
    listaLinha = entrada.readlines()
    entrada.close()
    print(listaLinha)
    return len(listaLinha)


def linhas02(arquivo):
    entrada = open(arquivo, 'r')
    for line in entrada:
        print(line, end='')
    entrada.close()


def meuGrep(arquivo, alvo):
    entrada = open(arquivo, 'r')
    for x in entrada:
        if alvo in x:
            print(x)


def saida(arquivo):
    entrada = open(arquivo, 'a')
    entrada.write('esta é a primeira linha.\n')
    entrada.write('esta é a segundas linha. ')
    entrada.write('\n usando o format para adiconar inteiros como:{}'.format(12))
    entrada.close()




def trocaPU(lista):
    lista[0], lista[-1] = lista[1], lista[0]
    print(lista)

lista = [1,2,3,4]
trocaPU(lista)

