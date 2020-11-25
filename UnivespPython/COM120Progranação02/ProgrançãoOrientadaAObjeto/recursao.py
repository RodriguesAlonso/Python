import math


def imprime(l, i=0):
    if i < len(l):
        print(l[i])
        imprime(l, i+1)


def geralist(tamanho=10):
    from random import randrange
    listag = []
    for x in range(tamanho):
        listag.append(randrange(0, tamanho))
    return listag


def fatora(nun):
    if nun == 0:
        return 1
    else:
        fat = nun * fatora(nun-1)
        return fat


def fibo(n):
    if n < 2:
        return n
    else:
        f = (fibo(n - 1) + fibo(n - 2))
        return f


def vertical(x):
    if x < 10:
        print(x)
    else:
        vertical(x//10)
        print(x % 10)


def reverso(x):
    if x < 10:
        print(x)
    else:
        print(x % 10)
        reverso(x//10)


def saude(n):
    if n == 0:
        print('Hurrah!!!')
    else:
        print('hip', end=' ')
        saude(n-1)


def maiorelemento(l):
    if l == 1:
        max(l)
        return l


def pattern(n):
    if n == 0:
        print(0, end='')
    else:
        pattern(n-1)
        print(n, end='')
        pattern(n -1)


def pattern2(n):
    if n == 0:
        print('')
    elif n == 1:
        print('*')
    else:
        pattern2(n - 1)
        print('*' * n)
        pattern2(n - 1)


def timeanalise(func, start, stop, inc, runs):
    for n in range(start, stop, inc):
        acc = 0.0
        for i in range(runs):
            acc += timeanalise(func, n)
        formatstr = 'Tempo de execução de {}({}) é {:.7f} segundos'
        print(formatstr.format(func._name_, n, acc/runs))


def listsum(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        print(lista)
        return lista[0] + listsum(lista[1:])


